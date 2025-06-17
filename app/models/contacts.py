from app.models.database import get_db
from datetime import datetime, timedelta
import json

def save_contact(name, email, phone, issue, message, source, utm_source, utm_medium, utm_campaign, utm_term, utm_content):
    db = get_db()
    db.execute(
        'INSERT INTO contacts (name, email, phone, issue, message, source, utm_source, utm_medium, utm_campaign, utm_term, utm_content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (name, email, phone, issue, message, source, utm_source, utm_medium, utm_campaign, utm_term, utm_content)
    )
    db.commit()

def get_lead_by_id(lead_id):
    """Busca um lead específico pelo ID"""
    db = get_db()
    lead = db.execute('''
        SELECT 
            id, name, email, phone, issue, message,
            source, utm_source, utm_medium, utm_campaign, utm_term, utm_content,
            strftime('%d/%m/%Y %H:%M', created_at) as formatted_created_at,
            created_at
        FROM contacts 
        WHERE id = ?
    ''', (lead_id,)).fetchone()
    return lead

def update_lead(lead_id, name, email, phone, issue, message, source, utm_source, utm_medium, utm_campaign, utm_term, utm_content):
    """Atualiza um lead existente"""
    try:
        db = get_db()
        
        # Sincronizar fonte: UTM Source tem prioridade sobre Fonte manual
        final_source = utm_source if utm_source and utm_source.strip() else source
        
        # Debug: log dos dados antes da atualização
        print(f"Atualizando lead ID {lead_id}:")
        print(f"  Nome: {name}")
        print(f"  Email: {email}")
        print(f"  Telefone: {phone}")
        print(f"  Assunto: {issue}")
        print(f"  Fonte original: {source}")
        print(f"  UTM Source: {utm_source}")
        print(f"  Fonte final (sincronizada): {final_source}")
        print(f"  UTM Campaign: {utm_campaign}")
        
        cursor = db.execute('''
            UPDATE contacts 
            SET name = ?, email = ?, phone = ?, issue = ?, message = ?,
                source = ?, utm_source = ?, utm_medium = ?, utm_campaign = ?, utm_term = ?, utm_content = ?
            WHERE id = ?
        ''', (name, email, phone, issue, message, final_source, utm_source, utm_medium, utm_campaign, utm_term, utm_content, lead_id))
        
        rows_affected = cursor.rowcount
        print(f"Linhas afetadas na atualização: {rows_affected}")
        
        db.commit()
        
        # Verificar se a atualização foi bem-sucedida
        updated_lead = db.execute('''
            SELECT name, email, phone, issue, source, utm_source, utm_campaign
            FROM contacts WHERE id = ?
        ''', (lead_id,)).fetchone()
        
        if updated_lead:
            print(f"Dados após atualização: {dict(updated_lead)}")
        else:
            print(f"ERRO: Lead {lead_id} não encontrado após atualização!")
            
    except Exception as e:
        print(f"ERRO na função update_lead: {str(e)}")
        raise e

def delete_lead(lead_id):
    """Exclui um lead"""
    db = get_db()
    db.execute('DELETE FROM contacts WHERE id = ?', (lead_id,))
    db.commit()

def get_all_leads_with_details():
    """Busca todos os leads com informações completas para a tabela do admin"""
    db = get_db()
    leads = db.execute('''
        SELECT 
            id, name, email, phone, issue, message,
            source, utm_source, utm_medium, utm_campaign, utm_term, utm_content,
            strftime('%d/%m/%Y %H:%M', created_at) as formatted_created_at,
            created_at
        FROM contacts 
        ORDER BY created_at DESC
    ''').fetchall()
    return leads

def get_lead_sources():
    db = get_db()
    sources = db.execute('''
        SELECT 
            source,
            COUNT(*) as total,
            COUNT(CASE 
                WHEN created_at >= datetime('now', '-30 days') 
                THEN 1 
            END) as last_30_days
        FROM contacts 
        GROUP BY source
        ORDER BY total DESC
    ''').fetchall()
    return sources

def get_lead_details():
    db = get_db()
    leads = db.execute('''
        SELECT 
            name,
            email,
            source,
            utm_campaign,
            utm_medium,
            strftime('%d/%m/%Y %H:%M', created_at) as created_at
        FROM contacts 
        ORDER BY created_at DESC
        LIMIT 100
    ''').fetchall()
    return leads

def get_dashboard_data():
    """Gera dados para o dashboard, incluindo estatísticas de leads e conversão"""
    db = get_db()
    
    # Dados para gráfico de leads por mês (últimos 6 meses)
    monthly_leads = db.execute('''
        SELECT 
            strftime('%m/%Y', created_at) as month,
            COUNT(*) as total
        FROM contacts 
        WHERE created_at >= datetime('now', '-6 months')
        GROUP BY strftime('%m/%Y', created_at)
        ORDER BY created_at ASC
    ''').fetchall()
    
    # Dados para gráfico de leads por fonte
    leads_by_source = db.execute('''
        SELECT 
            COALESCE(source, 'Direto') as source,
            COUNT(*) as total
        FROM contacts 
        GROUP BY source
        ORDER BY total DESC
        LIMIT 5
    ''').fetchall()
    
    # Dados para gráfico de leads por campanha
    leads_by_campaign = db.execute('''
        SELECT 
            COALESCE(utm_campaign, 'Sem campanha') as campaign,
            COUNT(*) as total
        FROM contacts 
        GROUP BY utm_campaign
        ORDER BY total DESC
        LIMIT 5
    ''').fetchall()
    
    # Totalizadores
    totals = db.execute('''
        SELECT 
            COUNT(*) as total_leads,
            COUNT(CASE WHEN created_at >= datetime('now', '-30 days') THEN 1 END) as last_30_days,
            COUNT(CASE WHEN created_at >= datetime('now', '-7 days') THEN 1 END) as last_7_days,
            COUNT(DISTINCT source) as total_sources
        FROM contacts
    ''').fetchone()
    
    # Taxa de crescimento (comparação mês atual vs mês anterior)
    growth_rate = db.execute('''
        SELECT 
            (SELECT COUNT(*) FROM contacts WHERE created_at >= datetime('now', 'start of month')) as current_month,
            (SELECT COUNT(*) FROM contacts WHERE 
                created_at >= datetime('now', 'start of month', '-1 month') AND 
                created_at < datetime('now', 'start of month')) as previous_month
    ''').fetchone()
    
    # Calcular taxa de crescimento
    current = growth_rate['current_month'] or 0
    previous = growth_rate['previous_month'] or 1  # Evitar divisão por zero
    growth_percentage = ((current - previous) / previous) * 100 if previous > 0 else 0
    
    # Formatar para JSON para uso nos gráficos
    chart_data = {
        'monthly_leads': {
            'labels': [row['month'] for row in monthly_leads],
            'data': [row['total'] for row in monthly_leads]
        },
        'leads_by_source': {
            'labels': [row['source'] for row in leads_by_source],
            'data': [row['total'] for row in leads_by_source]
        },
        'leads_by_campaign': {
            'labels': [row['campaign'] for row in leads_by_campaign],
            'data': [row['total'] for row in leads_by_campaign]
        }
    }
    
    return {
        'chart_data': chart_data,
        'totals': totals,
        'growth_percentage': round(growth_percentage, 1)
    }

def get_qualified_leads():
    """
    Qualifica leads com base em critérios específicos para o contexto da Consultoria Calazans.
    
    Critérios de pontuação:
    - Menção a dor/lesão/recuperação no assunto ou mensagem: +3 pontos
    - Menção a pós-parto/gravidez/maternidade: +3 pontos
    - Fonte específica (Instagram, Google): +2 pontos
    - Campanha específica relacionada a recuperação: +2 pontos
    - Tempo de resposta (leads mais recentes): +1 ponto
    """
    db = get_db()
    
    # Buscar leads com informações completas
    leads = db.execute('''
        SELECT 
            id,
            name,
            email,
            phone,
            issue,
            message,
            source,
            utm_campaign,
            created_at,
            strftime('%d/%m/%Y', created_at) as formatted_date
        FROM contacts 
        ORDER BY created_at DESC
    ''').fetchall()
    
    qualified_leads = []
    
    # Palavras-chave para pontuação
    pain_keywords = ['dor', 'lesão', 'lesao', 'lombar', 'coluna', 'hérnia', 'hernia', 'recuperação', 'recuperacao', 'dores', 'muscular']
    maternity_keywords = ['gravidez', 'pós-parto', 'pos-parto', 'gestante', 'mãe', 'mae', 'bebê', 'bebe', 'amamentação', 'amamentacao']
    
    for lead in leads:
        score = 0
        reasons = []
        
        # Verificar assunto e mensagem para palavras-chave
        issue_text = (lead['issue'] or '').lower()
        message_text = (lead['message'] or '').lower()
        
        # Pontuação para dor/lesão
        if any(keyword in issue_text or keyword in message_text for keyword in pain_keywords):
            score += 3
            reasons.append("Mencionou dor ou lesão")
        
        # Pontuação para maternidade
        if any(keyword in issue_text or keyword in message_text for keyword in maternity_keywords):
            score += 3
            reasons.append("Contexto de maternidade")
        
        # Pontuação para fonte
        if lead['source'] in ['instagram', 'google', 'facebook']:
            score += 2
            reasons.append(f"Via {lead['source'].capitalize()}")
        
        # Pontuação para campanha
        campaign = (lead['utm_campaign'] or '').lower()
        if any(keyword in campaign for keyword in ['recuperacao', 'recuperação', 'lombar', 'hernia', 'postura', 'mulher']):
            score += 2
            reasons.append(f"Campanha relevante: {lead['utm_campaign']}")
        
        # Pontuação para leads recentes (últimos 7 dias)
        lead_date = datetime.strptime(lead['created_at'], '%Y-%m-%d %H:%M:%S')
        if (datetime.now() - lead_date) <= timedelta(days=7):
            score += 1
            reasons.append("Lead recente")
        
        # Classificação baseada na pontuação
        if score >= 6:
            qualification = "Alta prioridade"
        elif score >= 3:
            qualification = "Média prioridade"
        else:
            qualification = "Baixa prioridade"
        
        qualified_leads.append({
            'id': lead['id'],
            'name': lead['name'],
            'email': lead['email'],
            'phone': lead['phone'],
            'issue': lead['issue'],
            'source': lead['source'] or 'Direto',
            'created_at': lead['formatted_date'],
            'score': score,
            'qualification': qualification,
            'reasons': reasons
        })
    
    # Ordenar por pontuação (maior para menor)
    return sorted(qualified_leads, key=lambda x: x['score'], reverse=True) 
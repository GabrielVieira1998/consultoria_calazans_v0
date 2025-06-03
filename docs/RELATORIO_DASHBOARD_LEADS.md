# Documentação do Dashboard de Relatórios e Sistema de Qualificação de Leads

## Visão Geral

Este documento descreve a implementação do dashboard de relatórios e do sistema de qualificação de leads para a Consultoria Calazans. Estas funcionalidades foram desenvolvidas para proporcionar à administradora uma visão abrangente do desempenho de marketing e uma forma de priorizar leads baseado em critérios relevantes para o contexto de recuperação física feminina.

## Tecnologias Utilizadas

- **Backend**: Python com Flask
- **Frontend**: HTML, CSS, JavaScript
- **Visualização de Dados**: Chart.js
- **Banco de Dados**: SQLite
- **Componentes UI**: Bootstrap 5

## Arquivos Modificados/Criados

1. **Modelos (app/models/contacts.py)**
   - Adição de `get_dashboard_data()` para gerar dados para os gráficos
   - Adição de `get_qualified_leads()` para aplicar pontuação aos leads

2. **Rotas (app/routes/admin.py)**
   - Atualização da rota `/reports` para incluir dados do dashboard
   - Adição da rota `/reports/qualified-leads` para exibir leads qualificados
   - Adição da rota API `/api/dashboard-data` para acesso aos dados via JSON

3. **Templates**
   - Atualização de `app/templates/admin/reports.html` para exibir dashboard
   - Criação de `app/templates/admin/qualified_leads.html` para exibir leads qualificados

## Funcionalidades Implementadas

### 1. Dashboard de Relatórios

O dashboard interativo proporciona uma visão geral das métricas de leads em quatro seções principais:

#### A. Cards de Métricas

Quatro métricas-chave são exibidas na parte superior do dashboard:
- **Total de Leads**: Contagem total de leads no sistema
- **Leads nos últimos 30 dias**: Atividade recente mensal
- **Leads na última semana**: Atividade muito recente
- **Crescimento no mês atual**: Comparativo percentual em relação ao mês anterior (com indicador visual de crescimento ou queda)

#### B. Gráfico de Leads por Mês

- Gráfico de barras mostrando a tendência de captação de leads nos últimos 6 meses
- Permite visualizar sazonalidade e avaliar o desempenho de campanhas ao longo do tempo

#### C. Gráfico de Leads por Fonte

- Gráfico de rosca (doughnut) exibindo a distribuição de leads por fonte (Instagram, Google, Facebook, etc.)
- Auxilia na identificação das fontes de tráfego mais eficazes

#### D. Gráfico de Leads por Campanha

- Gráfico de barras horizontais mostrando a eficácia das diferentes campanhas
- Ajuda a determinar quais campanhas estão gerando mais leads

#### E. Tabela de Leads Recentes

- Lista simplificada dos 5 leads mais recentes para referência rápida
- Link para visualização completa na página de leads qualificados

### 2. Sistema de Qualificação de Leads

O sistema de qualificação atribui uma pontuação a cada lead com base em critérios relevantes para o negócio da Consultoria Calazans:

#### A. Critérios de Pontuação

| Critério | Pontos | Explicação |
|----------|--------|------------|
| Menção a dor/lesão/recuperação | +3 | Lead que menciona problemas relevantes no assunto ou mensagem |
| Menção a pós-parto/gravidez/maternidade | +3 | Lead que menciona contexto de maternidade |
| Fonte específica (Instagram, Google, Facebook) | +2 | Plataformas com histórico de conversão para o negócio |
| Campanha relacionada a recuperação | +2 | Campanhas focadas em palavras-chave de recuperação |
| Lead recente (últimos 7 dias) | +1 | Leads recentes tendem a ter maior engajamento |

#### B. Classificação

Com base na pontuação total, os leads são classificados em:
- **Alta Prioridade (6+ pontos)**: Leads com alta probabilidade de conversão
- **Média Prioridade (3-5 pontos)**: Leads com potencial de conversão
- **Baixa Prioridade (0-2 pontos)**: Leads com menor probabilidade de conversão imediata

#### C. Interface de Qualificação

A interface de leads qualificados oferece:
- Código de cores para identificação visual rápida de prioridades
- Filtro de busca em tempo real para localizar leads específicos
- Exibição dos motivos da classificação para cada lead
- Ordenação automática por pontuação (maior para menor)

## Implementação Técnica

### 1. Geração de Dados para o Dashboard

```python
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
    
    # ... outras consultas para gráficos e métricas ...
    
    return {
        'chart_data': chart_data,
        'totals': totals,
        'growth_percentage': round(growth_percentage, 1)
    }
```

### 2. Sistema de Qualificação de Leads

```python
def get_qualified_leads():
    """
    Qualifica leads com base em critérios específicos para o contexto da Consultoria Calazans.
    """
    db = get_db()
    
    # Buscar leads com informações completas
    leads = db.execute('''
        SELECT 
            id, name, email, phone, issue, message,
            source, utm_campaign, created_at,
            strftime('%d/%m/%Y', created_at) as formatted_date
        FROM contacts 
        ORDER BY created_at DESC
    ''').fetchall()
    
    # Palavras-chave para pontuação
    pain_keywords = ['dor', 'lesão', 'lesao', 'lombar', 'coluna', 'hérnia', 'hernia', 'recuperação', ...]
    maternity_keywords = ['gravidez', 'pós-parto', 'pos-parto', 'gestante', 'mãe', 'mae', ...]
    
    # ... lógica de pontuação e classificação ...
    
    # Ordenar por pontuação (maior para menor)
    return sorted(qualified_leads, key=lambda x: x['score'], reverse=True)
```

### 3. Visualização com Chart.js

```javascript
// Configuração para gráfico de barras (Leads por Mês)
const monthlyChart = new Chart(
    document.getElementById('monthlyLeadsChart'),
    {
        type: 'bar',
        data: {
            labels: chartData.monthly_leads.labels,
            datasets: [{
                label: 'Número de Leads',
                data: chartData.monthly_leads.data,
                backgroundColor: chartColors[0],
                borderColor: chartColors[0],
                borderWidth: 1
            }]
        },
        options: {
            // ... opções de configuração ...
        }
    }
);
```

## Escalabilidade e Manutenção

A implementação foi projetada para ser facilmente escalável e adaptável às necessidades futuras:

### 1. Escalabilidade

- **Separação de Responsabilidades**: Modelo-Visão-Controlador (MVC) para facilitar alterações
- **API para Dados**: Endpoint JSON para futura integração com outras ferramentas
- **Estrutura Modular**: Fácil adição de novos gráficos ou critérios de qualificação

### 2. Possíveis Melhorias Futuras

- **Exportação de Dados**: Adicionar funcionalidade para exportar relatórios em PDF ou Excel
- **Filtros Avançados**: Implementar filtros por data, fonte e campanha nos relatórios
- **Ajuste de Critérios**: Interface para administradores ajustarem os critérios de pontuação
- **Automação**: Notificações automáticas para leads de alta prioridade
- **Integração**: Conexão com CRM ou ferramentas de email marketing

## Conclusão

O dashboard de relatórios e o sistema de qualificação de leads oferecem uma solução completa para análise e priorização de leads, adaptada especificamente para o contexto da Consultoria Calazans. A implementação segue boas práticas de desenvolvimento web, com foco em usabilidade, desempenho e manutenibilidade.

Esta solução permite que a administradora:
1. Visualize tendências de aquisição de leads
2. Identifique as fontes e campanhas mais eficazes
3. Priorize o acompanhamento de leads com maior potencial de conversão
4. Tome decisões baseadas em dados para otimizar esforços de marketing

---

## Instruções para Manutenção

### Adicionar Novos Critérios de Qualificação

Para adicionar um novo critério de qualificação, modifique a função `get_qualified_leads()` em `app/models/contacts.py`:

1. Adicione novas palavras-chave ou critérios
2. Atualize a lógica de pontuação
3. Atualize a documentação na página de leads qualificados

### Adicionar Novos Gráficos

Para adicionar um novo gráfico ao dashboard:

1. Adicione a consulta SQL necessária em `get_dashboard_data()`
2. Atualize o template `reports.html` com o novo elemento canvas
3. Adicione a configuração do gráfico no script JavaScript 
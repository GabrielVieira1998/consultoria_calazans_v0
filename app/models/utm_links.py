from app.models.database import get_db
import datetime
import urllib.parse

def get_all_utm_links():
    """Retorna todos os links UTM ordenados por data de criação (mais recentes primeiro)"""
    db = get_db()
    links = db.execute('''
        SELECT * FROM utm_links 
        ORDER BY created_at DESC
    ''').fetchall()
    return links

def get_utm_link_by_id(id):
    """Retorna um link UTM específico pelo ID"""
    db = get_db()
    link = db.execute('SELECT * FROM utm_links WHERE id = ?', (id,)).fetchone()
    return link

def add_utm_link(name, base_url, utm_source, utm_medium, utm_campaign, utm_term=None, utm_content=None, short_description=None):
    """Adiciona um novo link UTM"""
    db = get_db()
    db.execute('''
        INSERT INTO utm_links 
        (name, base_url, utm_source, utm_medium, utm_campaign, utm_term, utm_content, short_description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, base_url, utm_source, utm_medium, utm_campaign, utm_term, utm_content, short_description))
    db.commit()

def update_utm_link(id, name, base_url, utm_source, utm_medium, utm_campaign, utm_term=None, utm_content=None, short_description=None):
    """Atualiza um link UTM existente"""
    db = get_db()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.execute('''
        UPDATE utm_links
        SET name = ?, base_url = ?, utm_source = ?, utm_medium = ?, 
            utm_campaign = ?, utm_term = ?, utm_content = ?, 
            short_description = ?, last_updated = ?
        WHERE id = ?
    ''', (name, base_url, utm_source, utm_medium, utm_campaign, 
          utm_term, utm_content, short_description, now, id))
    db.commit()

def delete_utm_link(id):
    """Exclui um link UTM pelo ID"""
    db = get_db()
    db.execute('DELETE FROM utm_links WHERE id = ?', (id,))
    db.commit()

def generate_utm_url(link):
    """Gera a URL completa com os parâmetros UTM para um objeto link"""
    params = {
        'utm_source': link['utm_source'],
        'utm_medium': link['utm_medium'],
        'utm_campaign': link['utm_campaign']
    }
    
    # Adicionar parâmetros opcionais se existirem
    if link['utm_term']:
        params['utm_term'] = link['utm_term']
    if link['utm_content']:
        params['utm_content'] = link['utm_content']
    
    # Construir a URL com os parâmetros
    base_url = link['base_url']
    # Remove trailing slash if exists to prevent double slashes
    if base_url.endswith('/'):
        base_url = base_url[:-1]
    
    # Verificar se a URL já contém parâmetros
    if '?' in base_url:
        return f"{base_url}&{urllib.parse.urlencode(params)}"
    else:
        return f"{base_url}?{urllib.parse.urlencode(params)}"

def get_recent_utm_links(limit=5):
    """Retorna os links UTM mais recentes, limitados a um número específico"""
    db = get_db()
    links = db.execute('''
        SELECT * FROM utm_links 
        ORDER BY created_at DESC
        LIMIT ?
    ''', (limit,)).fetchall()
    return links 
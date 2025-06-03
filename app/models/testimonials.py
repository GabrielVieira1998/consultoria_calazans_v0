from app.models.database import get_db

def get_all_testimonials():
    conn = get_db()
    testimonials = conn.execute('SELECT * FROM testimonials').fetchall()
    return testimonials

def get_testimonial_by_id(id):
    conn = get_db()
    testimonial = conn.execute('SELECT * FROM testimonials WHERE id = ?', (id,)).fetchone()
    return testimonial

def add_new_testimonial(name, text):
    conn = get_db()
    conn.execute(
        'INSERT INTO testimonials (name, text) VALUES (?, ?)',
        (name, text)
    )
    conn.commit()
    
def update_testimonial(id, name, text):
    conn = get_db()
    conn.execute(
        'UPDATE testimonials SET name = ?, text = ? WHERE id = ?',
        (name, text, id)
    )
    conn.commit()
    
def delete_testimonial(id):
    conn = get_db()
    conn.execute('DELETE FROM testimonials WHERE id = ?', (id,))
    conn.commit() 
from flask import Blueprint, render_template, request, redirect, url_for, flash, g
from app.models.testimonials import get_all_testimonials
from app.models.contacts import save_contact

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    testimonials = get_all_testimonials()
    return render_template('pages/index.html', testimonials=testimonials)

@bp.route('/sobre')
def about():
    return render_template('pages/about.html')

@bp.route('/cursos')
def courses():
    return render_template('pages/courses.html')

@bp.route('/faq')
def faq():
    return render_template('pages/faq.html')

@bp.route('/contato', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        issue = request.form['issue']
        message = request.form['message']
        
        # Captura parâmetros UTM e fonte via POST (campos hidden do JavaScript)
        utm_source = request.form.get('utm_source', '')
        utm_medium = request.form.get('utm_medium', '')
        utm_campaign = request.form.get('utm_campaign', '')
        utm_term = request.form.get('utm_term', '')
        utm_content = request.form.get('utm_content', '')
        source = request.form.get('source', 'direct')
        
        save_contact(name, email, phone, issue, message, 
                     source, utm_source, utm_medium, utm_campaign, 
                     utm_term, utm_content)
        
        flash('Mensagem enviada com sucesso! Entraremos em contato em breve.', 'success')
        return redirect(url_for('main.contact'))
        
    return render_template('pages/contact.html') 
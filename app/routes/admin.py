from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.models.auth import login_required
from app.models.testimonials import get_all_testimonials, get_testimonial_by_id, add_new_testimonial, update_testimonial, delete_testimonial
from app.models.contacts import get_lead_sources, get_lead_details, get_dashboard_data, get_qualified_leads
from app.models.utm_links import get_all_utm_links, get_utm_link_by_id, add_utm_link, update_utm_link, delete_utm_link, generate_utm_url
import json

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

# Rotas para depoimentos
@bp.route('/depoimentos')
@login_required
def testimonials():
    testimonials = get_all_testimonials()
    return render_template('admin/testimonials.html', testimonials=testimonials)

@bp.route('/depoimentos/novo', methods=['GET', 'POST'])
@login_required
def add_testimonial():
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        
        add_new_testimonial(name, text)
        
        flash('Depoimento adicionado com sucesso!', 'success')
        return redirect(url_for('admin.testimonials'))
        
    return render_template('admin/testimonial_form.html')

@bp.route('/depoimentos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_testimonial(id):
    testimonial = get_testimonial_by_id(id)
    
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        
        update_testimonial(id, name, text)
        
        flash('Depoimento atualizado com sucesso!', 'success')
        return redirect(url_for('admin.testimonials'))
        
    return render_template('admin/testimonial_form.html', testimonial=testimonial)

@bp.route('/depoimentos/excluir/<int:id>')
@login_required
def delete_testimonial_route(id):
    delete_testimonial(id)
    
    flash('Depoimento excluído com sucesso!', 'success')
    return redirect(url_for('admin.testimonials'))

# Rotas para relatórios
@bp.route('/reports')
@login_required
def reports():
    sources = get_lead_sources()
    leads = get_lead_details()
    dashboard_data = get_dashboard_data()
    
    # Converter dados de gráficos para JSON para uso no JavaScript
    chart_json = json.dumps(dashboard_data['chart_data'])
    
    return render_template('admin/reports.html', 
                          sources=sources, 
                          leads=leads, 
                          dashboard=dashboard_data,
                          chart_json=chart_json)

@bp.route('/reports/qualified-leads')
@login_required
def qualified_leads():
    qualified = get_qualified_leads()
    return render_template('admin/qualified_leads.html', qualified_leads=qualified)

@bp.route('/api/dashboard-data')
@login_required
def api_dashboard_data():
    """API endpoint para obter dados do dashboard em formato JSON"""
    dashboard_data = get_dashboard_data()
    return jsonify(dashboard_data)

# Rotas para links UTM
@bp.route('/utm-links')
@login_required
def utm_links():
    links = get_all_utm_links()
    return render_template('admin/utm_links.html', links=links)

@bp.route('/utm-links/novo', methods=['GET', 'POST'])
@login_required
def add_utm_link_route():
    if request.method == 'POST':
        name = request.form['name']
        base_url = request.form['base_url']
        utm_source = request.form['utm_source']
        utm_medium = request.form['utm_medium']
        utm_campaign = request.form['utm_campaign']
        utm_term = request.form['utm_term'] if request.form['utm_term'] else None
        utm_content = request.form['utm_content'] if request.form['utm_content'] else None
        short_description = request.form['short_description'] if request.form['short_description'] else None
        
        add_utm_link(name, base_url, utm_source, utm_medium, utm_campaign, 
                    utm_term, utm_content, short_description)
        
        flash('Link UTM adicionado com sucesso!', 'success')
        return redirect(url_for('admin.utm_links'))
        
    return render_template('admin/utm_link_form.html')

@bp.route('/utm-links/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_utm_link_route(id):
    utm_link = get_utm_link_by_id(id)
    
    if request.method == 'POST':
        name = request.form['name']
        base_url = request.form['base_url']
        utm_source = request.form['utm_source']
        utm_medium = request.form['utm_medium']
        utm_campaign = request.form['utm_campaign']
        utm_term = request.form['utm_term'] if request.form['utm_term'] else None
        utm_content = request.form['utm_content'] if request.form['utm_content'] else None
        short_description = request.form['short_description'] if request.form['short_description'] else None
        
        update_utm_link(id, name, base_url, utm_source, utm_medium, utm_campaign, 
                       utm_term, utm_content, short_description)
        
        flash('Link UTM atualizado com sucesso!', 'success')
        return redirect(url_for('admin.utm_links'))
        
    return render_template('admin/utm_link_form.html', utm_link=utm_link)

@bp.route('/utm-links/excluir/<int:id>')
@login_required
def delete_utm_link_route(id):
    delete_utm_link(id)
    
    flash('Link UTM excluído com sucesso!', 'success')
    return redirect(url_for('admin.utm_links'))

@bp.route('/utm-links/visualizar/<int:id>')
@login_required
def view_utm_link_route(id):
    utm_link = get_utm_link_by_id(id)
    if utm_link:
        full_url = generate_utm_url(utm_link)
        return render_template('admin/utm_link_details.html', utm_link=utm_link, full_url=full_url)
    
    flash('Link UTM não encontrado!', 'danger')
    return redirect(url_for('admin.utm_links')) 
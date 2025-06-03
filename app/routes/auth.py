from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.auth import verify_login

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        
        if verify_login(password):
            session['logged_in'] = True
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Senha incorreta!', 'danger')
    
    return render_template('pages/login.html')

@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Você saiu com sucesso!', 'success')
    return redirect(url_for('main.index')) 
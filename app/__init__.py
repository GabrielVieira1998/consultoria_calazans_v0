from flask import Flask, g
import os
import datetime

# Importações dos modelos
from app.models.database import close_connection

def create_app(test_config=None):
    # Inicialização da aplicação
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='consultoria_calazans_secret_key',
        DATABASE=os.path.join(app.instance_path, 'database.db'),
    )

    if test_config is None:
        # Carrega a configuração da instância, se existir
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega a configuração de teste
        app.config.from_mapping(test_config)

    # Garante que o diretório da instância existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Função para adicionar o ano atual no contexto global
    @app.before_request
    def before_request():
        g.current_year = datetime.datetime.now().year
        # Captura parâmetros UTM da URL
        from flask import request
        g.utm_params = {
            'utm_source': request.args.get('utm_source', ''),
            'utm_medium': request.args.get('utm_medium', ''),
            'utm_campaign': request.args.get('utm_campaign', ''),
            'utm_term': request.args.get('utm_term', ''),
            'utm_content': request.args.get('utm_content', '')
        }
        # Determina a fonte do lead
        g.source = request.args.get('source', 'direct')

    # Hook para disponibilizar certas variáveis para todos os templates
    @app.context_processor
    def inject_current_year():
        return dict(current_year=datetime.datetime.now().year)

    # Configuração para fechar conexão com banco de dados
    @app.teardown_appcontext
    def close_db_connection(exception):
        close_connection(exception)

    # Registrar blueprints
    from app.routes import main, admin, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(auth.bp)

    # Registrar comandos CLI
    from app import cli
    cli.init_app(app)

    # Tratamento de erro 404
    @app.errorhandler(404)
    def page_not_found(e):
        from flask import render_template
        return render_template('pages/404.html'), 404

    return app 
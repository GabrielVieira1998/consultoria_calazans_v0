# Guia de Desenvolvimento - Consultoria Calazans

Este documento serve como um guia abrangente para desenvolvedores trabalhando no projeto da Consultoria Calazans. Aqui você encontrará instruções sobre como adicionar novas funcionalidades, rotas, tabelas no banco de dados, autenticação e outras tarefas comuns.

## Sumário

1. [Estrutura do Projeto](#estrutura-do-projeto)
2. [Adicionando Novas Rotas](#adicionando-novas-rotas)
3. [Criando Novas Tabelas no Banco de Dados](#criando-novas-tabelas-no-banco-de-dados)
4. [Trabalhando com Modelos](#trabalhando-com-modelos)
5. [Sistema de Autenticação](#sistema-de-autenticação)
6. [Criando Páginas CRUD](#criando-páginas-crud)
7. [Lidando com Formulários](#lidando-com-formulários)
8. [Dicas para a Prova](#dicas-para-a-prova)

## Estrutura do Projeto

O projeto segue uma arquitetura baseada em Flask com uma estrutura modularizada:

```
.
├── app/                         # Código principal da aplicação
│   ├── __init__.py              # Inicialização da aplicação Flask
│   ├── cli.py                   # Comandos CLI
│   ├── schema.sql               # Esquema do banco de dados
│   ├── models/                  # Lógica de negócios e acesso a dados
│   │   ├── __init__.py
│   │   ├── auth.py              # Autenticação
│   │   ├── contacts.py          # Operações com contatos
│   │   ├── database.py          # Conexão com banco de dados
│   │   ├── testimonials.py      # Operações com depoimentos
│   │   └── utm_links.py         # Operações com links UTM
│   ├── routes/                  # Endpoints da aplicação
│   │   ├── __init__.py
│   │   ├── admin.py             # Rotas administrativas
│   │   ├── auth.py              # Rotas de autenticação
│   │   └── main.py              # Rotas principais
│   ├── static/                  # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/               # Templates HTML (Jinja2)
│   └── utils/                   # Utilitários
├── instance/                    # Dados específicos da instância (BD)
├── docs/                        # Documentação
├── tutorial/                    # Tutoriais (este documento)
├── venv/                        # Ambiente virtual Python
├── .flaskenv                    # Variáveis de ambiente Flask
├── init_db.py                   # Script de inicialização do BD
├── requirements.txt             # Dependências do projeto
├── setup.bat/setup.sh           # Scripts de configuração
└── wsgi.py                      # Ponto de entrada da aplicação
```

## Adicionando Novas Rotas

### 1. Adicionar uma Rota em Arquivo Existente

Para adicionar uma nova rota a um arquivo de rotas existente (por exemplo, `app/routes/main.py`):

```python
@bp.route('/minha-nova-pagina')
def minha_nova_pagina():
    # Lógica da rota aqui
    return render_template('pages/minha_nova_pagina.html')
```

### 2. Criar um Novo Arquivo de Rotas

Para adicionar um conjunto completamente novo de rotas:

1. Crie um novo arquivo Python em `app/routes/`, por exemplo `meu_modulo.py`:

```python
from flask import Blueprint, render_template, request, redirect, url_for, flash, g
# Importe modelos necessários
from app.models.meu_modelo import get_data

bp = Blueprint('meu_modulo', __name__, url_prefix='/meu-modulo')

@bp.route('/')
def index():
    data = get_data()
    return render_template('meu_modulo/index.html', data=data)

@bp.route('/detalhe/<int:id>')
def detalhe(id):
    # Lógica para exibir detalhes
    return render_template('meu_modulo/detalhe.html', id=id)
```

2. Registre o blueprint no arquivo `app/__init__.py`:

```python
# Adicione ao bloco "Registrar blueprints"
from app.routes import main, admin, auth, meu_modulo
app.register_blueprint(main.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(meu_modulo.bp)
```

3. Crie os templates correspondentes em `app/templates/meu_modulo/`.

## Criando Novas Tabelas no Banco de Dados

### 1. Modificar o Schema

Para adicionar uma nova tabela ao banco de dados, edite o arquivo `app/schema.sql`:

```sql
-- Adicione após as tabelas existentes
CREATE TABLE meu_novo_modelo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_id INTEGER,
    ativo BOOLEAN DEFAULT 1
);

-- Dados iniciais (opcional)
INSERT INTO meu_novo_modelo (titulo, descricao)
VALUES 
    ('Primeiro item', 'Descrição do primeiro item'),
    ('Segundo item', 'Descrição do segundo item');
```

### 2. Recriar o Banco de Dados

Após modificar o schema, execute o script de inicialização para recriar o banco de dados:

```bash
python init_db.py
```

Alternativamente, se a aplicação estiver em execução:

```python
from app.models.database import init_db
init_db()
```

### 3. Atualizar Banco Existente (Alternativa)

Se você não quiser recriar todo o banco de dados e perder dados existentes, pode executar apenas os comandos SQL necessários:

```python
from app.models.database import get_db

def update_schema():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS meu_novo_modelo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            usuario_id INTEGER,
            ativo BOOLEAN DEFAULT 1
        )
    ''')
    db.commit()
```

## Trabalhando com Modelos

### 1. Criar um Novo Arquivo de Modelo

Para adicionar um novo modelo, crie um arquivo em `app/models/`, por exemplo `meu_modelo.py`:

```python
from app.models.database import get_db

def get_all_items():
    """Recupera todos os itens da tabela meu_novo_modelo"""
    db = get_db()
    items = db.execute('''
        SELECT id, titulo, descricao, data_criacao
        FROM meu_novo_modelo
        WHERE ativo = 1
        ORDER BY data_criacao DESC
    ''').fetchall()
    return items

def get_item_by_id(id):
    """Recupera um item específico pelo ID"""
    db = get_db()
    item = db.execute('''
        SELECT id, titulo, descricao, data_criacao
        FROM meu_novo_modelo
        WHERE id = ?
    ''', (id,)).fetchone()
    return item

def create_item(titulo, descricao, usuario_id=None):
    """Cria um novo item"""
    db = get_db()
    db.execute('''
        INSERT INTO meu_novo_modelo (titulo, descricao, usuario_id)
        VALUES (?, ?, ?)
    ''', (titulo, descricao, usuario_id))
    db.commit()
    
def update_item(id, titulo, descricao):
    """Atualiza um item existente"""
    db = get_db()
    db.execute('''
        UPDATE meu_novo_modelo
        SET titulo = ?, descricao = ?
        WHERE id = ?
    ''', (titulo, descricao, id))
    db.commit()

def delete_item(id):
    """Exclui um item (ou marca como inativo)"""
    db = get_db()
    # Exclusão lógica (mantém o registro, mas marca como inativo)
    db.execute('''
        UPDATE meu_novo_modelo
        SET ativo = 0
        WHERE id = ?
    ''', (id,))
    db.commit()
    
    # Alternativa: Exclusão física
    # db.execute('DELETE FROM meu_novo_modelo WHERE id = ?', (id,))
    # db.commit()
```

### 2. Usar o Modelo nas Rotas

```python
from app.models.meu_modelo import get_all_items, get_item_by_id, create_item, update_item, delete_item

@bp.route('/')
def index():
    items = get_all_items()
    return render_template('meu_modulo/index.html', items=items)

@bp.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        create_item(titulo, descricao)
        flash('Item criado com sucesso!', 'success')
        return redirect(url_for('meu_modulo.index'))
    return render_template('meu_modulo/form.html')
```

## Sistema de Autenticação

O projeto utiliza um sistema de autenticação simples baseado em senha. Veja como expandir esse sistema:

### 1. Adicionar Usuários ao Sistema

Modifique o arquivo `app/schema.sql` para incluir uma tabela de usuários:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL DEFAULT 'user',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Usuário admin padrão (senha: admin123)
INSERT INTO users (username, password, name, email, role)
VALUES ('admin', 'admin123', 'Administrador', 'admin@exemplo.com', 'admin');
```

### 2. Atualizar o Modelo de Autenticação

Modifique o arquivo `app/models/auth.py`:

```python
from app.models.database import get_db
from functools import wraps
from flask import session, redirect, url_for, flash, g

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, faça login para acessar esta página.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, faça login para acessar esta página.', 'warning')
            return redirect(url_for('auth.login'))
        if session.get('user_role') != 'admin':
            flash('Acesso restrito a administradores.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

def verify_login(username, password):
    db = get_db()
    user = db.execute(
        'SELECT * FROM users WHERE username = ?', (username,)
    ).fetchone()
    
    if user is None:
        return None
    
    if user['password'] == password:  # Em produção, use hash de senha!
        return user
    
    return None

def get_current_user():
    if 'user_id' in session:
        db = get_db()
        user = db.execute(
            'SELECT id, username, name, email, role FROM users WHERE id = ?',
            (session['user_id'],)
        ).fetchone()
        return user
    return None
```

### 3. Atualizar as Rotas de Autenticação

Modifique o arquivo `app/routes/auth.py`:

```python
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
from app.models.auth import verify_login, get_current_user

bp = Blueprint('auth', __name__)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_current_user()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = verify_login(username, password)
        if user:
            session.clear()
            session['user_id'] = user['id']
            session['user_role'] = user['role']
            session['logged_in'] = True
            flash(f'Bem-vindo, {user["name"]}!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Usuário ou senha incorretos!', 'danger')
    
    return render_template('pages/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash('Você saiu com sucesso!', 'success')
    return redirect(url_for('main.index'))
```

## Criando Páginas CRUD

Para implementar um CRUD (Create, Read, Update, Delete) completo para uma entidade, siga estes passos:

### 1. Definir o Modelo

Crie o arquivo `app/models/produtos.py` (exemplo):

```python
from app.models.database import get_db
from datetime import datetime

def get_all_products():
    db = get_db()
    products = db.execute('''
        SELECT id, nome, descricao, preco, estoque, created_at
        FROM produtos
        ORDER BY created_at DESC
    ''').fetchall()
    return products

def get_product(id):
    db = get_db()
    product = db.execute('''
        SELECT id, nome, descricao, preco, estoque, created_at
        FROM produtos
        WHERE id = ?
    ''', (id,)).fetchone()
    return product

def create_product(nome, descricao, preco, estoque):
    db = get_db()
    db.execute('''
        INSERT INTO produtos (nome, descricao, preco, estoque)
        VALUES (?, ?, ?, ?)
    ''', (nome, descricao, preco, estoque))
    db.commit()

def update_product(id, nome, descricao, preco, estoque):
    db = get_db()
    db.execute('''
        UPDATE produtos
        SET nome = ?, descricao = ?, preco = ?, estoque = ?
        WHERE id = ?
    ''', (nome, descricao, preco, estoque, id))
    db.commit()

def delete_product(id):
    db = get_db()
    db.execute('DELETE FROM produtos WHERE id = ?', (id,))
    db.commit()
```

### 2. Definir as Rotas CRUD

Crie o arquivo `app/routes/produtos.py`:

```python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.produtos import get_all_products, get_product, create_product, update_product, delete_product
from app.models.auth import login_required, admin_required

bp = Blueprint('produtos', __name__, url_prefix='/produtos')

@bp.route('/')
def index():
    products = get_all_products()
    return render_template('produtos/index.html', products=products)

@bp.route('/<int:id>')
def view(id):
    product = get_product(id)
    if product is None:
        flash('Produto não encontrado!', 'danger')
        return redirect(url_for('produtos.index'))
    return render_template('produtos/view.html', product=product)

@bp.route('/create', methods=['GET', 'POST'])
@admin_required
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = float(request.form['preco'])
        estoque = int(request.form['estoque'])
        
        # Validação simples
        if not nome:
            flash('Nome é obrigatório!', 'danger')
        else:
            create_product(nome, descricao, preco, estoque)
            flash('Produto criado com sucesso!', 'success')
            return redirect(url_for('produtos.index'))
            
    return render_template('produtos/form.html')

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@admin_required
def edit(id):
    product = get_product(id)
    if product is None:
        flash('Produto não encontrado!', 'danger')
        return redirect(url_for('produtos.index'))
        
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = float(request.form['preco'])
        estoque = int(request.form['estoque'])
        
        # Validação simples
        if not nome:
            flash('Nome é obrigatório!', 'danger')
        else:
            update_product(id, nome, descricao, preco, estoque)
            flash('Produto atualizado com sucesso!', 'success')
            return redirect(url_for('produtos.view', id=id))
            
    return render_template('produtos/form.html', product=product)

@bp.route('/<int:id>/delete', methods=['POST'])
@admin_required
def delete(id):
    product = get_product(id)
    if product is None:
        flash('Produto não encontrado!', 'danger')
    else:
        delete_product(id)
        flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('produtos.index'))
```

### 3. Criar os Templates

Crie os seguintes templates:

1. `app/templates/produtos/index.html` - Lista de produtos
2. `app/templates/produtos/view.html` - Detalhes do produto
3. `app/templates/produtos/form.html` - Formulário para criar/editar produto

#### Exemplo de template de formulário:

```html
{% extends "layout.html" %}

{% block title %}{{ 'Editar' if product else 'Criar' }} Produto{% endblock %}

{% block content %}
<div class="container py-4">
    <h1>{{ 'Editar' if product else 'Criar' }} Produto</h1>
    
    <form method="post">
        <div class="mb-3">
            <label for="nome" class="form-label">Nome</label>
            <input type="text" class="form-control" id="nome" name="nome" value="{{ product.nome if product else '' }}" required>
        </div>
        
        <div class="mb-3">
            <label for="descricao" class="form-label">Descrição</label>
            <textarea class="form-control" id="descricao" name="descricao" rows="3">{{ product.descricao if product else '' }}</textarea>
        </div>
        
        <div class="mb-3">
            <label for="preco" class="form-label">Preço</label>
            <input type="number" step="0.01" class="form-control" id="preco" name="preco" value="{{ product.preco if product else '' }}" required>
        </div>
        
        <div class="mb-3">
            <label for="estoque" class="form-label">Estoque</label>
            <input type="number" class="form-control" id="estoque" name="estoque" value="{{ product.estoque if product else 0 }}" required>
        </div>
        
        <div class="d-flex justify-content-between">
            <a href="{{ url_for('produtos.index') }}" class="btn btn-secondary">Cancelar</a>
            <button type="submit" class="btn btn-primary">Salvar</button>
        </div>
    </form>
</div>
{% endblock %}
```

### 4. Registrar o Blueprint

No arquivo `app/__init__.py`, adicione:

```python
from app.routes import main, admin, auth, produtos
app.register_blueprint(main.bp)
app.register_blueprint(admin.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(produtos.bp)
```

## Lidando com Formulários

### 1. Validação de Formulários

Para validação mais robusta, você pode usar bibliotecas como Flask-WTF ou implementar uma validação manual:

```python
def validate_product_form(form):
    errors = {}
    
    # Validar nome
    if not form.get('nome'):
        errors['nome'] = 'O nome é obrigatório'
    elif len(form.get('nome')) < 3:
        errors['nome'] = 'O nome deve ter pelo menos 3 caracteres'
    
    # Validar preço
    try:
        preco = float(form.get('preco', 0))
        if preco < 0:
            errors['preco'] = 'O preço não pode ser negativo'
    except ValueError:
        errors['preco'] = 'Preço inválido'
    
    # Validar estoque
    try:
        estoque = int(form.get('estoque', 0))
        if estoque < 0:
            errors['estoque'] = 'O estoque não pode ser negativo'
    except ValueError:
        errors['estoque'] = 'Estoque inválido'
    
    return errors
```

### 2. Upload de Arquivos

Para permitir upload de imagens ou outros arquivos:

```python
import os
from werkzeug.utils import secure_filename

# Configuração
UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/create', methods=['GET', 'POST'])
@admin_required
def create():
    if request.method == 'POST':
        # ... outros campos do formulário ...
        
        # Processar upload de imagem
        if 'imagem' in request.files:
            file = request.files['imagem']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Gerar nome único baseado no timestamp
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                filename = f"{timestamp}_{filename}"
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                
                # Salvar caminho da imagem no banco
                imagem_path = f"uploads/{filename}"
            else:
                imagem_path = None
                
        # Continuar com o processamento normal...
```

## Dicas para a Prova

### 1. Entendendo o Fluxo de Dados

Esteja preparado para explicar como os dados fluem do front-end ao banco de dados:

1. **Formulário HTML** → Envia dados via método POST
2. **Rota Flask** → Recebe e processa os dados
3. **Modelo** → Executa operações de banco de dados (SQL)
4. **Banco de Dados** → Armazena ou recupera informações
5. **Resposta** → Retorna ao usuário (redirect ou render_template)

### 2. Perguntas Comuns

- **Como adicionar uma nova tabela?** Modificar schema.sql e executar init_db.py
- **Como proteger rotas admin?** Usar o decorador login_required ou admin_required
- **Como implementar uma busca?** Usar parâmetros de URL e consultas SQL com LIKE
- **Como relacionar tabelas?** Usar chaves estrangeiras e JOINs nas consultas SQL

### 3. Explicando as Consultas SQL

Esteja preparado para explicar as consultas SQL que você escreveu:

```python
# Exemplo de JOIN entre tabelas
def get_produtos_por_categoria():
    db = get_db()
    produtos = db.execute('''
        SELECT p.id, p.nome, p.preco, c.nome as categoria
        FROM produtos p
        JOIN categorias c ON p.categoria_id = c.id
        ORDER BY c.nome, p.nome
    ''').fetchall()
    return produtos
```

### 4. Personalizando o Projeto

Para diferenciar seu projeto:

- Adicione validações de formulário mais robustas
- Implemente paginação para listas longas
- Adicione recursos de busca e filtro
- Melhore a interface do usuário com mais interatividade
- Implemente relatórios e estatísticas

## Conclusão

Este guia abrange os aspectos fundamentais para desenvolvimento no projeto da Consultoria Calazans. Lembre-se de seguir as convenções estabelecidas, manter o código organizado e documentado, e testar regularmente suas modificações.

Para qualquer dúvida ou sugestão, consulte a documentação do Flask ou entre em contato com a equipe de desenvolvimento.

Boa sorte na sua prova! 
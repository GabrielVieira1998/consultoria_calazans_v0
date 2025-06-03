# Projeto Consultoria Calazans

Plataforma web para consultoria educacional.

## Estrutura do Projeto

```
├── app/                    # Código principal da aplicação
│   ├── __init__.py        # Inicialização da aplicação
│   ├── models/            # Modelos do banco de dados
│   ├── routes/            # Rotas da aplicação
│   │   ├── __init__.py
│   │   ├── main.py       # Rotas públicas
│   │   ├── admin.py      # Rotas administrativas
│   │   └── auth.py       # Rotas de autenticação
│   ├── static/            # Arquivos estáticos
│   │   ├── css/
│   │   ├── js/
│   │   └── qrcodes/      # QR codes gerados
│   ├── templates/         # Templates HTML
│   │   ├── admin/        # Templates da área administrativa
│   │   ├── pages/        # Templates das páginas públicas
│   │   └── layout.html   # Template base
│   └── utils/            # Funções utilitárias
├── docs/                  # Documentação adicional
├── instance/             # Arquivos específicos da instância
│   └── database.db       # Banco de dados SQLite
└── wsgi.py               # Ponto de entrada da aplicação
```

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Inicialize o banco de dados: `flask init-db`

## Executando a Aplicação

```bash
# Modo de desenvolvimento
python wsgi.py

# Alternativa usando Flask CLI
flask run --host=0.0.0.0 --port=5000 --debug
```

## Acessando a Aplicação

- **Área Pública**: http://localhost:5000/
- **Área Administrativa**: http://localhost:5000/admin (senha: admin123)

## 🚀 Funcionalidades

- **Páginas Principais**
  - Página inicial com apresentação da consultoria
  - Seção de cursos disponíveis
  - Depoimentos de clientes
  - FAQ
  - Formulário de contato

- **Área Administrativa**
  - Gerenciamento de cursos
  - Gerenciamento de depoimentos
  - Visualização de relatórios de leads
  - Análise de origem de tráfego

- **Rastreamento de Leads**
  - Parâmetros UTM para campanhas
  - Identificação de fontes de tráfego
  - Relatórios detalhados
  - Análise de conversão

## 🛠️ Tecnologias Utilizadas

- Python 3.8+
- Flask
- SQLite
- Bootstrap 5
- HTML5/CSS3
- JavaScript

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/consultoria-calazans.git
cd consultoria-calazans
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Inicialize o banco de dados:
```bash
flask init-db
```

6. Execute a aplicação:
```bash
flask run
```

## 📊 Rastreamento de Leads

O sistema inclui um robusto sistema de rastreamento de leads que permite identificar a origem de cada contato.

### Parâmetros UTM
Adicione parâmetros UTM nas URLs para rastrear campanhas específicas:
```
https://seusite.com/?utm_source=instagram&utm_medium=social&utm_campaign=promocao_maio
```

Parâmetros disponíveis:
- `utm_source`: Origem do tráfego (ex: instagram, google, facebook)
- `utm_medium`: Tipo de mídia (ex: social, cpc, email)
- `utm_campaign`: Nome da campanha
- `utm_term`: Termo de busca (para campanhas de busca)
- `utm_content`: Identificador do conteúdo específico

### Parâmetro Source
Use o parâmetro source para identificar a origem geral do lead:
```
https://seusite.com/?source=blog
```

### Relatórios
Acesse os relatórios em `/admin/reports` para visualizar:
- Total de leads por fonte
- Leads dos últimos 30 dias
- Detalhes completos de cada lead com sua origem

## 🔐 Acesso Administrativo

- URL: `/admin`
- Senha padrão: `admin123`

## 📁 Estrutura do Projeto

```
projeto_calazans_python/
├── app.py              # Aplicação principal
├── schema.sql          # Esquema do banco de dados
├── requirements.txt    # Dependências do projeto
├── static/            # Arquivos estáticos (CSS, JS, imagens)
├── templates/         # Templates HTML
└── database.db        # Banco de dados SQLite
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Agradecimentos

- Equipe de desenvolvimento
- Consultoria Calazans
- Todos os contribuidores

---

Para suporte adicional ou dúvidas, entre em contato com a equipe de desenvolvimento. 
- [Nome do seu colega de equipe] 
# Documentação do Projeto Consultoria Calazans

## Índice
1. [Visão Geral](#visão-geral)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Banco de Dados](#banco-de-dados)
5. [Funcionalidades](#funcionalidades)
6. [Rastreamento de Leads](#rastreamento-de-leads)
7. [Área Administrativa](#área-administrativa)
8. [Personalização](#personalização)

## Visão Geral
Este é um sistema web desenvolvido para a Consultoria Calazans, especializada em recuperação física para mulheres. O sistema permite gerenciar cursos, depoimentos e contatos de clientes.

## Estrutura do Projeto
```
projeto_calazans_python/
├── app.py              # Aplicação principal
├── schema.sql          # Esquema do banco de dados
├── requirements.txt    # Dependências do projeto
├── static/            # Arquivos estáticos (CSS, JS, imagens)
├── templates/         # Templates HTML
└── database.db        # Banco de dados SQLite
```

## Configuração do Ambiente
1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Inicialize o banco de dados: `flask init-db`
6. Execute a aplicação: `flask run`

## Banco de Dados
O sistema utiliza SQLite como banco de dados. As principais tabelas são:

### Courses
- Armazena informações sobre os cursos oferecidos
- Campos: id, title, description, image, link, created_at

### Testimonials
- Armazena depoimentos de clientes
- Campos: id, name, text, created_at

### Contacts
- Armazena informações de contato dos leads
- Campos: id, name, email, phone, issue, message, source, utm_source, utm_medium, utm_campaign, utm_term, utm_content, created_at

## Funcionalidades
- Página inicial com apresentação da consultoria
- Seção de cursos disponíveis
- Depoimentos de clientes
- Formulário de contato
- Área administrativa protegida por senha
- Sistema de rastreamento de leads

## Rastreamento de Leads
O sistema inclui um robusto sistema de rastreamento de leads que permite identificar a origem de cada contato. Para usar o rastreamento:

### Parâmetros UTM
Adicione parâmetros UTM nas URLs para rastrear campanhas específicas:
```
https://seusite.com/?utm_source=instagram&utm_medium=social&utm_campaign=promocao_maio
```

Parâmetros disponíveis:
- utm_source: Origem do tráfego (ex: instagram, google, facebook)
- utm_medium: Tipo de mídia (ex: social, cpc, email)
- utm_campaign: Nome da campanha
- utm_term: Termo de busca (para campanhas de busca)
- utm_content: Identificador do conteúdo específico

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

## Área Administrativa
Acesse a área administrativa em `/admin` com a senha padrão: `admin123`

Funcionalidades administrativas:
- Gerenciamento de cursos
- Gerenciamento de depoimentos
- Visualização de relatórios de leads
- Análise de origem de tráfego

## Personalização
### Templates
Os templates estão localizados em `templates/`:
- `layout.html`: Template base
- `pages/`: Páginas principais
- `admin/`: Páginas administrativas

### Estilos
Os arquivos CSS estão em `static/css/`:
- `main.css`: Estilos principais
- Personalize as cores e fontes conforme necessário

### Imagens
Substitua as imagens em `static/images/` por suas próprias imagens, mantendo os mesmos nomes de arquivo.

---

Para suporte adicional ou dúvidas, entre em contato com a equipe de desenvolvimento. 
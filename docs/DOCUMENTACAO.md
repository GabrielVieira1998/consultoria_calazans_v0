# Documentação do Projeto Consultoria Calazans

## Índice
1. [Visão Geral](#visão-geral)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Banco de Dados](#banco-de-dados)
5. [Funcionalidades](#funcionalidades)
6. [Rastreamento de Leads](#rastreamento-de-leads)
7. [Qualificação de Leads](#qualificação-de-leads)
8. [Área Administrativa](#área-administrativa)
9. [Identidade Visual](#identidade-visual)
10. [Personalização](#personalização)
11. [Tutoriais e Recursos](#tutoriais-e-recursos)

## Visão Geral
Este é um sistema web desenvolvido para a Consultoria Calazans, especializada em treinos online personalizados para mulheres. A plataforma permite gerenciar leads, contatos, depoimentos e realizar análises de marketing, proporcionando um fluxo otimizado de captura e qualificação de leads.

## Estrutura do Projeto
```
consultoria_calazans/
├── app/                          # Código principal da aplicação
│   ├── __init__.py               # Inicialização da aplicação Flask
│   ├── cli.py                    # Comandos CLI
│   ├── schema.sql                # Esquema do banco de dados
│   ├── models/                   # Lógica de negócios e acesso a dados
│   │   ├── auth.py               # Autenticação
│   │   ├── contacts.py           # Operações com contatos
│   │   ├── database.py           # Conexão com banco de dados
│   │   ├── testimonials.py       # Operações com depoimentos
│   │   └── utm_links.py          # Operações com links UTM
│   ├── routes/                   # Endpoints da aplicação
│   │   ├── admin.py              # Rotas administrativas
│   │   ├── auth.py               # Rotas de autenticação
│   │   └── main.py               # Rotas principais
│   ├── static/                   # Arquivos estáticos (CSS, JS, imagens)
│   └── templates/                # Templates HTML (Jinja2)
├── instance/                     # Dados específicos da instância (BD)
├── docs/                         # Documentação
├── tutorial/                     # Tutoriais
├── init_db.py                    # Script de inicialização do BD
├── requirements.txt              # Dependências do projeto
├── setup.bat/setup.sh            # Scripts de configuração
└── wsgi.py                       # Ponto de entrada da aplicação
```

## Configuração do Ambiente
1. Clone o repositório
2. Execute o script de configuração:
   - Windows: `setup.bat`
   - Linux/Mac: `setup.sh`
3. Alternativamente, configure manualmente:
   - Crie um ambiente virtual: `python -m venv venv`
   - Ative o ambiente virtual:
     - Windows: `venv\Scripts\activate`
     - Linux/Mac: `source venv/bin/activate`
   - Instale as dependências: `pip install -r requirements.txt`
   - Inicialize o banco de dados: `python init_db.py`
4. Execute a aplicação: `flask run` ou `python wsgi.py`

## Banco de Dados
O sistema utiliza SQLite como banco de dados. As principais tabelas são:

### Testimonials
- Armazena depoimentos de clientes
- Campos: id, name, text, created_at

### Contacts
- Armazena informações de contato dos leads
- Campos: id, name, email, phone, issue, message, source, utm_source, utm_medium, utm_campaign, utm_term, utm_content, created_at
- O campo "issue" armazena a principal necessidade do cliente (Dores Posturais, Recuperação Pós-parto, Recuperação de Lesão, Objetivos Estéticos, Diástase, Outro)

### UTM Links
- Armazena links de campanha com parâmetros UTM
- Campos: id, name, base_url, utm_source, utm_medium, utm_campaign, utm_term, utm_content, short_description, created_at, last_updated

## Funcionalidades
- Página inicial com apresentação da consultoria e depoimentos
- Página "Sobre" com detalhes da consultoria
- FAQ com perguntas frequentes
- Formulário de contato com captura de principais necessidades
- Sistema de rastreamento de origem de leads com parâmetros UTM
- Sistema de qualificação e pontuação de leads
- Relatórios detalhados de marketing e conversão
- Área administrativa protegida por senha

## Rastreamento de Leads
O sistema inclui um robusto sistema de rastreamento de leads que permite identificar a origem de cada contato:

### Parâmetros UTM
Adicione parâmetros UTM nas URLs para rastrear campanhas específicas:
```
https://consultoriacalazans.com/?utm_source=instagram&utm_medium=social&utm_campaign=promocao_maio
```

Parâmetros disponíveis:
- utm_source: Origem do tráfego (ex: instagram, google, facebook)
- utm_medium: Tipo de mídia (ex: social, cpc, email)
- utm_campaign: Nome da campanha
- utm_term: Termo de busca (para campanhas de busca)
- utm_content: Identificador do conteúdo específico

### Gerador de Links UTM
A área administrativa oferece um gerador de links UTM para facilitar a criação de campanhas rastreáveis.

## Qualificação de Leads
O sistema implementa um algoritmo de pontuação para qualificar leads automaticamente:

### Critérios de Pontuação
- Menção a dor/lesão/recuperação no assunto ou mensagem: +3 pontos
- Menção a pós-parto/gravidez/maternidade: +3 pontos
- Fonte específica (Instagram, Google): +2 pontos
- Campanha específica relacionada a recuperação: +2 pontos
- Leads recentes (últimos 7 dias): +1 ponto

### Visualização de Leads Qualificados
Os leads são apresentados com sua pontuação e classificação em:
- Hot (7-10 pontos): Alta prioridade
- Warm (4-6 pontos): Média prioridade
- Cold (0-3 pontos): Baixa prioridade

## Área Administrativa
Acesse a área administrativa em `/admin` com a senha padrão: `admin123`

Funcionalidades administrativas:
- Dashboard com métricas de leads
- Relatórios detalhados com gráficos
- Análise de origem de tráfego
- Lista de leads qualificados por prioridade
- Gerador e gerenciador de links UTM
- Gerenciamento de depoimentos

## Identidade Visual
O sistema implementa a nova identidade visual da Consultoria Calazans com a seguinte paleta de cores:

- `#f6f2ed`: Cor de fundo clara (off-white)
- `#f04c2f`: Laranja vibrante (usado no texto "CALAZANS CONSULTORIA")
- `#d62c35`: Vermelho escuro (usado no corpo da personagem)
- `#fa7a39`: Laranja médio (usado nas folhas e detalhes)
- `#b61c3a`: Vinho profundo (pesos da barra)
- `#fba66e`: Laranja claro (realces e elementos secundários)

## Personalização
### Templates
Os templates estão localizados em `app/templates/`:
- `layout.html`: Template base
- `pages/`: Páginas principais
- `admin/`: Páginas administrativas

### Estilos
Os arquivos CSS estão em `app/static/css/`:
- `main.css`: Estilos principais com variáveis CSS para fácil personalização
- As cores e estilos seguem a nova identidade visual

### Imagens
As imagens principais estão em `app/static/images/`, incluindo:
- `logo_final.png`: O novo logo da consultoria

## Tutoriais e Recursos
O sistema inclui uma série de tutoriais detalhados na pasta `tutorial/`:

1. **Guia do Painel Administrativo**: Uso das funcionalidades administrativas
2. **Guia de Links UTM**: Como utilizar links UTM para rastreamento de campanhas
3. **Sistema de Pontuação de Leads**: Como funciona a qualificação de leads
4. **Processo Otimizado de Atendimento**: Framework para gestão de atendimento
5. **Guia de Desenvolvimento**: Documentação técnica para desenvolvedores

---

Para suporte adicional ou dúvidas, entre em contato com a equipe de desenvolvimento. 
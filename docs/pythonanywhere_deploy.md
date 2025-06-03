# Deploy Simplificado no PythonAnywhere

Este guia contém apenas os passos essenciais para configurar o projeto Consultoria Calazans no PythonAnywhere.

## 1. Criação da Conta

1. Acesse [PythonAnywhere](https://www.pythonanywhere.com) e crie uma conta gratuita
2. Faça login e acesse o Dashboard

## 2. Configuração do Projeto

### Fazer Upload do Projeto

Opção 1: Via GitHub (para repositórios públicos)
1. No dashboard do PythonAnywhere, abra um console Bash
2. Clone o repositório:
   ```bash
   git clone https://github.com/GabrielVieira1998/consultoria_calazans_producao.git
   ```

Opção 2: Upload manual (recomendado para repositórios privados)
1. Comprima o projeto em um arquivo ZIP localmente
2. No dashboard do PythonAnywhere, faça upload do arquivo ZIP
3. No console Bash, descompacte o arquivo:
   ```bash
   unzip nome_do_arquivo.zip -d consultoria_calazans_producao
   ```

### Configurar Ambiente Virtual

1. No console Bash, navegue até a pasta do projeto:
   ```bash
   cd ~/consultoria_calazans_producao
   ```
2. Crie um ambiente virtual:
   ```bash
   mkvirtualenv --python=python3.9 calazans-venv
   ```
   (Nota: Isso ativará automaticamente o ambiente virtual)
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 3. Configurar a Aplicação Web

1. No dashboard do PythonAnywhere, vá para a seção "Web"
2. Clique em "Add a new web app"
3. Escolha um domínio (será algo como `seuusername.pythonanywhere.com`)
4. Selecione "Manual configuration" (não "Flask")
5. Selecione a versão Python 3.9

### Configurar o WSGI

1. Na página de configuração da aplicação web, localize o link para o arquivo WSGI
2. Clique no link para editar o arquivo
3. Substitua **todo** o conteúdo pelo seguinte (ajuste o caminho substituindo 'seuusername' pelo seu nome de usuário real):

```python
import sys
import os

# Adicionar o diretório do projeto ao path
path = '/home/seuusername/consultoria_calazans_producao'
if path not in sys.path:
    sys.path.append(path)

# Definir variáveis de ambiente
os.environ['FLASK_APP'] = 'wsgi.py'
os.environ['FLASK_ENV'] = 'production'

# Importar a aplicação
from wsgi import app as application
```

### Configurar o Virtualenv

1. Na página de configuração da aplicação web, na seção "Virtualenv"
2. Informe o caminho para o seu virtualenv: `/home/seuusername/.virtualenvs/calazans-venv`
   (substitua 'seuusername' pelo seu nome de usuário real)

### Configurar Diretórios Estáticos

1. Na seção "Static files", adicione:
   - URL: `/static/`
   - Directory: `/home/seuusername/consultoria_calazans_producao/app/static/`
   (substitua 'seuusername' pelo seu nome de usuário real)

## 4. Inicializar o Banco de Dados

1. Abra um console Bash (ou use o que já está aberto)
2. Se o ambiente virtual não estiver ativado, ative-o:
   ```bash
   workon calazans-venv
   ```
   (Você saberá que está ativado quando ver `(calazans-venv)` no início da linha de comando)
3. Navegue até a pasta do projeto (se ainda não estiver nela):
   ```bash
   cd ~/consultoria_calazans_producao
   ```
4. Crie um arquivo temporário para inicializar o banco de dados:
   ```bash
   echo '
   from app import create_app
   app = create_app()
   from app.models.database import init_db
   with app.app_context():
       init_db()
   ' > init_db_script.py
   ```
5. Execute o script:
   ```bash
   python init_db_script.py
   ```
6. Após a execução bem-sucedida, você pode remover o script temporário:
   ```bash
   rm init_db_script.py
   ```

## 5. Reiniciar a Aplicação

1. Volte para a página de configuração da aplicação web
2. Clique no botão grande verde "Reload" para iniciar a aplicação

## 6. Manutenção

### Atualizar o Código

1. Faça as alterações no repositório
2. No console Bash do PythonAnywhere:
   ```bash
   cd ~/consultoria_calazans_producao
   git pull  # Se estiver usando GitHub
   ```
   Ou faça upload de um novo arquivo ZIP e descompacte-o
3. Recarregue a aplicação web clicando no botão "Reload"

### Backup do Banco de Dados

1. No console Bash:
   ```bash
   cp ~/consultoria_calazans_producao/instance/database.db ~/backup_$(date +%Y%m%d).db
   ```

## 7. Solução de Problemas

- Se a aplicação não iniciar, verifique os logs de erro na seção "Web" > "Logs"
- Certifique-se de que todos os caminhos nos arquivos de configuração correspondem à sua estrutura de diretórios
- Verifique se o ambiente virtual está corretamente configurado e todas as dependências estão instaladas
- Para testar localmente a aplicação antes de enviar para produção, execute:
  ```bash
  gunicorn wsgi:app
  ```

## 8. Novas Funcionalidades (Dashboard e Qualificação de Leads)

O sistema agora conta com um dashboard de relatórios e sistema de qualificação de leads. Certifique-se de que após o deploy:

1. Acesse a área administrativa em `/admin/reports` para verificar se o dashboard está funcionando corretamente
2. Acesse a área de leads qualificados em `/admin/reports/qualified-leads` para verificar o sistema de pontuação

### Detalhes das Novas Funcionalidades

- **Dashboard de Relatórios**: Fornece visualizações gráficas das métricas de leads, incluindo totais, tendências mensais, distribuição por fonte e eficácia de campanhas.
- **Sistema de Qualificação de Leads**: Atribui pontuações aos leads com base em critérios específicos para o contexto da Consultoria Calazans, permitindo priorização eficiente de acompanhamento.

### Dependências Adicionais

A implementação dessas funcionalidades utilizou Chart.js, que já está incluído nos arquivos estáticos do projeto. Não é necessário instalar dependências adicionais para o Python.

### Solução de Problemas Específicos

Se os gráficos não aparecerem corretamente:
1. Verifique os logs de erro do JavaScript no console do navegador
2. Certifique-se de que a rota `/api/dashboard-data` está retornando os dados esperados
3. Verifique se o banco de dados contém leads suficientes para gerar visualizações significativas

Para mais informações sobre a implementação, consulte a documentação em `docs/RELATORIO_DASHBOARD_LEADS.md`. 
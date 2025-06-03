# Reativação da Aplicação no PythonAnywhere

Se você pausou sua aplicação no PythonAnywhere e precisa reativá-la, siga estes passos:

## 1. Acesso ao PythonAnywhere

1. Acesse [PythonAnywhere](https://www.pythonanywhere.com) e faça login na sua conta
2. Vá para o Dashboard do PythonAnywhere

## 2. Verificar o Status da Aplicação

1. Na seção "Web", verifique se sua aplicação está listada
2. Se estiver marcada como "Disabled" ou "Stopped", você precisará reativá-la

## 3. Verificar o Ambiente Virtual

1. Abra um console Bash no PythonAnywhere
2. Ative o ambiente virtual da aplicação:
   ```bash
   workon calazans-venv
   ```
3. Navegue até a pasta do projeto:
   ```bash
   cd ~/consultoria_calazans_producao
   ```

## 4. Verificar o Banco de Dados

1. Verifique se o arquivo de banco de dados ainda existe:
   ```bash
   ls -la instance/database.db
   ```
2. Se o arquivo não existir ou se você precisar reinicializá-lo, execute:
   ```bash
   echo '
   from app import create_app
   app = create_app()
   from app.models.database import init_db
   with app.app_context():
       init_db()
   ' > init_db_script.py
   python init_db_script.py
   rm init_db_script.py
   ```

## 5. Reativar a Aplicação Web

1. Volte para a página "Web" no dashboard do PythonAnywhere
2. Se a aplicação estiver desativada, clique no botão para reativá-la
3. Clique no botão verde "Reload" para reiniciar a aplicação

## 6. Verificar os Logs

Se a aplicação não funcionar corretamente após a reativação:

1. Na seção "Web", clique nos links para os logs de erro
2. Verifique se há mensagens de erro específicas que possam indicar o problema

## 7. Atualização de Código (se necessário)

Se você fez alterações no código desde a última vez que a aplicação estava ativa:

1. Certifique-se de que seu código local está atualizado
2. Faça upload das alterações para o PythonAnywhere:
   - Se estiver usando GitHub: `git pull`
   - Se estiver fazendo upload manual: faça upload do arquivo ZIP e descompacte-o
3. Recarregue a aplicação após atualizar o código 
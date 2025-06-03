# Implementação do Gunicorn como Servidor WSGI

Este documento fornece instruções detalhadas para configurar o Gunicorn como servidor WSGI para a aplicação Consultoria Calazans.

## O que é Gunicorn e por que usá-lo?

Gunicorn (Green Unicorn) é um servidor WSGI HTTP para Python que implementa o protocolo WSGI, permitindo que aplicações Python como Flask sejam servidas de maneira mais eficiente e segura em ambientes de produção.

Vantagens do Gunicorn:
- Gerencia múltiplos processos (workers)
- Lida com requisições simultâneas eficientemente
- Implementa timeouts e recuperação de falhas
- Possui suporte a logging avançado
- É mais seguro e robusto que o servidor de desenvolvimento do Flask

## Instalação

1. Adicione o Gunicorn ao `requirements.txt`:

```
gunicorn==20.1.0
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração Básica

Para iniciar a aplicação com Gunicorn, use o comando:

```bash
gunicorn wsgi:app
```

Esse comando inicia o Gunicorn usando o objeto `app` exportado do módulo `wsgi.py`.

## Configuração Avançada

Para ambientes de produção, crie um arquivo `gunicorn_config.py`:

```python
# Configuração do Gunicorn para produção

# Número de workers (2-4 x núcleos + 1)
workers = 3

# Tipo de worker
worker_class = 'sync'

# Tempo máximo de processamento antes de reiniciar um worker
timeout = 30

# Porta de bind
bind = '0.0.0.0:8000'

# Arquivo de log
accesslog = 'logs/access.log'
errorlog = 'logs/error.log'
loglevel = 'info'

# Outras configurações
keepalive = 2
```

Inicie o Gunicorn com a configuração personalizada:

```bash
gunicorn -c gunicorn_config.py wsgi:app
```

## Script de Inicialização

Crie um script `start.sh` para facilitar a inicialização:

```bash
#!/bin/bash

# Ativa o ambiente virtual
source venv/bin/activate

# Define variáveis de ambiente para produção
export FLASK_APP=wsgi.py
export FLASK_ENV=production
export SECRET_KEY="chave_secreta_longa_gerada_aleatoriamente"

# Cria pasta para logs (se necessário)
mkdir -p logs

# Inicia o Gunicorn
gunicorn -c gunicorn_config.py wsgi:app
```

Não se esqueça de tornar o script executável:

```bash
chmod +x start.sh
```

## Integração com Nginx (Opcional, mas Recomendado)

Para uma configuração completa de produção, é recomendável usar o Nginx como proxy reverso:

1. Instale o Nginx:
```bash
sudo apt-get install nginx
```

2. Crie um arquivo de configuração para o site:
```
server {
    listen 80;
    server_name seudominio.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /caminho/para/seu/projeto/app/static;
    }
}
```

3. Habilite a configuração e reinicie o Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/seu_arquivo.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

## Gerenciamento com Supervisor (Opcional)

Para garantir que sua aplicação seja iniciada automaticamente e permaneça em execução, use o Supervisor:

```
[program:calazans]
command=/caminho/para/seu/projeto/start.sh
directory=/caminho/para/seu/projeto
user=seu_usuario
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/caminho/para/seu/projeto/logs/supervisor.err.log
stdout_logfile=/caminho/para/seu/projeto/logs/supervisor.out.log
```

## Atualização do `.flaskenv`

Atualize o arquivo `.flaskenv` para usar o `wsgi.py` em vez do `app.py`:

```
FLASK_APP=wsgi.py
FLASK_ENV=production
```

## Teste da Configuração

Para testar se a configuração do Gunicorn está funcionando:

```bash
# Teste básico
gunicorn wsgi:app --check-config

# Teste com configuração personalizada
gunicorn -c gunicorn_config.py wsgi:app --check-config
```

## Passos para Produção

1. Atualize e teste a aplicação localmente
2. Configure variáveis de ambiente de segurança
3. Implante os arquivos no servidor
4. Instale as dependências
5. Configure o Gunicorn
6. Inicie a aplicação com o script `start.sh`
7. Configure o servidor web (Nginx) se necessário
8. Configure o Supervisor se necessário 
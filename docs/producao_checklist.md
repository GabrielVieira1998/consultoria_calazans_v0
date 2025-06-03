# Checklist para Implantação em Produção

## Configurações Essenciais

- [ ] Atualizar arquivo `.flaskenv` para apontar para `wsgi.py`
- [ ] Remover configuração de debug em produção
- [ ] Mover SECRET_KEY para variável de ambiente
- [ ] Instalar Gunicorn (`pip install gunicorn`)
- [ ] Adicionar Gunicorn ao `requirements.txt`
- [ ] Criar script de inicialização para produção

## Segurança

- [ ] Verificar configurações de segurança do Flask
- [ ] Remover qualquer credencial hardcoded
- [ ] Configurar HTTPS se possível
- [ ] Validar entradas de usuários
- [ ] Verificar proteções contra CSRF

## Banco de Dados

- [ ] Verificar permissões do arquivo SQLite
- [ ] Configurar backups automáticos
- [ ] Testar recuperação do banco de dados
- [ ] Implementar migrações para atualizações futuras

## Monitoramento e Manutenção

- [ ] Configurar logs apropriados
- [ ] Implementar monitoramento básico
- [ ] Criar scripts de backup
- [ ] Documentar o processo de implantação
- [ ] Documentar o processo de atualização

## Testes Finais

- [ ] Testar todos os formulários e funcionalidades
- [ ] Verificar desempenho sob carga leve
- [ ] Testar fluxos completos de usuário
- [ ] Verificar responsividade em dispositivos móveis 
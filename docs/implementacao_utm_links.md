# Plano de Implementação - Sistema de Gerenciamento de Links UTM

Este documento descreve o plano para implementar um sistema completo de gerenciamento de links UTM no projeto Consultoria Calazans, com base na estrutura e identidade visual existentes.

## 1. Análise da Estrutura Atual

### Funcionalidades existentes
- Captura automática de parâmetros UTM através do middleware
- Armazenamento de parâmetros UTM na tabela `contacts` 
- Visualização de parâmetros UTM na página de relatórios

### Identidade visual
- Bootstrap 5 como framework CSS
- Cards para cada funcionalidade no dashboard
- Tabelas responsivas para exibição de dados
- Formulários com validação para entrada de dados
- Botões com cores consistentes (primário, secundário, perigo)

## 2. Criação da Nova Tabela no Banco de Dados

Adicionar à `app/schema.sql`:

```sql
DROP TABLE IF EXISTS utm_links;

CREATE TABLE utm_links (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  base_url TEXT NOT NULL,
  utm_source TEXT NOT NULL,
  utm_medium TEXT NOT NULL,
  utm_campaign TEXT NOT NULL,
  utm_term TEXT,
  utm_content TEXT,
  short_description TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_updated TIMESTAMP
);
```

## 3. Modelo para Gerenciamento de Links UTM

Criar arquivo `app/models/utm_links.py` com funções para:
- Obter todos os links UTM
- Obter link UTM por ID
- Adicionar novo link UTM
- Atualizar link UTM existente
- Excluir link UTM
- Gerar URL completa com parâmetros UTM

## 4. Rotas para o Gerenciamento de Links UTM

Adicionar à `app/routes/admin.py`:
- Rota para listar todos os links UTM
- Rota para adicionar novo link UTM
- Rota para editar link UTM existente
- Rota para excluir link UTM
- Rota para visualizar detalhes do link UTM (incluindo URL gerada)

## 5. Templates para a Interface Administrativa

Criar os seguintes templates:
- `app/templates/admin/utm_links.html`: Listar todos os links UTM
- `app/templates/admin/utm_link_form.html`: Formulário para adicionar/editar links UTM
- `app/templates/admin/utm_link_details.html`: Detalhes do link UTM, incluindo URL gerada

## 6. Atualização do Dashboard Administrativo

Adicionar um novo card ao dashboard (`app/templates/admin/dashboard.html`) para acessar a gestão de links UTM, mantendo a mesma estrutura visual dos cards existentes.

## 7. Estilo e Experiência do Usuário

- Manter a consistência com o design atual
- Adicionar validação de formulários
- Incluir feedback visual para ações (mensagens de sucesso/erro)
- Adicionar funcionalidade de copiar URL para a área de transferência
- Implementar visualização de QR code para links UTM

## 8. Testes

- Testar a criação, edição e exclusão de links UTM
- Verificar a geração correta de URLs
- Testar a funcionalidade de copiar URL
- Validar a exibição de QR codes

## 9. Documentação

Após a implementação, criar documentação completa sobre:
- Como usar o sistema de gerenciamento de links UTM
- Melhores práticas para nomenclatura de campanhas
- Explicação de cada parâmetro UTM e seu propósito

## Cronograma Estimado

1. Criação da tabela e modelo: 1 hora
2. Implementação das rotas: 1 hora
3. Desenvolvimento dos templates: 2 horas
4. Integração com o dashboard: 30 minutos
5. Testes e ajustes: 1 hora
6. Documentação: 30 minutos

**Tempo total estimado: 6 horas** 
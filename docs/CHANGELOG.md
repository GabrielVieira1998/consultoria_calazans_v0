# Changelog - Consultoria Calazans

## [1.0.0] - 2024-03-19

### Removido
- Removida a funcionalidade de cursos e todas as páginas relacionadas:
  - `app/templates/admin/courses.html`
  - `app/templates/admin/course_form.html`
  - `app/templates/pages/courses.html`
  - `app/models/courses.py`
- Removidas as rotas de cursos do admin e main
- Removido o link de cursos da navegação
- Removido o card de cursos do painel administrativo
- Removida a tabela de cursos do banco de dados

### Melhorias de Design e UX
- Adicionado um padrão de fundo sutil usando gradientes CSS
- Melhorado o contraste e legibilidade dos textos
- Adicionadas transições suaves para interações
- Implementado efeito de hover mais sofisticado nos cards
- Adicionado padrão de fundo decorativo no hero section
- Melhorada a hierarquia visual com sombras e elevações
- Atualizado o sistema de cores para melhor acessibilidade
- Adicionados efeitos de hover mais interativos
- Melhorada a consistência visual em todo o site

### Detalhes Técnicos
1. **Background Pattern**
   - Implementado usando CSS Gradients
   - Cores suaves que não interferem na legibilidade
   - Padrão geométrico sutil que adiciona profundidade

2. **Melhorias de Contraste**
   - Texto principal agora usa `--cinza-medio` (#606266)
   - Links e elementos interativos em `--verde-petroleo` (#39777B)
   - Hover states em `--verde-petroleo-escuro` (#245052)

3. **Animações e Transições**
   - Adicionadas transições suaves em todos os elementos interativos
   - Implementado efeito de elevação nos cards
   - Melhorada a animação do hero section

4. **Consistência Visual**
   - Padronização dos border-radius (12px)
   - Sistema consistente de sombras
   - Espaçamento uniforme entre elementos

### Arquivos Modificados
- `app/static/css/main.css`
- `app/routes/admin.py`
- `app/routes/main.py`
- `app/templates/layout.html`
- `app/templates/admin/dashboard.html`
- `app/schema.sql`

### Próximos Passos
1. Monitorar o feedback dos usuários sobre as mudanças visuais
2. Considerar a implementação de um modo escuro
3. Avaliar a necessidade de ajustes adicionais no contraste
4. Coletar métricas de usabilidade após as mudanças 
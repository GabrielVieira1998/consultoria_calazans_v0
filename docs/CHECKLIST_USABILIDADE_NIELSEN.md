# Checklist de Usabilidade - Heurísticas de Nielsen

Este documento serve como guia para avaliar e melhorar a usabilidade da plataforma Consultoria Calazans, tanto na versão web quanto mobile.

## Como usar este checklist

Para cada item:
- [ ] Marque a caixa se o critério for atendido
- Adicione notas sobre problemas encontrados e possíveis melhorias
- Priorize os problemas usando a seguinte escala:
  - **Alta**: Impede o uso ou causa frustração significativa
  - **Média**: Dificulta o uso mas tem contorno
  - **Baixa**: Pequeno incômodo ou oportunidade de melhoria

## 1. Visibilidade do status do sistema

O sistema deve sempre manter os usuários informados sobre o que está acontecendo, através de feedback apropriado dentro de um tempo razoável.

### Desktop
- [ ] Todas as ações do usuário recebem feedback visual ou textual
- [ ] Estados de carregamento são claramente indicados (spinners, barras de progresso)
- [ ] Mensagens de sucesso/erro são exibidas após ações importantes
- [ ] A página atual é destacada na navegação

### Mobile
- [ ] Feedback tátil ou visual é fornecido para toques em elementos interativos
- [ ] Estados de carregamento são otimizados para telas menores
- [ ] Notificações não obstruem conteúdo importante
- [ ] Indicadores de progresso são visíveis mesmo em telas pequenas

## 2. Correspondência entre o sistema e o mundo real

O sistema deve falar a linguagem do usuário, com palavras, frases e conceitos familiares, seguindo convenções do mundo real e apresentando informações em ordem lógica e natural.

### Desktop e Mobile
- [ ] A terminologia utilizada é familiar ao público-alvo (mulheres buscando recuperação física)
- [ ] Ícones e metáforas visuais são reconhecíveis e intuitivos
- [ ] O fluxo de navegação segue um processo lógico e natural
- [ ] Informações médicas e de exercícios são apresentadas em linguagem acessível
- [ ] Evita-se jargões técnicos desnecessários

## 3. Controle e liberdade do usuário

Os usuários frequentemente escolhem funções por engano e precisam de uma "saída de emergência" claramente marcada para sair do estado indesejado sem ter que passar por um processo extenso.

### Desktop
- [ ] Opção de cancelar ações está disponível em processos multi-etapas
- [ ] Botões "voltar" estão presentes em todas as páginas relevantes
- [ ] Confirmação é solicitada antes de ações irreversíveis
- [ ] Histórico de navegação funciona corretamente

### Mobile
- [ ] Gestos para voltar são suportados (swipe)
- [ ] Botões de navegação são grandes o suficiente para tocar facilmente
- [ ] Formulários salvam dados parcialmente preenchidos
- [ ] Usuário pode facilmente retornar à página inicial de qualquer ponto

## 4. Consistência e padrões

Os usuários não devem ter que se perguntar se diferentes palavras, situações ou ações significam a mesma coisa. Siga as convenções da plataforma.

### Desktop
- [ ] Layout, cores e tipografia são consistentes em todas as páginas
- [ ] Elementos de navegação permanecem no mesmo local
- [ ] Botões de ação primária têm aparência consistente
- [ ] Formulários seguem o mesmo padrão de design

### Mobile
- [ ] Design responsivo mantém consistência visual entre dispositivos
- [ ] Elementos tocáveis têm tamanho adequado (mínimo 44x44px)
- [ ] Gestos padrão funcionam como esperado
- [ ] Menus e navegação seguem padrões de aplicativos móveis

## 5. Prevenção de erros

Melhor que boas mensagens de erro é um design cuidadoso que previne que um problema ocorra.

### Desktop e Mobile
- [ ] Campos obrigatórios são claramente marcados
- [ ] Validação de formulários ocorre em tempo real
- [ ] Opções em menus dropdown evitam erros de digitação
- [ ] Confirmação antes de ações destrutivas ou irreversíveis
- [ ] Instruções claras antes de tarefas complexas
- [ ] Botões de ações opostas (salvar/cancelar) são visualmente distintos

## 6. Reconhecimento em vez de lembrança

Minimize a carga de memória do usuário tornando objetos, ações e opções visíveis. O usuário não deve ter que lembrar informações de uma parte da interface para outra.

### Desktop
- [ ] Menus de navegação mostram claramente todas as opções principais
- [ ] Breadcrumbs indicam localização atual no site
- [ ] Campos de busca são facilmente acessíveis
- [ ] Histórico de ações recentes está disponível quando relevante

### Mobile
- [ ] Menus compactos mostram opções principais mesmo em telas pequenas
- [ ] Informações importantes permanecem visíveis durante rolagem
- [ ] Elementos de navegação são fixos ou facilmente acessíveis
- [ ] Sugestões de busca auxiliam o usuário

## 7. Flexibilidade e eficiência de uso

Aceleradores – invisíveis para o usuário novato – podem aumentar a velocidade de interação para o usuário experiente, permitindo que o sistema atenda tanto usuários inexperientes quanto experientes.

### Desktop
- [ ] Atalhos de teclado estão disponíveis para ações comuns
- [ ] Histórico de buscas recentes é mantido
- [ ] Autopreenchimento em formulários economiza tempo
- [ ] Filtros avançados estão disponíveis mas não obstruem o uso básico

### Mobile
- [ ] Gestos avançados (pinch, swipe) complementam controles básicos
- [ ] Opção de salvar informações para uso futuro
- [ ] Interface se adapta às preferências do usuário
- [ ] Funcionalidades offline estão disponíveis quando possível

## 8. Estética e design minimalista

As interfaces não devem conter informações irrelevantes ou raramente necessárias. Cada unidade extra de informação compete com as unidades relevantes e diminui sua visibilidade relativa.

### Desktop
- [ ] Layout é limpo e sem poluição visual
- [ ] Informações são apresentadas em ordem de importância
- [ ] Espaçamento adequado entre elementos
- [ ] Hierarquia visual clara (títulos, subtítulos, conteúdo)

### Mobile
- [ ] Conteúdo é priorizado para telas pequenas
- [ ] Menus recolhíveis economizam espaço
- [ ] Imagens são otimizadas para carregamento rápido
- [ ] Densidade de informação é apropriada para visualização móvel

## 9. Ajudar usuários a reconhecer, diagnosticar e recuperar-se de erros

Mensagens de erro devem ser expressas em linguagem simples (sem códigos), indicar precisamente o problema e sugerir construtivamente uma solução.

### Desktop e Mobile
- [ ] Mensagens de erro são claras e em linguagem simples
- [ ] Erros indicam especificamente o que aconteceu
- [ ] Sugestões de correção são fornecidas
- [ ] Erros são visualmente distintos (mas não alarmantes)
- [ ] Erros de validação de formulário indicam exatamente qual campo precisa de correção
- [ ] Contato de suporte é facilmente acessível em caso de problemas

## 10. Ajuda e documentação

Embora seja melhor que o sistema possa ser usado sem documentação, pode ser necessário fornecer ajuda e documentação. Tais informações devem ser fáceis de pesquisar, focadas na tarefa do usuário, listar etapas concretas a serem executadas e não ser muito extensas.

### Desktop
- [ ] FAQ abrange as dúvidas mais comuns
- [ ] Tutoriais ou tours guiados estão disponíveis para novos usuários
- [ ] Dicas contextuais aparecem em momentos relevantes
- [ ] Documentação completa está acessível e pesquisável

### Mobile
- [ ] Ajuda é otimizada para telas pequenas
- [ ] Tutoriais são divididos em etapas gerenciáveis
- [ ] Documentação pode ser acessada offline
- [ ] Conteúdo de ajuda é conciso e visual

## Observações adicionais para a Consultoria Calazans

### Considerações específicas para o público-alvo
- [ ] Interface é acolhedora e não-intimidadora para mulheres buscando recuperação física
- [ ] Linguagem é inclusiva e empática
- [ ] Informações sobre exercícios são claras e seguras
- [ ] Privacidade e segurança dos dados são comunicadas claramente

### Acessibilidade
- [ ] Textos têm contraste adequado
- [ ] Tamanho de fonte é ajustável ou suficientemente grande
- [ ] Alternativas textuais para conteúdo visual
- [ ] Interface é navegável por teclado ou tecnologias assistivas

---

## Resultados da avaliação

**Data da avaliação**: _____________________

**Avaliador(es)**: _____________________

### Problemas identificados (prioridade alta)
1. 
2. 
3. 

### Problemas identificados (prioridade média)
1. 
2. 
3. 

### Problemas identificados (prioridade baixa)
1. 
2. 
3. 

### Próximos passos
1. 
2. 
3. 
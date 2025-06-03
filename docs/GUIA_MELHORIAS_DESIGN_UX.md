# Guia de Implementação de Melhorias de Design e UX — Consultoria Calazans

Este documento serve como referência para aplicar as principais melhorias de identidade visual, contraste, acessibilidade e experiência do usuário no projeto.

---

## 1. Logo no Header

- **Aumentar o tamanho do logo para 72x72px.**
- **Deixar o logo circular** usando `border-radius: 50%`, borda de 3px na cor principal e leve sombra.
- **Remover o texto "Consultoria Calazans" ao lado do logo** se a imagem já contiver o nome.
- **Adicionar/ajustar o atributo `alt`** para acessibilidade.

**Exemplo de HTML:**
```html
<a class="navbar-brand d-flex align-items-center" href="{{ url_for('index') }}">
    <img src="{{ url_for('static', filename='images/Logo_Oficial_Consultoria.png') }}" alt="Logo da Consultoria Calazans" class="logo-circular" style="height: 72px; width: 72px; object-fit: cover;">
</a>
```

**Exemplo de CSS:**
```css
.logo-circular {
  border-radius: 50%;
  box-shadow: 0 2px 8px rgba(57,119,123,0.10);
  border: 3px solid var(--verde-petroleo);
  background: #fff;
}
```

---

## 2. Paleta de Cores e Contraste

- **Atualizar variáveis CSS para:**
  - `--verde-petroleo: #39777B;`
  - `--pessego-claro: #F4CFC3;`
  - `--cinza-medio: #606266;` <!-- atualizado para melhor contraste -->
  - `--off-white: #FAF9F7;`

- **Aplicar as cores em botões, links, textos e rodapé.**

---

## 3. Navbar e Links

- **Links da navbar:** Hover em verde petróleo mais escuro (`#245052`) e sublinhado.
- **Links do rodapé:** Cor branca, hover em pêssego claro.

**Exemplo de CSS:**
```css
.navbar-nav .nav-link:hover, .navbar-nav .nav-link:focus {
  color: #245052;
  text-decoration: underline;
}
footer a {
  color: #fff;
  text-decoration: underline;
}
footer a:hover {
  color: var(--pessego-claro);
}
```

---

## 4. Acessibilidade e UX

- **Garantir contraste mínimo de 4.5:1** para textos e links importantes.
- **Responsividade:** O logo e o header devem se adaptar bem em dispositivos móveis.
- **Feedback visual:** Links e botões devem ter feedback claro ao passar o mouse ou ao serem clicados.
- **Espaçamento:** Manter espaçamento consistente entre elementos do header e do restante da página.

---

## 5. Checklist para o Agente

- [ ] Atualizar o HTML do header conforme o exemplo.
- [ ] Adicionar/ajustar a classe `.logo-circular` no CSS.
- [ ] Atualizar variáveis de cor no CSS.
- [ ] Ajustar hover e contraste dos links.
- [ ] Remover redundância textual do header.
- [ ] Garantir responsividade e acessibilidade.

---

**Observação:**  
Este guia pode ser indexado no Cursor para que o agente aplique todas as melhorias automaticamente no projeto oficial.

--- 
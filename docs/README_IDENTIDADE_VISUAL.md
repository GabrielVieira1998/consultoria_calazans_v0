# Documentação de Identidade Visual e UX

## Processo Criativo

Como especialista em design e UX, realizei uma análise detalhada da interface da plataforma Consultoria Calazans, focando em:
- Visibilidade e destaque do logo
- Contraste e acessibilidade das cores
- Redução de redundância visual
- Melhoria da experiência do usuário em diferentes dispositivos

### 1. Visibilidade e Destaque do Logo
- **Aumento do tamanho:** O logo foi ampliado para 72x72px, tornando-se mais presente e visível no header.
- **Formato circular:** Apliquei borda arredondada (border-radius: 50%) e uma borda de destaque na cor principal da marca, criando um enquadramento elegante e moderno.
- **Remoção de redundância:** O texto "Consultoria Calazans" foi removido do lado do logo, pois a imagem já contém o nome, evitando poluição visual.

### 2. Contraste e Acessibilidade
- **Links da navbar:** O hover agora utiliza um verde petróleo mais escuro (#245052) e sublinhado, melhorando o contraste e a percepção de interatividade.
- **Footer:** Os links do rodapé agora são brancos, com hover em pêssego claro, garantindo contraste suficiente para acessibilidade.
- **Paleta de cores:** Todas as cores seguem a identidade visual extraída do logo, reforçando a marca e facilitando a navegação.

### 3. Experiência do Usuário (UX)
- **Foco visual:** O logo é o primeiro elemento do header, alinhado à esquerda, facilitando o reconhecimento da marca.
- **Responsividade:** O tamanho e formato do logo garantem boa visualização em diferentes tamanhos de tela.
- **Acessibilidade:** O atributo `alt` da imagem foi revisado para descrever corretamente o logo.
- **Feedback visual:** Links e botões possuem feedback claro ao passar o mouse.

## Implementação

### HTML (layout.html)
- Substituição do bloco da navbar para:

```html
<a class="navbar-brand d-flex align-items-center" href="{{ url_for('index') }}">
    <img src="{{ url_for('static', filename='images/Logo_Oficial_Consultoria.png') }}" alt="Logo da Consultoria Calazans" class="logo-circular" style="height: 72px; width: 72px; object-fit: cover;">
</a>
```

### CSS (main.css)
- Adição da classe:
```css
.logo-circular {
  border-radius: 50%;
  box-shadow: 0 2px 8px rgba(57,119,123,0.10);
  border: 3px solid var(--verde-petroleo);
  background: #fff;
}
```
- Ajuste de hover e contraste:
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

## Considerações Finais
- Todas as alterações seguem boas práticas de design, acessibilidade e UX.
- O logo agora é o elemento central da identidade visual, com destaque e clareza.
- O contraste e a navegação foram aprimorados para todos os públicos.

---

Se desejar expandir a identidade visual para outras áreas do site, basta seguir o padrão de cores e estilos definidos aqui. 
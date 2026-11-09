# Site do Hirly

Página única em HTML, CSS e JavaScript. Não precisa de build nem de instalar nada.

## Arquivos
- `index.html`: o site inteiro (estilos e scripts dentro do próprio arquivo)
- `og-image.png`: imagem que aparece quando o link é compartilhado (WhatsApp, Instagram, LinkedIn)
- `favicon.svg`: ícone da aba do navegador

## Ver no computador
Dê dois cliques em `index.html` para abrir no navegador.

## Antes de lançar
1. **Lista de espera:** no fim do `index.html`, procure `const CONFIG` e preencha `waitlistEndpoint`
   com o endereço que vai receber os cadastros (Formspree, Google Apps Script ou um backend próprio).
   Enquanto estiver vazio, o formulário só mostra a mensagem de sucesso e não salva nada.
2. **Placeholders:** procure por `[` no arquivo para achar `[número]`, `[Depoimento aqui]`, `[e-mail]`,
   `[Instagram]`, `[TikTok]` e `[LinkedIn]`, e troque pelos dados reais.
3. **Links legais:** troque os `href="#"` de Termos de Uso e Política de Privacidade pelos links reais.
4. **Imagem de compartilhamento:** com o domínio no ar, troque `og-image.png` nas tags `og:image` e
   `twitter:image` pelo endereço completo, por exemplo `https://hirly.com.br/og-image.png`.
5. **Lojas:** quando o app lançar, preencha `appStoreUrl` e `playStoreUrl` no `CONFIG`.

## Hospedar num servidor Linux (Nginx)
```bash
sudo mkdir -p /var/www/hirly
sudo cp index.html og-image.png favicon.svg /var/www/hirly/
```
Configure o Nginx com `root /var/www/hirly;` e ative HTTPS com o Certbot (Let's Encrypt):
```bash
sudo certbot --nginx -d hirly.com.br -d www.hirly.com.br
```
Alternativas sem servidor e gratuitas: Cloudflare Pages, Netlify ou Vercel (é só arrastar a pasta).

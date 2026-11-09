# Hirly

**Sua próxima vaga, num swipe.**

Hirly reúne estágios, programas de trainee e primeiros empregos num feed no estilo TikTok. O candidato desliza pelas vagas, vê o seu percentual de match com cada uma e se candidata com um clique. É grátis para candidatos.

🌐 **Site:** https://diegocastro-code.github.io/Hirly/

## O que tem aqui

```
Hirly/
├── site/                     Página de divulgação com lista de espera
│   ├── index.html            O site inteiro (HTML, CSS e JS num arquivo só)
│   ├── og-image.png          Imagem de prévia ao compartilhar o link
│   ├── favicon.svg           Ícone da aba do navegador
│   └── LEIA-ME.md            Checklist de lançamento e como hospedar
└── marketing/
    ├── Hirly_comercial_v1.mp4        Vídeo comercial (vertical, 1080×1920)
    └── fonte-do-video/
        ├── comercial-video-fonte.html  Animação que dá origem ao vídeo
        └── render-video.py             Script que grava a animação em MP4
```

## Ver o site no computador

Não precisa instalar nada: basta abrir `site/index.html` no navegador com dois cliques.

## Atualizar o site publicado

O site é publicado pelo GitHub Pages a partir da branch `gh-pages`, que guarda só o conteúdo da pasta `site/`. Depois de alterar e enviar a `main`, rode na raiz do projeto:

```bash
git subtree split --prefix site -b gh-pages
git push origin gh-pages
```

Em um ou dois minutos o link já mostra a nova versão.

## Antes do lançamento

O site ainda tem itens provisórios: o endereço que recebe os cadastros da lista de espera, textos entre colchetes (`[e-mail]`, `[Depoimento aqui]`...), os links de Termos e Privacidade e os links das lojas de aplicativos. A lista completa, com onde mexer em cada um, está em [site/LEIA-ME.md](site/LEIA-ME.md).

Enquanto o endereço da lista de espera estiver vazio, o formulário mostra a mensagem de sucesso, mas **não salva nenhum cadastro**.

## Gerar o vídeo de novo

O `render-video.py` abre a animação num navegador controlado pelo Playwright, tira uma foto de cada quadro e junta tudo com o FFmpeg. Para rodar, é preciso ter Python, `playwright`, Google Chrome e `ffmpeg` instalados.

Antes, ajuste duas coisas no script, porque ele foi escrito para Linux: o nome do arquivo HTML (o script espera `comercial.html`) e o caminho do Chrome (`/usr/bin/google-chrome`).

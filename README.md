# Convite de Casamento Digital — Helena & Rafael (modelo)

Convite interativo: envelope com selo de cera, carta que desdobra em sanfona, páginas com local, dress code, presentes (Pix) e confirmação de presença por WhatsApp.

- `index.html` — o site pronto (arquivo único, imagens e bibliotecas embutidas). É o que a Vercel publica.
- `src/index.html` — código-fonte. Edite o bloco `CONFIG` no topo do script (noivos, data, local, Pix, convidados…).
- `img/` — imagens usadas no build.
- `tools/build.py` — gera o `index.html` a partir de `src/` (embute imagens, GSAP e QR Code).

## Links personalizados por convidado
`https://seu-dominio.com/ana` ou `https://seu-dominio.com/#ana` — o código precisa existir em `CONFIG.convidados`.

## Antes de entregar
- `CONFIG.demo = false` (esconde o painel de demonstração)
- Testar o Pix com R$ 0,01

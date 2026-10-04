# Relatório das Máquinas - Amarildo Bragança

Site para marcar, todo dia, o estado de cada máquina (Funcionando,
Manutenção ou Parada) e gerar o relatório no formato que vai para o
WhatsApp. Feito para usar no celular.

- Sem senha: abre pelo link que a Lorena manda. O link carrega uma chave
  (depois do `#`), e os dados ficam no Firestore debaixo dessa chave. Quem
  não tem o link não acha nada. O celular lembra a chave depois da primeira
  vez.
- Os dados ficam no Firestore (projeto `relatorio-maquinas`): não se
  apagam e abrem em qualquer aparelho.
- Funciona com sinal fraco: a marcação feita sem internet fica no celular e
  sobe sozinha quando o sinal volta.
- Cada dia começa igual ao último relatório; só se mexe no que mudou.

## Onde está no ar

GitHub Pages, publicado a cada push na `main`
(`.github/workflows/publicar.yml`). O site é a pasta `site/`, sem montagem:
um `index.html` só.

## O que mora fora do repositório

O repositório é público. Por isso **a lista das máquinas e a chave do link
não estão aqui**: a lista mora no banco, e a chave mora só no link e nas
regras do Firestore, coladas no console. O arquivo `firestore.rules` é o
modelo dessas regras, com uma chave de exemplo.

A configuração do Firebase dentro do `index.html` não é segredo: vai dentro
de todo site com Firebase. Quem protege os dados é a chave do link, conferida pelas regras.

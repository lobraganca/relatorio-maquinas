# O que uma sessão nova precisa saber

**Este repositório não tem nada a ver com o `Nuvem-Lorena`** (Ei Itabirito,
Avena) nem com o `catalogo-de-pecas`. A dona pede os apps separados.

- O app é um arquivo só: `site/index.html`. Sem npm, sem montagem.
- Firebase: só Firestore, projeto `relatorio-maquinas`, SDK fixo em 10.12.2
  vindo do gstatic. **Sem login — a dona não quer senha.** Os dados moram em
  `frotas/<chave>/...`; a chave vem no link (depois do `#`) e fica guardada
  no aparelho. Não pôr a chave no código: o repositório é público.
- O visual e o funcionamento são os do app que a dona aprovou no Claude
  (artifact "Relatório das Máquinas"). Ela pediu: "não altere nada do que
  estava antes". Mudança de tela só a pedido dela.
- Coleções, debaixo de `frotas/<chave>/`: `maquinas/{numero}` (`tipo`, `numero`, `ordem`),
  `dias/{AAAA-MM-DD}` (`data`, `itens` com `{s, obs, numero, tipo}` por
  máquina; `s` é `ok`, `manut` ou `parada`), `config/geral` (`cabecalho`).
- As regras do banco são coladas à mão no console. O `firestore.rules` daqui
  é modelo, com uma chave de exemplo.
- **Não pôr a lista da frota no código.** Número de máquina e defeito são
  dados do serviço do pai da dona; moram só no banco.
- O relatório: o número no título de cada tipo é quantas estão FUNCIONANDO
  (dois dígitos), e debaixo vêm só as paradas e as em manutenção.

Como a dona trabalha: português, celular, pede curto. Dizer com clareza o que
foi e o que não foi verificado.

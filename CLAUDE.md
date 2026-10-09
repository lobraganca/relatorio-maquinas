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
- As regras do banco (`firestore.rules`) não guardam a chave: exigem só uma
  chave de 28+ caracteres e as três coleções. Publicar: `python3 regra.py`
  no Cloud Shell (a dona não conseguiu colar na caixa do console pelo
  celular).
- **Não pôr a lista da frota no código.** Número de máquina e defeito são
  dados do serviço do pai da dona; moram só no banco.
- **Gravação por máquina, nunca o dia inteiro.** Cada toque grava só
  `itens.<id>` (setDoc com mergeFields) e o texto `relatorio` do dia. Em
  05/10 a versão que regravava o dia inteiro gravou um dia com 14 das 48
  máquinas, porque o celular ainda não tinha trazido o dia anterior.
- Toda máquina sem marcação hoje herda a do último dia (`ultimoAntes`, lido
  do SERVIDOR — a cópia do celular sem sinal responde "vazio" sem errar) e
  isso é gravado, mas só depois de o banco confirmar o dia de hoje.
- O relatório: o número no título de cada tipo é quantas estão LIBERADAS
  (dois dígitos); debaixo vêm as paradas, as em manutenção e as liberadas
  que tenham observação.
- A observação fica até a pessoa apagar: trocar o status NÃO a apaga (já
  apagou, e quem escrevia em Manutenção e marcava Liberado perdia o texto).

Como a dona trabalha: português, celular, pede curto. Dizer com clareza o que
foi e o que não foi verificado.

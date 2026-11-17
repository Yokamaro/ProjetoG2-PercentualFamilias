# Dicionário de dados

## Origem

Arquivo bruto: `data/raw/1461_original.xls` e extração tabular `data/raw/tabela_1461_fonte.csv`.

Fonte indicada na planilha: IBGE, Diretoria de Pesquisas, Coordenação de Índices de Preços, Pesquisa de Orçamentos Familiares 2002–2003, Tabela 1461. A tabela apresenta famílias por existência de problemas no domicílio, segundo as 12 maiores capitais, em percentuais.

Cada linha representa uma capital. As variáveis de problemas representam percentuais de respostas **Sim**. Os percentuais Não foram omitidos da tabela analítica porque a análise se concentra na ocorrência declarada.

| Variável | Tipo | Unidade/formato | Significado |
|---|---|---|---|
| `capital` | texto | nome | Capital brasileira apresentada na tabela |
| `Pouco espaço` | numérico decimal | percentual (%) | Percentual de famílias que responderam “Sim” para: pouco espaço |
| `Rua ou vizinhos barulhentos` | numérico decimal | percentual (%) | Percentual de famílias que responderam “Sim” para: rua ou vizinhos barulhentos |
| `Casa escura` | numérico decimal | percentual (%) | Percentual de famílias que responderam “Sim” para: casa escura |
| `Telhado com goteira` | numérico decimal | percentual (%) | Percentual de famílias que responderam “Sim” para: telhado com goteira |
| `Fundação, paredes ou chão úmidos` | numérico decimal | percentual (%) | Percentual de famílias que responderam “Sim” para: fundação, paredes ou chão úmidos |
| `Madeira das janelas, portas ou assoalhos deteriorados` | numérico decimal | percentual (%) | Percentual de famílias que responderam “Sim” para: madeira das janelas, portas ou assoalhos deteriorados |
| `Poluição ou problemas ambientais causados pelo trânsito ou indústria` | numérico decimal | percentual (%) | Percentual de famílias que responderam “Sim” para: poluição ou problemas ambientais causados pelo trânsito ou indústria |
| `Violência ou vandalismo na área de residência` | numérico decimal | percentual (%) | Percentual de famílias que responderam “Sim” para: violência ou vandalismo na área de residência |

## Observações metodológicas

- Os valores são percentuais publicados na tabela, não microdados domiciliares.
- A média entre capitais é aritmética simples, sem ponderação pelo tamanho populacional ou amostral.
- A fonte informa que as respostas foram prestadas por um único membro indicado pela família.
- A planilha apresenta oito problemas, com respostas “Sim” ou “Não”.
- Não há, no arquivo fornecido, informação suficiente para calcular erros-padrão ou intervalos de confiança.
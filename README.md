# Condições habitacionais nas 12 maiores capitais brasileiras

**Autores:** Yago Amaro Zamborlini e Pedro Augusto Pereira da Silva  
**Curso:** Bacharelado em Sistemas de Informação — 6º período  
**Instituição:** Unilasalle
**Professor:** Alexandre Louzada.
**Disciplina:** Linguagem de Programação (Análise e Visualização de Dados com Python)  
**Fonte:** IBGE, POF 2002–2003, Tabela 1461.
**GitHub Pages**: https://yokamaro.github.io/ProjetoG2-PercentualFamilias/

## Resumo
Projeto de análise exploratória de oito problemas domiciliares declarados por famílias em 12 capitais brasileiras. O estudo usa percentuais de respostas “Sim” da Tabela 1461, calcula estatísticas descritivas e apresenta visualizações no artigo HTML.

## Perguntas de pesquisa
1. Quais problemas apresentam os maiores percentuais médios?
2. Como os percentuais variam entre as capitais?
3. Quais capitais têm as maiores e menores médias simples dos oito indicadores?

## Estrutura
- `data/raw/`: planilha original e extração CSV.
- `data/processed/`: dados tratados, JSON e estatísticas.
- `data/data_dictionary.md`: dicionário de dados.
- `src/etl.py`: pipeline determinístico.
- `notebooks/analise_exploratoria.ipynb`: exploração e validação.
- `docs/index.html`: artigo acadêmico para GitHub Pages.

## Como reproduzir
Requer Python 3.11.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
python src/etl.py
```

Abra `docs/index.html` no navegador para visualizar o artigo. O HTML usa SVG embutido e não depende de CDN para exibir os gráficos.

## Publicação no GitHub Pages
1. Crie um repositório público e envie os arquivos.
2. Em **Settings → Pages**, escolha **Deploy from a branch**.
3. Selecione a branch `main` e a pasta `/docs`.
4. Salve e aguarde a publicação.
5. Atualize no artigo os campos de instituição, docente e URL do repositório.

## Fonte e limitações
A planilha informa que as respostas foram prestadas por um único membro indicado pela família e que foram apresentados oito problemas com respostas “sim” ou “não”. A análise utiliza percentuais agregados publicados; não contém microdados, tamanhos amostrais por célula ou medidas de incerteza. As médias entre capitais são simples, sem ponderação.

## Palavras-chave
Condições habitacionais; IBGE; POF; dados públicos; análise exploratória; Python.

## Licenças
Código: MIT (`LICENSE`). Texto e dados derivados: CC BY 4.0 (`LICENSE-DATA.md`), respeitando a atribuição à fonte original.

"""Pipeline determinístico para a Tabela 1461 (IBGE/POF 2002–2003)."""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "tabela_1461_fonte.csv"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(RAW, encoding="utf-8-sig")
    df.columns = [c.strip() for c in df.columns]
    if "capital" not in df.columns:
        raise ValueError("A coluna obrigatória 'capital' não foi encontrada.")
    if df["capital"].duplicated().any():
        raise ValueError("Foram encontradas capitais duplicadas.")
    numeric = [c for c in df.columns if c != "capital"]
    df[numeric] = df[numeric].apply(pd.to_numeric, errors="coerce")
    if df[numeric].isna().any().any():
        raise ValueError("Há valores ausentes ou não numéricos nos indicadores.")
    if not df[numeric].apply(lambda col: col.between(0, 100).all()).all():
        raise ValueError("Há percentuais fora do intervalo de 0 a 100.")
    df.to_csv(OUT / "problemas_domiciliares.csv", index=False, encoding="utf-8")
    df.to_json(OUT / "problemas_domiciliares.json", orient="records", force_ascii=False, indent=2)
    stats = df[numeric].agg(["mean", "median", "std", "min", "max"]).T
    stats.to_csv(OUT / "estatisticas_por_problema.csv", encoding="utf-8")
    df["media_simples_indicadores"] = df[numeric].mean(axis=1)
    df[["capital", "media_simples_indicadores"]].to_csv(
        OUT / "media_por_capital.csv", index=False, encoding="utf-8"
    )
    print(f"Pipeline concluído: {len(df)} capitais, {len(numeric)} indicadores.")

if __name__ == "__main__":
    main()

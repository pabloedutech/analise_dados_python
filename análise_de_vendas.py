import os
import pandas as pd
import matplotlib.pyplot as plt

# Verifica e cria as pastas se não existirem
if not os.path.exists("graficos_mes"):
    os.mkdir("graficos_mes")

if not os.path.exists("planilha_dados"):
    print("Pasta 'planilha_dados' não encontrada. Certifique-se de colocar os arquivos lá.")
else:
    # Carrega a planilha de vendas
    excel = pd.read_excel(os.path.join("planilha_dados", "vendas_2023.xlsx"))

    # Cria uma pasta para os gráficos
    if not os.path.exists(os.path.join("graficos_mes")):
        os.mkdir(os.path.join("graficos_mes"))

    # Visualização dos dados com gráficos
    for col in excel.columns[1:]:
        plt.figure(figsize=(10, 6))
        plt.bar(excel["Vendedor"], excel[col])
        plt.title(f"Vendas por Vendedor - {col}")
        plt.xlabel("Vendedor")
        plt.ylabel("Vendas")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join("graficos_mes", f"grafico_{col}.png"))
        plt.close()

    print("Gráficos de vendas por vendedor foram criados.")

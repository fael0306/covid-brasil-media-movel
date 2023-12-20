import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura do arquivo de dados
covid = pd.read_csv("C:\\Users\\f0fp1107\\Documents\\covid.csv")

# Filtrando dados do Brasil
covid_brazil = covid[covid['location'] == "Brazil"]

# Preenchendo valores nulos com zero
covid_brazil = covid_brazil.fillna(0)

# Selecionando os últimos 60 dias para o gráfico
casos = covid_brazil['new_cases'].tail(60)

# Função para calcular a média móvel dos casos
def calc_media_movel(casos, tam):
    return casos.rolling(window=tam).mean()

tam = int(len(casos)**0.5)
mediamovel = calc_media_movel(casos, tam)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=covid_brazil, x=covid_brazil.index, y='new_cases', label='Casos Diários')
sns.lineplot(data=mediamovel, label=f'Média Móvel ({tam} dias)')
plt.xlabel("Dia")
plt.ylabel("Número de Casos")
plt.title("Casos Diários e Média Móvel de COVID-19 no Brasil")
plt.legend()
plt.show()

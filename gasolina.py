# importando as bibliotecas necessárias
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import savefig

# Lendo os dados
df = pd.read_csv(filepath_or_buffer= 'gasolina.csv', sep = ',', header= 0)

# Criando o gráfico
obj = sns.lineplot(
    data = df,
    x = 'dia',
    y = 'venda',
    color = 'magenta'
)

# Editando título do gráfico e dos eixos
obj.set_title("Valor de Venda da Gasolina x Dias")
obj.set_xlabel('Dias')
obj.set_ylabel('Valor da Gasolina')

# Editando os rótulos dos eixos
obj.set_xticks(df['dia'])

# Colocando linhas de grade
obj.grid()

# Salvando o gráfico gerado
savefig('gasolina.png')

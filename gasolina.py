import pandas as pd
from matplotlib.pyplot import savefig,figure,subplots,show

# Lendo os dados
df = pd.read_csv(filepath_or_buffer= 'gasolina.csv', sep = ',', header= 0)

fig,ax = subplots(figsize= (12,8))

ax.plot('dia', 'venda', data= df)

ax.set_title("Valor de Venda da Gasolina x Dias")
ax.set_xlabel('Dias')
ax.set_ylabel('Valor da Gasolina')

# Editando os rótulos dos eixos
ax.set_xticks(df['dia'])

# Colocando linhas de grade
ax.grid()

# Colocando o valor de cada ponto
for x in zip(df['dia'], df['venda']):
    ax.annotate(
        'R$'+str(x[1]),
        xy= x,
        horizontalalignment = 'left',
        fontsize = 12,
        color = 'darkgreen',
        style = 'oblique'
        )

# Pegando o Menor valor de venda registrado no período
menor = df['venda'].min()

# Pegando o índice
min_idx = df.query('venda == @menor').index.to_list()

# Criando uma seta para apontar no gráfico o menor valor registrado
ax.annotate(
    text='Menor Valor no Período', 
    xy= (int(df['dia'].iloc[min_idx]),float(df['venda'].iloc[min_idx])), 
    xytext=(5.5,5), 
    arrowprops= dict(facecolor = 'red', arrowstyle= '->')
    )

# Salvando o gráfico gerado
savefig('gasolina.png')

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from plotly.graph_objs import Figure

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group" )
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as lojas")
app.layout = html.Div(children=[
    html.H1(children='Faturamento das lojas'),
    html.H2(children='Grafico com o faturamneto dos produtos por lojas'),

    html.Div(children='''
        obs: esse grafico mostra a quantidade de produtos vendidos
    '''),

   dcc.Dropdown(opcoes, value='Todas as lojas', id='lista-lojas'),

    dcc.Graph(
        id='grafico-quantidade',
        figure=fig
    )
])
# call back
@app.callback(
    Output('grafico-quantidade', 'figure'),
    Input('lista-lojas', 'value')
)
def update_output(value):
    if value == "Todas as lojas":
       fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group" )
    else:
        tabela_filtrada = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group" )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
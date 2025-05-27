from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.gapminder(return_type='pandas')
# print(df)
# Initialize Dash app
app = Dash(__name__)
server = app.server

countries=pd.Series(df['country']).unique()
# print(countries)

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': symbol, 'value': symbol} for symbol in countries],
        value='Canada'
    ),
    dcc.Graph(id='gdp-growth')
])

# # Callback for dynamic updates
@app.callback(
    Output('gdp-growth', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(country_name):
    mask = df['country']==country_name
    fig = px.line(df[mask], x='year', y='gdpPercap', title=f'{country_name} GDP')
    return fig

# Run the app
if __name__ == '__main__': 
    app.run(debug=True) 
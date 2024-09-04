from dash import dcc, html, Dash ,  dash_table
from dash.dependencies import Input, Output
import plotly.express as px
df=px.data.gapminder()
def gg1(x):
    return px.bar(df[df['country'].isin(x)],color='country',x='year',y='lifeExp',barmode='group')
def gg2(x):
    return px.box( df[df['country'].isin(x)], x='country', color='country', y='lifeExp')


app = Dash()

# Define the sidebar layout
sidebar = html.Div(
    [
        html.H2("Life expectancy"),
        html.Hr(),
        dcc.Checklist(id='d1',options=df['country'].unique())
    ],
    style={
        'padding': '10px',
        'width': '20%',
        'backgroundColor': '#93b1bf',
        'position': 'fixed',  # Keep the sidebar fixed on the left
        'height': '100%',
        'overflowY': 'auto',  # Scroll if the content is long
    }
)

# Define the content layout
content = html.Div(
     [
    dcc.Textarea(id='t1',readOnly=True,style={'width': '100%'}),
    dcc.Graph(id='g1', figure=gg1(['Egypt'])),
    dcc.Graph(id='g2', figure=gg2(['Egypt'])),
    dash_table.DataTable(
        id='table1',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'width': '50%'},  
         page_size=10,
        style_header={ 'backgroundColor': 'rgb(30, 30, 30)','color': 'white' },
        style_cell=  { 'textAlign': 'left',  'padding': '10px','fontFamily': 'Arial',        })        
        ],
    style={
        'margin-left': '25%',        'padding': '20px',
    }
)

# Combine the sidebar and content in the app layout
app.layout = html.Div([
    sidebar,
    content
])


@app.callback( Output('g1','figure'),Output('g2','figure'),Output('t1','value'), Output('table1','data'), Input('d1','value')   )
def updatetext(x):    
    if(x ==None):
        return gg1(['Egypt']), gg2(['Egypt']),'',df.to_dict('records')
    else:
        return gg1(x), gg2(x),'Life expectancy of '+str(x),df[df['country'].isin(x)].to_dict('records')
    
if __name__ == "__main__":
    app.run_server(debug=True)

import dash
from dash import dcc
from dash import html
from dash import Input, Output, State
import plotly.graph_objs as go


########### Define your variables ######

myheading1='McDonald\'s Menu'
tabtitle = 'Mickey D\'s'
list_of_options=['McChicken', 'McRib', 'McDouble', 'McNuggets']
list_of_images=['t-mcdonalds-Chicken-McNuggets-4pc-1_1-3-product-tile-desktop.jpeg', 't-mcdonalds-McChicken-1_1-3-product-tile-desktop.jpeg', 't-mcdonalds-McDouble.jpeg', 't-mcdonalds-McRib-new_1-3-product-tile-desktop.jpeg', 'download.png']
sourceurl = 'https://xkcd.com/'
githublink = 'https://github.com/plotly-dash-apps/203-radio-callbacks'


########## Set up the chart

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.RadioItems(
        id='your_input_here',
        options=[
                {'label':list_of_options[0], 'value':list_of_images[1]},
                {'label':list_of_options[1], 'value':list_of_images[3]},
                {'label':list_of_options[2], 'value':list_of_images[2]},
                {'label':list_of_options[3], 'value':list_of_images[0]},
                ],
        value=list_of_images[4],
        ),
    html.Div(id='your_output_here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(Output('your_output_here', 'children'),
              [Input('your_input_here', 'value')])
def radio_results(image_you_chose):
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': '50%'}),


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)

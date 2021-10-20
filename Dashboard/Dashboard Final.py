import dash
import dash_leaflet as dl
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table as dt
from dash.dependencies import Input, Output, State

import os
import numpy as np
import pandas as pd
import base64

from jupyter_plotly_dash import JupyterDash
from pymongo import MongoClient
from bson.json_util import dumps
from animal_shelter import AnimalShelter

###########################
#Data Manipulation / Model
###########################

username = "accuser"
password = "hello"
shelter = AnimalShelter(username, password)

labels = ['Dog Male','Dog Female','Cat Male','Cat Female']
values = [0, 1, 2, 3]

df3 = pd.DataFrame({'labels': labels, 'values': values})


#Loads data from aac_shelter_outcomes.csv
df = pd.read_csv('aac_shelter_outcomes.csv')
df2 = px.data.tips()


#########################
#Dashboard Layout / View
#########################

app = dash.Dash(__name__)

#Loads Image
image_filename = 'GS_Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#Unique Identifier
app.layout = html.Div([
    
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
    html.Center(html.B(html.H1('SNHU CS-340 Dashboard'))),
    html.Hr(),
    html.H1("Robert Swanke"),
    html.Div(
       
        
    #Radio Buttons
    ),
    html.Hr(),
    dcc.RadioItems(
        id='dogtype',
        options=[
            {'label': 'Water Rescue', 'value': 'Water'},
            {'label': 'Mountian Rescue', 'value': 'Mountian'},
            {'label': 'Disaster Rescue', 'value': 'Disaster'},
            {'label': 'Reset', 'value': 'Reset'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'}
    ),
    dt.DataTable(
        id='datatable-id',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        filter_action='native',
        sort_action='native',
        sort_mode='multi',
        row_selectable='single',
        page_action='native',
        page_current=0,
        page_size=10,

    ),
    html.Br(),
    html.Hr(),
    
    #Chart & Map
    html.Div(className='row',
             style={'display': 'flex'},
             children=[
                 html.Div([dcc.Graph(id="pie-chart")]),
                 html.Div([
                     dl.Map(id='map-id', className='col s12 m6', style={'width': '1000px', 'height': '500px'}, center=[30.75, -97.48], zoom=10, children=[
                         dl.TileLayer(id="base-layer-id"),
                         
                         #Marker,tool tip & popup
                         dl.Marker(position=[30.75, -97.48], children=[

                             dl.Tooltip(df.iloc[0, 4]),
                             dl.Popup([
                                 html.H1("Animal Name"),
                                 html.P(df.iloc[1, 1])

                             ])

                         ])
                     ])

                 ]),
             ])
])

#############################################
#Interaction Between Components / Controller
#############################################

@app.callback(
    Output('map-id', "children"),
    [Input('datatable-id', "derived_virtual_data"),
     Input('datatable-id', "derived_virtual_selected_rows")])

def update_graphs(rows, derived_virtual_selected_rows):

    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = df if rows is None else pd.DataFrame(rows)

    try:
        row = derived_virtual_selected_rows[0]        
    except:
        row = 0

    try:
        return [
            dl.Map(style={'width': '1000px', 'height': '500px'}, center=[float(dff.iloc[row, 13]), float(dff.iloc[row, 14])], zoom=10, children=[
                dl.TileLayer(id="base-layer-id"),
                # Marker with tool tip and popup
                dl.Marker(position=[float(dff.iloc[row, 13]), float(dff.iloc[row, 14])], children=[
                    dl.Tooltip(dff.iloc[1, 4]),
                    dl.Popup([html.H1("Animal Name"), html.P(dff.iloc[row, 9])
                              ])
                ])
            ])
        ]
    
    except Exception as e:
        print(e)
        pass


@app.callback(
    Output("pie-chart", "figure"), 
    [Input('datatable-id', "derived_virtual_data"),
     Input('datatable-id', "derived_virtual_selected_rows")])

def generate_chart(names, values):
    fig = px.pie(df3, lables='labels', vales='values')
    return fig


app.run_server()

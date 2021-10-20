# from jupyter_plotly_dash import JupyterDash

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
# from pymongo import MongoClient
# from bson.json_util import dumps

#### FIX ME #####
# change animal_shelter and AnimalShelter to match your CRUD Python module file name and class name
# from animal_shelter import AnimalShelter


###########################
# Data Manipulation / Model
###########################
# FIX ME change for your username and password and CRUD Python module name
# username = "accuser"
# password = "changeme"
# shelter = AnimalShelter(username, password)



labels = ['Labrador Retriever Mix','Basset Hound','Australian Cattle Dog Mix','Siberian Husky Mix']
values = [4500, 2500, 1053, 500]



# class read method must support return of cursor object
# df = pd.DataFrame.from_records(shelter.read({})
df = pd.read_csv('Austin_Animal_Center_Outcomes.csv')
df2 = px.data.tips()


#########################
# Dashboard Layout / View
#########################
app = dash.Dash(__name__)

# FIX ME Add in Grazioso Salvare’s logo
image_filename = 'my-image.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

# FIX ME Place the HTML image tag in the line below into the app.layout code according to your design
# FIX ME Also remember to include a unique identifier such as your name or date
# html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))

app.layout = html.Div([
    #    html.Div(id='hidden-div', style={'display':'none'}),
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
    html.Center(html.B(html.H1('SNHU CS-340 Dashboard'))),
    html.Hr(),
    html.Div(

        # FIXME Add in code for the interactive filtering options. For example, Radio buttons, drop down, checkboxes, etc.


    ),
    html.Hr(),
    dcc.RadioItems(
        id='dogtype',
        options=[
            {'label': 'Water Rescue', 'value': 'Water'},
            {'label': 'Mountian Rescue', 'value': 'Mountian'},
            {'label': 'Disaster Rescue', 'value': 'Disaster'},
            {'label': 'None', 'value': 'None'}
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
    # This sets up the dashboard so that your chart and your geolocation chart are side-by-side
    html.Div(className='row',
             style={'display': 'flex'},
             children=[
                 html.Div([dcc.Graph(id="pie-chart")]),
                 html.Div([
                     dl.Map(id='map-id', className='col s12 m6', style={'width': '1000px', 'height': '500px'}, center=[30.75, -97.48], zoom=10, children=[
                         dl.TileLayer(id="base-layer-id"),
                         # Marker with tool tip and popup
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
# Interaction Between Components / Controller
#############################################


# @ app.callback([Output('datatable-id', 'data'),
#                 Output('datatable-id', 'columns')],
#                [Input('filter-type', 'value')])
# def update_dashboard(filter_type):
#     # FIX ME Add code to filter interactive data table with MongoDB queries

#     columns = [{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns]
#     data = df.to_dict('records')

#     return (data, columns)


# @ app.callback(
#     Output('datatable-id', 'style_data_conditional'),
#     [Input('datatable-id', 'selected_columns')]
# )
# def update_styles(selected_columns):
#     return [{
#         'if': {'column_id': i},
#         'background_color': '#D2F3FF'
#     } for i in selected_columns]


# @ app.callback(
#     Output('graph-id', "children"),
#     [Input('datatable-id', "derived_viewport_data")])
# def update_graphs(viewData):
#     ###FIX ME ####
#     # add code for chart of your choice (e.g. pie chart) #
#     # return [
#     #    dcc.Graph(
#     #        figure = ###
#     #    )
#     #]

# @app.callback(Output('datatable-id', 'style_data_conditional'),
#               [Input('datatable-id', 'selected_rows')])
# def update_styles(selected_rows):
#     return [{'if': {'derived_virtual_selected_row_ids': i}, 'background_color': '#D2F3FF'} for i in selected_rows]


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
    fig = px.pie(labels=labels, values=values)
    return fig


app.run_server()

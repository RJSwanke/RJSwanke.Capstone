## Databases (CS-340: Advanced Programming Concepts)

[Dashboard: Pre-Enhancements](https://github.com/RJSwanke/RJSwanke.github.io/tree/main/Dashboard%20-%20Pre-Enhancement)
	
[Dashboard: Final](https://github.com/RJSwanke/RJSwanke.github.io/tree/main/Dashboard)

#### Artifact explanation:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The artifact from CS 340: Advanced Programming Concepts is a MongoDB client and user interface that allows users to access data about their business which in this case is an animal shelter. This project was written in Python and uses MongoDB.

#### Reason for inclusion in portfolio:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This project is a great project to display in my ePortfolio since it is a different language than Java, uses a database and is a full stack build. Python is a language that is quickly gaining popularity especially in the artificial intelligence world. Having a basic understanding of Python for me shows that I am a diversified programmer that isn't just locked to one language.

#### What the program does: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This program allows any user to store, change, updates, move and/or retrieve data from a database of their making. It also has other utilities like GPS and search options with a full interface. Below is an example of the radio buttons that were added and the update to the chart & map.

#### Changes:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The enhancements that I did to this project was to take out everything that isn't necessary as I had a lot of lines that were either hashtagged out or left over notes for when I was originally building the project. Then I added from bson.json_util import dumps & from animal_shelter import AnimalShelter to the top as those will both be used. Next I cleaned up the structure and added/cleaned up the comments making sure they are visible and easy to understand while still giving a full picture. I also checked to see if any loops could be adjusted or moved to be more optimal within the code but after reviewing it I believe that everything is how and where it is supposed to be. Finally, I made sure all the spacing was continuous and the same throughout the project to ensure it is easy to read.
```
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

```

![Screenshot (194)](https://user-images.githubusercontent.com/49452450/137618638-ed783840-d6bb-4a67-99ac-a70967ab105d.png)
![Screenshot (193)](https://user-images.githubusercontent.com/49452450/137618641-482b5b60-27ee-41a6-b826-54518668912f.png)

#### What I learned: 
This project taught me a lot by focuses on the understanding of how to develop and implement a fullstack. The knowledge I gained I have been able to apply to other projects. This is a fullstack build and was one of the first times I connected the front end to the back end and then to a database. This project taught me that sometimes trial and error is the only way to figure certain things out.  

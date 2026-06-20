from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        id="header"
    ),

    dcc.Graph(
        id="sales-graph"
    ),

    dcc.RadioItems(
        id="region-picker",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"}
        ],
        value="all"
    )
])

if __name__ == "__main__":
    app.run(debug=True)
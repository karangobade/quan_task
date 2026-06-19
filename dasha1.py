from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_output.csv")

df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "padding": "20px"
        }
    ),

    html.Div([
        html.Label(
            "Select Region:",
            style={"fontWeight": "bold", "fontSize": "18px"}
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        ),
    ], style={"padding": "20px"}),

    dcc.Graph(id="sales-graph")
],
style={
    "backgroundColor": "#f4f6f7",
    "padding": "20px",
    "fontFamily": "Arial"
})

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    sales = (
        filtered_df.groupby("date")["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = px.line(
        sales,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.title()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)
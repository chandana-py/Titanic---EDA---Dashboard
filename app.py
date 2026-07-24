from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# Create charts
fig1 = px.bar(df.groupby("Pclass")["Survived"].mean().reset_index(),x="Pclass",y="Survived",title="Survival Rate by Passenger Class")

fig2 = px.histogram( df, x="Age", nbins=20, title="Age Distribution")

fig3 = px.scatter(df,x = "Age", y="Fare",title = "Age vs Fare")

# Create dashboard
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Titanic EDA Dashboard"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure = fig3)
])

if __name__ == "__main__":
    app.run(debug=True)
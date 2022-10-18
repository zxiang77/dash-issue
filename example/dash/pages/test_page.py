from example.dash.components import h3
from dash import register_page
from dash import html


register_page(__name__, path='/', layout=h3.H3Test())

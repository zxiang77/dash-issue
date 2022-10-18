from dash import html
from dash import register_page


class TestComponent(html.Div):
	def __init__(self):
		super().__init__([html.H3('Test Title')])


register_page(__name__, layout=TestComponent(), path='/')

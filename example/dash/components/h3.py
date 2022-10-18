from dash import html

class H3Test(html.Div):
	def __init__(self):
		super().__init__([
			html.H3('Test H3 title')
		])

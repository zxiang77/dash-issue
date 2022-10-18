from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
	# without disabling hot reload, the server won't start.
	app.run_server(debug=True)

	# With dev_tools_hot_reload disabled, the server is expected
	# to start correctly.
    # app.run_server(debug=True, dev_tools_hot_reload=False)


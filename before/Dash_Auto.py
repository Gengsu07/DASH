from ast import Div
from tkinter import _Padding
from tkinter.tix import CheckList
from xml.dom.minidom import Childless
import pandas as pd
import dash 
from dash import dcc, html
import plotly.express as px
from sympy import div 

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str,
                                   'Div2Airport': str, 'Div2TailNum': str})


app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='US Domestic Airline Flights Performance',style={'color':'#503D36', 'font-size':24, 'textAlign':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.H2('Report Type:')
                ]),
            dcc.Dropdown(id='input-type',
                         options=[{'Yearly Airline Performance Report':'OPT1',
                                   'Yearly Airline Delay Report':'OPT2'}
                                  ],
                         placeholder='Select a report type',
                         style={'width':'80%', 'padding':'3px', 'font-size':'20px', 'textAlign':'center'})
            ], style={'display':'flex'})
        ]
             )
    html.Div([
        html.Div([
            html.Div([
                html.H2('Choose Year:')]
                     ),
            dcc.Dropdown(
            )])])

if __name__ == '__main__':
    app.run_server(debug=True)

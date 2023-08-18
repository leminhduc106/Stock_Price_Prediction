import pandas as pd
import numpy as np

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

app = dash.Dash()
server = app.server

ts = TimeSeries(key='G7PXOJDYOFRBJ826', output_format='pandas')
ti = TechIndicators(key='G7PXOJDYOFRBJ826', output_format='pandas')


df = pd.read_csv("../DATA/MSFT.csv")


app.layout = html.Div([
   
    html.H1("Stock Price Analysis", style={"textAlign": "center"}),
   
    dcc.Tabs(id="tabs", children=[
       
        dcc.Tab(label='Stock Data', children=[
            html.Div([
                
                html.Div([                
                    html.Button('Update', 
                     id='update_button', 
                     style={"background-color": "#5DADE2", "border": "none", "color": "white", 
                            "padding": "15px 32px", "text-align": "center", "text-decoration": "none", 
                            "display": "inline-block", "font-size": "16px", 
                            "margin-left": "auto", "margin-top": "10px", 
                            "margin-bottom": "10px", "margin-right": "auto", "width": "20%"})
                ], style={"text-align": "center"}),
                
                html.Div(id='something', children=''),
                
                html.H1("Stock Price", 
                        style={'textAlign': 'center'}),
              
                dcc.Dropdown(id='my-dropdown',
                             options=[{'label': 'Microsoft','value': 'MSFT'}], 
                             multi=True,
                             value=['MSFT'],
                             style={"display": "block", "margin-left": "auto", 
                                    "margin-right": "auto", "width": "60%"}),
                
                dcc.Graph(id='stockprice'),
                
                
                html.H1("Stock Market Volume", style={'textAlign': 'center'}),
         
                dcc.Dropdown(id='my-dropdown2',
                             options=[{'label': 'Microsoft','value': 'MSFT'}], 
                             multi=True,
                             value=['MSFT'],
                             style={"display": "block", "margin-left": "auto", 
                                    "margin-right": "auto", "width": "60%"}),
                dcc.Graph(id='volume')
                
            ], className="container"),
        ]),
        
        
        dcc.Tab(label='Stock Prediction',children=[
            html.Div([
                
                dcc.Dropdown(id='dropdown-company',
                     options=[{'label': 'Microsoft','value': 'MSFT'}], 
                     multi=False, placeholder="Choose company",value='MSFT',
                     style={"margin-left": "auto", "margin-top": "10px", "margin-bottom": "10px",
                            "margin-right": "auto", "width": "80%"}),
                
                dcc.Dropdown(id='dropdown-model',
                     options=[{'label': 'Extreme Gradient Boosting (XGBOOST)', 'value': 'XGBOOST'},
                              {'label': 'Recurrent Neural Network (RNN)','value': 'RNN'}, 
                              {'label': 'Long Short Term Memory (LSTM)', 'value': 'LSTM'}], 
                     multi=False, placeholder="Choose model",value='LSTM',
                     style={"margin-left": "auto", "margin-top": "10px", "margin-bottom": "10px",
                            "margin-right": "auto", "width": "80%"}),
                
                dcc.Dropdown(id='dropdown-period',
                     options=[{'label': '15 minutes', 'value': 15}], 
                     multi=False, placeholder="Choose time period",value=15,
                     style={"margin-left": "auto", "margin-top": "10px", "margin-bottom": "10px",
                            "margin-right": "auto", "width": "80%"}),
  
                dcc.Dropdown(id='dropdown-indicator',
                     options=[{'label': 'Close Price','value': 'close'},
                              {'label': 'Price Rate of Change (ROC)','value': 'ROC'}, 
                              {'label': 'Relative Strength Index (RSI)', 'value': 'RSI'}, 
                              {'label': 'Simple Moving Averages (SMA)', 'value': 'SMA'},
                              {'label': 'Bolling Bands', 'value': 'KBANDS'}], 
                     multi=True, placeholder="Choose indicators",value=['close'],
                     style={"margin-left": "auto", "margin-top": "10px", "margin-bottom": "10px",
                            "margin-right": "auto", "width": "80%"}),
                
                html.Div([                
                    html.Button('Predict', 
                     id='predict_button', 
                     style={"background-color": "#5DADE2", "border": "none", "color": "white", 
                            "padding": "15px 32px", "text-align": "center", "text-decoration": "none", 
                            "display": "inline-block", "font-size": "16px", 
                            "margin-left": "auto", "margin-top": "10px", 
                            "margin-bottom": "10px", "margin-right": "auto", "width": "20%"})
                ], style={"text-align": "center"}),

                dcc.Graph(id='predicted_graph')
                
            ])                

        ])


    ])
])

app.run_server(debug=True, port=8080)
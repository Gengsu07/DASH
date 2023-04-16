from fileinput import filename
from statistics import mode
from matplotlib import markers
import pandas as pd
from pandas.core import groupby
from sqlalchemy import create_engine
import plotly.graph_objs  as go
import plotly.offline as po
from sympy import symbols

superstore = pd.read_excel('superstore.xls',parse_dates=['Ship Date', 'Order Date'])

scat = go.Scatter(x=superstore['Discount']
                ,y=superstore['Profit']
                ,mode='markers',
                marker = dict(
                    size = 12,
                    color = 'rgb(24,67,90)',
                    symbol = 'star-diamond'
                ))

scat1 = go.Scatter(x=superstore['Discount']
                ,y=superstore['Profit']*- 1,
                mode = 'lines',name = 'below'
                )

scat2 = go.Scatter(x=superstore['Discount']
                ,y=superstore['Profit'],
                mode = 'lines',name = 'above'
                )

# Multi Chart masukkan ke list
data = [scat,scat1,scat2]
layout = go.Layout(title = 'First Dash Plotly Chart', 
                    xaxis = {'title':'Diskon'}, 
                    yaxis = dict(title = 'Profit'))

fig = go.Figure(data= data, layout=layout)
po.plot(fig,filename='scatter.html')


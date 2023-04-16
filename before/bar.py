from fileinput import filename
from statistics import mode
from turtle import color
from matplotlib import markers
import pandas as pd
from pandas.core import groupby
from sqlalchemy import create_engine
import plotly.graph_objs  as go
import plotly.offline as po
from sympy import symbols

superstore = pd.read_excel('superstore.xls',parse_dates=['Ship Date', 'Order Date'])
bardata = superstore.filter(['State','Quantity','Sales','Profit']).groupby('State').sum().reset_index()

bar = go.Bar(x=bardata['State'], y=bardata['Profit'],
                name = 'Profit', marker = {'color':'#39aea9'})

bar1 = go.Bar(y = bardata['State'], x= bardata['Sales'],
                name = 'Sales', marker = {'color':'#557b83'}, orientation = 'h')

bar2 = go.Bar(x = bardata['State'],y = bardata['Sales'],
                name = 'Sales', marker = {'color':'#557b83'})

# Multi Chart masukkan ke list
data = [bar,bar2]
layout = go.Layout(title = 'Superstore Sales by State')
stack_layout = go.Layout(title = 'Superstore Sales by State',barmode='stack')

nested = go.Figure(data= data, layout=layout)
stack = go.Figure(data=data, layout=stack_layout)
horisontal = go.Figure(data=[bar1],layout=layout)

# fig = go.Figure(go.Bar(x = bardata['State'],y = bardata['Sales'],
#                 name = 'Sales', marker = {'color':'#557b83'})
#                 )
# fig.show()

po.plot(nested,filename='bar_nested.html')
po.plot(stack, filename='bar_stack.html')
po.plot(horisontal, filename='bar_horizontal.html')

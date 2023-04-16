from fileinput import filename
from statistics import mode
from matplotlib import axis, markers
import pandas as pd
from pandas.core import groupby
from sqlalchemy import create_engine
import plotly.graph_objs  as go
import plotly.offline as po
from sympy import symbols
import plotly.express as px

superstore = pd.read_excel('superstore.xls',parse_dates=['Ship Date', 'Order Date'])

line_data = superstore.filter(['Order Date','Profit'])

line_data['Order Date'] = line_data['Order Date'].dt.month_name()
line_data= line_data.groupby('Order Date').sum().reset_index()
line_data.set_index('Order Date',inplace=True)

new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
line_data = line_data.reindex(new_order, axis=0)

line = px.line(line_data,x=line_data.index,y='Profit', title='Line With Plotly Express')
po.plot(line,filename='line.html')


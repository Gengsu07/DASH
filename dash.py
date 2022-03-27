from fileinput import filename
from statistics import mode
from matplotlib import markers
import pandas as pd
from pandas.core import groupby
from sqlalchemy import create_engine
import plotly.graph_objs  as go
import plotly.offline as po

# conn =create_engine('postgresql://postgres:sgwi2341@10.4.19.215/penerimaan')

# query_mpnspm = '''select "KDMAP","DATEBAYAR",sum("JUMLAH") as Nominal 
# from appportal.mpnspm_2022
# group by "KDMAP","DATEBAYAR"
# '''
superstore = pd.read_excel('superstore.xls')

scat = [go.Scatter(x=superstore['Discount']
                ,y=superstore['Profit']
                ,mode='markers')
]
layout = go.Layout(title = 'First Dash Plotly Chart', 
                    xaxis = {'title':'Diskon'}, 
                    yaxis = dict(title = 'Profit'))

fig = go.Figure(data= scat, layout=layout)
po.plot(fig,filename='scatter.html')


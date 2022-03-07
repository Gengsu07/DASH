import pandas as pd
from pandas.core import groupby
from sqlalchemy import create_engine
import plotly.graph_objs  as go

conn =create_engine('postgresql://postgres:sgwi2341@10.4.19.215/penerimaan')

query_mpnspm = '''select "KDMAP","DATEBAYAR",sum("JUMLAH") as Nominal 
from appportal.mpnspm_2022
group by "KDMAP","DATEBAYAR"
'''

mpnspm = pd.read_sql(query_mpnspm,con=conn)
mpnspm.head()



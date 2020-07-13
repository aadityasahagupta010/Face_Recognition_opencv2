from pandas_datareader import data
import datetime
from bokeh.plotting import figure,show,output_file
start_date=datetime.datetime(2020,4,1)
end_date=datetime.datetime(2020,4,19)
df=data.DataReader(name="GOOG",data_source="yahoo",start=start_date,end=end_date)
df
p=figure(x_axis_type='datetime',width=1000,height=3000)
p.title.text="CandleStickChart"
time_calc=12*60*60*1000
p.rect=(df.index[df.Close>df.Open],(df.Open+df.Close)/2,time_calc,abs(df.Open-df.Close))
output_file("CS.html")
show(p)

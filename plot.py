import pandas
from bokeh.plotting import figure,output_file,show
df=pandas.read_csv("Sample_of_the_produced_time_values.csv")
"""
print(df["Start"])
print(df["End"])
"""
plot = figure(px_axis_type)
plot.quad(top=1, bottom=1, left=df["Start"],
          right=df["End"], color="#B3DE69")
output_file("mt.html")
show(plot)

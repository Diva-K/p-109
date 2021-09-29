import statistics 
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
score_list=df["math score"].to_list()
mean=sum(score_list)/len(score_list)
median=statistics.median(score_list)
mode=statistics.mode(score_list)
standard_deviation=statistics.stdev(score_list)
print("mean is",mean)
print ("median is", median)
print("mode is", mode)
print("standard deviation is", standard_deviation)

fig=ff.create_distplot([score_list],["result"],show_hist=False)

first_sd_start,first_sd_end=mean-standard_deviation, mean+standard_deviation
second_sd_start,second_sd_end=mean-(2*standard_deviation), mean+(2*standard_deviation)
third_sd_start,third_sd_end=mean-(3*standard_deviation), mean+(3*standard_deviation)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="first_sd_start"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="first_sd_end"))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="second_sd_start"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="second_sd_end"))

fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.17],mode="lines",name="third_sd_start"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="third_sd_end"))
fig.show()
list_within_1_sd=[result for result in score_list if result>first_sd_start and result<first_sd_end]
list_within_2_sd=[result for result in score_list if result>second_sd_start and result<second_sd_end]
list_within_3_sd=[result for result in score_list if result>third_sd_start and result<third_sd_end]
print("percentage of data within one sd",len(list_within_1_sd)*100/len(score_list))
print("percentage of data within two sd",len(list_within_2_sd)*100/len(score_list))
print("percentage of data within three sd",len(list_within_3_sd)*100/len(score_list))

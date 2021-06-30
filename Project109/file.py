import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

data=pd.read_csv("StudentsPerformance.csv")
pf=data["math score"].tolist()

mean=int(sum(pf)/len(pf))
med=statistics.median(pf)
mode=statistics.mode(pf)
deviation=statistics.stdev(pf)

stdevstart1=mean-deviation
stdevend1=mean+deviation
devation2=mean-2*deviation
stdevstart2=mean-2*deviation
stdevend2=mean+2*deviation
stdevstart3=mean-3*deviation
stdevend3=mean+3*deviation

data1=[result for result in pf if result>stdevstart1 and result<stdevend1]
percentage=len(data1)*100/len(pf)

data2=[result for result in pf if result>stdevstart2 and result<stdevend2]
percentage2=len(data2)*100/len(pf)

data3=[result for result in pf if result>stdevstart3 and result<stdevend3]
percentage3=len(data3)*100/len(pf)

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(med))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(deviation))

print("{} per cent of the data lies within the first standard deviation.".format(percentage))
print("{} per cent of the data lies within the second standard deviation.".format(percentage2))
print("{} per cent of the data lies within the third standard deviation.".format(percentage3))

#fig=px.bar(x=allSum,y=count)
fig=ff.create_distplot([pf],['scores'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.16],mode='lines',name="mean"))
fig.add_trace(go.Scatter(x=[stdevstart1,stdevstart1],y=[0,0.16],mode='lines',name="stdev 1"))
fig.add_trace(go.Scatter(x=[stdevend1,stdevend1],y=[0,0.16],mode='lines',name="stdev 1"))
fig.add_trace(go.Scatter(x=[stdevstart2,stdevstart2],y=[0,0.16],mode='lines',name="stdev 2"))
fig.add_trace(go.Scatter(x=[stdevend2,stdevend2],y=[0,0.16],mode='lines',name="stdev 2"))
fig.add_trace(go.Scatter(x=[stdevstart3,stdevstart3],y=[0,0.16],mode='lines',name="stdev 3"))
fig.add_trace(go.Scatter(x=[stdevend3,stdevend3],y=[0,0.16],mode='lines',name="stdev 3"))
fig.show()
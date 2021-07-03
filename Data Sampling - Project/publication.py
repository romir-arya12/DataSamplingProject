import pandas as pd
import csv
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
fig=ff.create_distplot([data],["reading_time"], show_hist=False)
fig.show()
stdev=statistics.stdev(data)
print(population_mean)
print(stdev)
#dataSet=[]
#for i in range(0,100):
    #random_index=random.randint(0,len(data))
    #value=data[random_index]
    #dataSet.append(value)
#mean=statistics.mean(dataSet)
#stdev=statistics.stdev(dataSet)
#print(mean)
#print(stdev)
def randomSetOfMeans(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()
def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans=randomSetOfMeans(30)
        mean_list.append(setOfMeans)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("mean of the sampling distribution",mean)
setup()
def stdev_():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans=randomSetOfMeans(30)
        mean_list.append(setOfMeans)
    stdev=statistics.stdev(mean_list)
    print("standard devation of the sampling",stdev)
stdev_()
from pdb import Pdb
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
population_data = df["reading_time"].tolist()


population_mean = statistics.mean(population_data)
print("Population Mean :",population_mean)

def random_set_of_mean(counter) :
    random_data_list =[]
    for i in range(0,counter) :
        random_index = random.randint(0,len(population_data)-1)
        value = population_data[random_index]
        random_data_list.append(value)
    mean = statistics.mean(random_data_list)
    return mean

def show_fig(mean_list,mean,sd) :

    first_sd_start , first_sd_end = mean-sd , mean+sd
    second_sd_start , second_sd_end = mean-2*sd , mean+2*sd
    third_sd_start , third_sd_end = mean-3*sd , mean+3*sd

    df1 = pd.read_csv("intervention_data.csv")
    intervention_data = df1["reading_time"].tolist()
    new_sample_mean = statistics.mean(intervention_data)
    print("New Sample Mean :",new_sample_mean)

    z_score = (new_sample_mean-mean)/sd
    print("Z SCORE :",z_score)

    d_f = mean_list
    fig = ff.create_distplot([d_f],["Means"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.7],mode = "lines",name="Mean"))
    fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.7],mode = "lines",name="1st Standard Deviation Start"))
    fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.7],mode = "lines",name="1st Standard Deviation End"))
    fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.7],mode = "lines",name="2nd Standard Deviation End"))
    fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.7],mode = "lines",name="2nd Standard Deviation Start"))
    fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.7],mode = "lines",name="3rd Standard Deviation End"))
    fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.7],mode = "lines",name="3rd Standard Deviation Start"))
    fig.add_trace(go.Scatter(x=[new_sample_mean,new_sample_mean],y=[0,0.7],mode = "lines",name="New Sample Mean"))
    
    #print("inside show fig")
    fig.show()


def setup() :
    mean_list = []
    for i in range(0,100) :
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    sample_mean = statistics.mean(mean_list)
    sample_sd = statistics.stdev(mean_list)
    #print(set_of_means)
    print("Sampling Mean :",sample_mean)
    print("Sampling Standard Deviation :",sample_sd)
    show_fig(mean_list=mean_list,mean=sample_mean,sd=sample_sd)


setup()


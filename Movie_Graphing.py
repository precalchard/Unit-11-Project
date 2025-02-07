import pandas
import matplotlib.pyplot as plot

graph = pandas.read_csv("Movie_Data.csv")

def avg(col):
    total = sum(col)/len(col)
    return total
print(f"The avreage run time for the top 250 movies is {avg(graph["run_time"])} minutes.")

#graph.plot(x="year", y="rank", m="rating")

plot.savefig("Graph_attempt_1.png") 
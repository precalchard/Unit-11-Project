import pandas
import statistics as stat
import matplotlib.pyplot as plot

graph = pandas.read_csv("Movie_Data.csv")

def avg(col):
    total = sum(col)/len(col)
    return total
def most_common(col):
    return stat.mode(col)

print(f"The avreage run time for the top 250 movies is {avg(graph["run_time"])} minutes.")
print(f"The most common age rating for the top 250 movies is {most_common(graph["age_rating"])}.")

graph.plot.scatter(x="year", y="rating")

plot.savefig("Graph_attempt_1.png")
import pandas
import statistics as stat
import seaborn
import matplotlib.pyplot as plot

graph = pandas.read_csv("Movie_Data.csv")

def avg(col):
    '''
    Calculates the avreage for a specific topic within my dataset
    '''
    total = sum(col)/len(col)
    return total
def most_common(col):
    '''
    Calculates the mode for a specific topic within my dataset
    '''
    return stat.mode(col)

print(f"The avreage run time for the top 250 movies is {avg(graph["run_time"])} minutes.")
print(f"The most common age rating for the top 250 movies is {most_common(graph["age_rating"])}.")

graph.plot.scatter(x="year", y="rating")
# Used this graph to find the quality of movies over time.
plot.xlabel("Years")
plot.ylabel("Ratings")
plot.title("Movie Ratings over Time")
plot.savefig("Movies_Time.png")


seaborn.kdeplot(x=graph["run_time"], y=graph["rating"], fill=True)
# Used this graph to find wether or not the age_rating has an effect on the rating of a movie.
plot.xlabel("run time in mins.")
plot.ylabel("ratings")
plot.xlim(0, 300)
plot.title("Movie ratings affected by run time.")
plot.savefig("Movies_run_time.png")
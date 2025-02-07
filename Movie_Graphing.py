#age_rating is ranked, so Passed = -2,Not Rated = -1, G=0, PG= 1, PG-13=2, etc. 

import pandas
import numpy as np
import matplotlib.pyplot as plot

avg_runtime = np.mean("run_time")
print(avg_runtime)

graph = pandas.read_csv("Movie_Data.csv")

graph.plot(x="year", y="rank", m="rating")

plot.savefig("Graph_attempt_1.png") 
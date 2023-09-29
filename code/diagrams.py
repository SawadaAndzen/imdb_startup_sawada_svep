from dataframe import*
import pandas
import math
import plotly.express as exp

#друга гіпотеза: чи залежить режисер(Director) фільму на голоси(Votes)?
'''dataframe = dataframe.sort_values(by="Votes")
dataframe = dataframe.head(10)
dv = exp.bar(dataframe, x="Director", y="Votes", title="DirectorVotes")
dv.show()'''

#третє: скільки заробив 3 найбільш довготривалі фільми в IMDb?
'''dataframe = dataframe.sort_values(by="Runtime (Minutes)")
dataframe = dataframe.tail(3)
rr = exp.pie(dataframe, names = "Runtime (Minutes)", values = "Revenue (Millions)", title="MostRuntimeRevenue")
rr.show()'''

#Четверте: топ 3 найпопулярніших фільмів 2016 року
'''dataframe = dataframe.sort_values(by="Rating")
dataframe = dataframe[dataframe["Year"] == 2016]
dataframe = dataframe.tail(3)
ry = exp.bar(dataframe, x="Title", y="Rating", title="Top-3 most pupular films 2016")
ry.show()'''
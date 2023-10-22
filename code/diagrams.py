from dataframe import*
import plotly.express as exp

# #перше: який жанр бiльш заробляе?
df = dataframe
df = df[df["Revenue (Millions)"] > 400]

df = df.sort_values(by="Genre")
fig = exp.line(df, y="Revenue (Millions)", x="Genre")
fig.show()
#
# #друга гіпотеза: чи залежить режисер(Director) фільму на голоси(Votes)?
df = dataframe.head(10)
df = df.sort_values(by="Votes")
dv = exp.bar(df, x="Director", y="Votes", title="DirectorVotes")
dv.show()
#
# #третє: скільки заробив 3 найбільш довготривалі фільми в IMDb?
df = dataframe.sort_values(by="Runtime (Minutes)")
df = df.tail(4)
rr = exp.pie(df, names = "Runtime (Minutes)", values = "Revenue (Millions)", title="MostRuntimeRevenue")
rr.show()
#
# #Четверте: топ 3 найпопулярніших фільмів 2016 року
df = dataframe.sort_values(by="Rating")
df = df[df["Year"] == 2016]
df = df.tail(3)
ry = exp.bar(df, x="Title", y="Rating", title="Top-3 most pupular films 2016")
ry.show()

# П'яте: топ-3 найпопулярніших фільмів режисера Peter Berg.
df = dataframe[dataframe["Director"] == "Peter Berg"]
df = df.sort_values(by="Rating")
a = exp.bar(df.tail(3), y="Rating", x="Title", title="топ-3 найпопулярніших фільмів режисера Peter Berg")
a.update_traces(marker_color='green')
a.show()

# Шосте: актори 5 найнепопулярніших фільмів 2008 року.
df = dataframe[dataframe["Year"] == 2008]
df = df.sort_values(by="Rating")
b = exp.line(df.head(5), x="Actors", y="Rating", title="Актори 5 найнепопулярніших фільмів 2008 року.")
b.update_traces(line_color='#a450d9', line_width=5)
b.show()

import pandas
import math

file = pandas.read_csv("csv/IMDB-Movie-Data.csv")
check = file.isnull().sum() #checking NaN values
cleared = file.dropna() #clearing file for NaN values
dataframe = cleared.head(10)
#dataframe = cleared[cleared["Revenue (Millions)"] > 400]
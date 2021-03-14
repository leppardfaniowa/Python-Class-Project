import datetime as dt
import pandas as pd

#import CSV from project github
covid19Dataframe = pd.read_csv("https://raw.githubusercontent.com/WhipSnake23/Python-Class-Project/main/Data/owid-covid-data.csv")

#scrub data from rolled up rows for each region globally. NOTE: ~=="not"
covid19Dataframe = covid19Dataframe[~covid19Dataframe.iso_code.str.contains("OWID")]

#Create column for day, month, year. This makes it easier to aggregate
covid19Dataframe.insert(59,'Day',pd.to_datetime(covid19Dataframe['date']),True)
covid19Dataframe.insert(60,'Month',pd.to_datetime(covid19Dataframe['date']),True)
covid19Dataframe.insert(61,'Year',pd.to_datetime(covid19Dataframe['date']),True)
covid19Dataframe['Day'] = covid19Dataframe['Day'].dt.year
covid19Dataframe['Month'] = covid19Dataframe['Month'].dt.month
covid19Dataframe['Year'] = covid19Dataframe['Year'].dt.year

#ACTION ITEM: Create function that outputs the worst 5 or best 5 for a given metric
#EXAMPLE Code:(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))
countries = covid19Dataframe[['iso_code','population']]
countries = countries.drop_duplicates()
top5Countries_population = countries.nlargest(5,'population')
top5Countries_list = top5Countries_population['iso_code'].values.tolist()
booleanSeries = covid19Dataframe.iso_code.isin(top5Countries_list)
print(covid19Dataframe[booleanSeries])


#population_density
#new_deaths_smoothed

#print(covid19Dataframe.info(verbose=True))
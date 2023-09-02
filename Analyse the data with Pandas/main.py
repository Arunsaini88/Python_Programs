import pandas


data = pandas.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
gray_squirrel_count = len(data[data["Primary Fur Color"] == 'Gray'])
red_squirrel_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_squirrel_count = len(data[data["Primary Fur Color"] == 'Black'])
data_dict = {
    "Fun color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
print(df)
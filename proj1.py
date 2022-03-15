import pandas as pd

# Takes the file's folder
filepath = r"C:\Users\lenovo\Downloads\crime.csv"

# read the CSV file
df = pd.read_csv(filepath)

# print the first five rows
#print(df)
#drop unnecessary columns
df1 = df.drop(['OFFENSE_TYPE_ID', 'LAST_OCCURRENCE_DATE', 'LAST_OCCURRENCE_DATE' ,'GEO_X' ,'GEO_Y', 'IS_CRIME', 'IS_TRAFFIC'], axis=1)
print(df1)
#df1 = df.dropna(axis=1)
#print(df1)
#start one hot encoding
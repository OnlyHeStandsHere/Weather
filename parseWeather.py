import json
import pyodbc
import os


# first open our json weather data
try:
    fileName = 'vancouverweather.json' #'C:\\Users\\jmaitland\\Source\\Repos\\VesselPrediction\\DataParsing\\vancouverweather.json'
    file = open(fileName)
    sfile = file.read()
except FileNotFoundError:
    print("The file {} could not be found".format(fileName))
    exit()

# next we'll create a dictionary out of the jason weather data
# this resulting object will be a list of dictionaries accessable with the following
# loop structure
# for r in weather_json:
#     for k, v in r.items():
#         print(k, v)
weather_json = json.loads(sfile)

def get_cityID(weather_record):
    try:
        city_id = weather_record['city_id']
        return city_id
    except KeyError:
        return 0




# set up a DB Connection
con = pyodbc.connect('Trusted_Connection=yes', driver='{ODBC Driver 13 for SQL Server}', server='localhost',
                     database='Weather')

query = 'select * from album'
cursor = con.cursor()
cursor.execute(query)
rows = cursor.fetchall()

print(rows)


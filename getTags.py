from sql_to_csv import SqlToCsv


con_str = 'DRIVER={ODBC Driver 13 for SQL Server}; server=NBTVMDW01; database=NBT-DW-InTest; Trusted_Connection=yes'

sql = SqlToCsv(con_str)

query = "select * from tag"

file = 'Data/tags.csv'

sql.dump_sql(file_name=file, query=query, include_header=True)
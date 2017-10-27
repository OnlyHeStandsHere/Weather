from sql_to_csv import SqlToCsv
from datetime import datetime, timedelta


def get_connection_string():
    return 'DRIVER={ODBC Driver 13 for SQL Server}; server=localhost; database=Chinook; Trusted_Connection=yes'


def get_filesafe_date(datetimeObj):
    return datetimeObj.strftime('%Y_%m_%d_%H_%M_%S')


def get_sql_date(datetimeObj):
    return datetimeObj.strftime('%Y-%m-%d %H:%M:%S')


def get_query_writer():
    return SqlToCsv(get_connection_string())


def get_query(date_start, date_end):
    sql_date_start = get_sql_date(date_start)
    sql_date_end = get_sql_date(date_end)

    return 'SELECT ID, DateTime, TagID, Value, ValueText ' \
           'FROM Eventhist ' \
           'WHERE DateTime BETWEEN {} AND {} ' \
           'ORDER BY DateTime ASC'.format(sql_date_start, sql_date_end)


def get_file_name(path, table, start_date, end_date):
    return '{}\{}-{}-to-{}.csv'.format(path, table, get_filesafe_date(start_date), get_filesafe_date(end_date))

if __name__ == '__main__':

    # get our start and end times
    start_date = datetime.now()
    end_date = start_date + timedelta(days=5)

    # get the file names
    file = get_file_name('Data', 'EH', start_date, end_date)

    #open a query writer and make a csv file
    query_writer = get_query_writer()
    query = "SELECT * FROM Tag"
    query_writer.dump_sql(file, query)

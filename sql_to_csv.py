import csv
import pyodbc
import sys


class SqlToCsv():

    def __init__(self, con_str):
        self.con_str = con_str
        self.log = open("log.txt", 'w')

    def write_log(self, line):
        self.log.writelines(line)

    def dump_sql(self, file_name, query, include_header=False):

        try:
            cursor = pyodbc.connect(self.con_str).cursor()
        except pyodbc.Error:
            self.write_log("error establishing database connection {} \n".format(sys.exc_info()))
            self.write_log("for query {} and filename {}. include_header={} \n".format(query, file_name, str(include_header)))
            return None

        try:
            results = cursor.execute(query).fetchall()
            with open(file_name, 'w') as csvFile:
                writer = csv.writer(csvFile, dialect='excel' ,lineterminator='\n')
                writer.writerows(results)
        except Exception:
            self.write_log("An error occured creating csv file {}".format(sys.exc_info()))

    def close_log(self):
        self.log.close()

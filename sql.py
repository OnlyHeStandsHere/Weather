class Sql():

    def __init__(self):
        pass

    def get_insert(self, table_name, columns):
        cols = str(columns).strip("[]").replace("'", '')
        params = ''
        for i in range(0, len(columns)):
            if i == len(columns) - 1:
                params = params + '?'
            else:
                params = '?, ' + params
        return "INSERT INTO {} ({}) VALUES ({})".format(table_name, cols, params)

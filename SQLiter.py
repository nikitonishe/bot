import sqlite3
class SQLiter:

    def __init__(self, data_base_name):
        self.con = sqlite3.connect("database/"+data_base_name)
        self.cur = self.con.cursor()

    def get_info(self, table_name):
        return self.cur.execute("SELECT * FROM %s" % table_name).fetchall()

    def get_info_by_id(self, table_name, id):
        return self.cur.execute("SELECT * FROM %s WHERE id = %i" % (table_name,id)).fetchall()

    def get_quantity_of_rows(self, table_name):
        return len(self.cur.execute("SELECT * FROM %s" % table_name).fetchall())

    def close(self):
        self.con.close()

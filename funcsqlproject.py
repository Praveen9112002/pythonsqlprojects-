import sqlite3
table_name='data'
db_name='clgmanagement.db'
c=sqlite3.connect(db_name)
curser = c.cursor()

def get_data():
    print("get the table datas")
    a=curser.execute(f"SELECT* FROM {table_name}")
    print([x for x in a])
    # print(a)
def insert_data(column,value):
    curser.execute(f"INSERT INTO {table_name} {column} VALUES {value}")
    c.commit()
def update_data(key,value,condition):
    curser.execute(f"""UPDATE {table_name} SET "{key}"="{value}" WHERE {condition}""")

key = "department"
value="ECE"
condition = """ "id" = "5" """
# column=('id','name','department','roll_number')
# value=(5,'dinesh','E&I',15)
update_data(key,value,condition)
get_data()   
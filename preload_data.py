import psycopg2

print('File execution started')

postgre_file = open('postgre_data_load.sql')
postgre_file_data = postgre_file.readlines()

print('File execution finished')

conn = psycopg2.connect(
    database="postgres", user='postgres',
    password='1234', host='localhost', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

print('Statement execution started')

for sql_statement in postgre_file_data:
    if sql_statement == '':
        pass
    cursor.execute(sql_statement)
    conn.commit()

print('Statement execution finished')

conn.close()


import config as c
import psycopg2
import pandas as pd


# Подключение к базе данных
connection = psycopg2.connect(
    host=c.host,
    port=c.port,
    user=c.username,
    password=c.password,
    database=c.database
)
print('Загрузка данных в raw-слой')


# Создание и наполнение таблицы слоя сырых данных
cur = connection.cursor()
query_create_schema = "CREATE SCHEMA IF NOT EXISTS result;"
cur.execute(query_create_schema)


#Создание таблицы raw_data со стобцами исходя их предоставленного файла csv
query_create = ("CREATE TABLE IF NOT EXISTS result.raw_data (vendorid BIGINT, tpep_pickup_datetime VARCHAR(50), "
                    "tpep_dropoff_datetime VARCHAR(50), passenger_count INT, trip_distance FLOAT, RatecodeID INT, "
                    "store_and_fwd_flag VARCHAR(8), PULocationID VARCHAR(8), DOLocationID VARCHAR(8), payment_type INT,"
                    "fare_amount FLOAT, extra FLOAT, mta_tax FLOAT, tip_amount FLOAT, tolls_amount FLOAT, "
                    "improvement_surcharge FLOAT, total_amount FLOAT, congestion_surcharge FLOAT);")
cur.execute(query_create)
connection.commit()
print("База создана")


#Копируем файл с данными службы такси в таблицу raw_data
cur.execute("ROLLBACK;")
cur.execute("COPY result.raw_data FROM '/init_db/data/yellow_tripdata_2020-01.csv' "
                "DELIMITER ',' ENCODING 'UTF8' CSV HEADER;")
connection.commit()
cur.close()

print("Данные в таблицу внесены")

# Создание и наполнение второй таблицы для последующей фильтрации данных и подготовки к выполениею задач
cur = connection.cursor()
query_create = ("CREATE TABLE IF NOT EXISTS result.core_data (date TIMESTAMP, passenger_count INT, trip_distance FLOAT," 
                    "tip_amount FLOAT, total_amount FLOAT);")
cur.execute(query_create)
connection.commit()
print("База создана")


#Создание таблицы с необходимыми для последующего анализа стобцами с учетом фильтрации от некорректных данных
cur.execute("ROLLBACK;")
insert_query = ("INSERT INTO result.core_data (date, passenger_count, trip_distance, tip_amount, total_amount) "
"(SELECT DATE(tpep_dropoff_datetime::timestamp), passenger_count, trip_distance, tip_amount, total_amount "
"FROM result.raw_data WHERE (passenger_count IS NOT NULL AND "
"trip_distance > 0 AND "
"tip_amount > 0 AND "
"total_amount > 0 ))")
cur.execute(insert_query)
connection.commit()
cur.close()

print('print("База создана")')

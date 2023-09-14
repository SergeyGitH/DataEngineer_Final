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
print('Подключение к базе успешно')
cur = connection.cursor()

create_table_query = """CREATE TABLE IF NOT EXISTS result.passengers_base(
date DATE,
percentage_zero FLOAT,
pecentage_1p FLOAT,
percentage_2p FLOAT,
percentage_3p FLOAT,
percentage_4p_plus FLOAT,
max_amount_perc_zero FLOAT,
min_amount_perc_zero FLOAT,
max_amount_perc_1p FLOAT,
min_amount_perc_1p FLOAT,
max_amount_perc_2p FLOAT,
min_amount_perc_2p FLOAT,
max_amount_perc_3p FLOAT,
min_amount_perc_3p FLOAT,
max_amount_perc_4p_plus FLOAT,
min_amount_perc_4p_plus FLOAT
);"""
cur.execute(create_table_query)

connection.commit()

print('Создание result.passengers_base данных завершено')

insert_data_query = """INSERT INTO result.passengers_base (
date,
percentage_zero,
pecentage_1p,
percentage_2p,
percentage_3p,
percentage_4p_plus,
max_amount_perc_zero,
min_amount_perc_zero,
max_amount_perc_1p,
min_amount_perc_1p,
max_amount_perc_2p,
min_amount_perc_2p,
max_amount_perc_3p,
min_amount_perc_3p,
max_amount_perc_4p_plus,
min_amount_perc_4p_plus
)
SELECT DISTINCT percent_count.date,
sum(CASE WHEN percent_count.passenger_count = 0 THEN percent_count.percent_per_passenger ELSE 0 END) AS percentage_zero,
sum(CASE WHEN percent_count.passenger_count = 1 THEN percent_count.percent_per_passenger ELSE 0 END) AS pecentage_1p,
sum(CASE WHEN percent_count.passenger_count = 2 THEN percent_count.percent_per_passenger ELSE 0 END) AS percentage_2p,
sum(CASE WHEN percent_count.passenger_count = 3 THEN percent_count.percent_per_passenger ELSE 0 END) AS percentage_3p,
sum(CASE WHEN percent_count.passenger_count > 3 THEN percent_count.percent_per_passenger ELSE 0 END) AS percentage_4p_plus,
sum(CASE WHEN percent_count.passenger_count = 0 THEN percent_count.max_Total_amount ELSE 0 END) AS max_amount_perc_zero,
sum(CASE WHEN percent_count.passenger_count = 0 THEN percent_count.min_Total_amount ELSE 0 END) AS min_amount_perc_zero,
sum(CASE WHEN percent_count.passenger_count = 1 THEN percent_count.max_Total_amount ELSE 0 END) AS max_amount_perc_1p,
sum(CASE WHEN percent_count.passenger_count = 1 THEN percent_count.min_Total_amount ELSE 0 END) AS min_amount_perc_1p,
sum(CASE WHEN percent_count.passenger_count = 2 THEN percent_count.max_Total_amount ELSE 0 END) AS max_amount_perc_2p,
sum(CASE WHEN percent_count.passenger_count = 2 THEN percent_count.min_Total_amount ELSE 0 END) AS min_amount_perc_2p,
sum(CASE WHEN percent_count.passenger_count = 3 THEN percent_count.max_Total_amount ELSE 0 END) AS max_amount_perc_3p,
sum(CASE WHEN percent_count.passenger_count = 3 THEN percent_count.min_Total_amount ELSE 0 END) AS min_amount_perc_3p,
sum(CASE WHEN percent_count.passenger_count > 3 THEN percent_count.max_Total_amount ELSE 0 END) AS max_amount_perc_4p_plus,
sum(CASE WHEN percent_count.passenger_count > 3 THEN percent_count.min_Total_amount ELSE 0 END) AS min_amount_perc_4p_plus
FROM (
SELECT DISTINCT date, passenger_count,
round((count(passenger_count) OVER (PARTITION BY date, passenger_count))*100/(count(date) OVER (PARTITION BY date)),0) AS percent_per_passenger,
max(Total_amount) OVER (PARTITION BY date, passenger_count) AS max_Total_amount,
min(Total_amount) OVER (PARTITION BY date, passenger_count) AS min_Total_amount
FROM result.core_data
WHERE trip_distance > 0
) AS percent_count
GROUP BY percent_count.date
ORDER BY percent_count.date;"""

cur.execute(insert_data_query)
connection.commit()
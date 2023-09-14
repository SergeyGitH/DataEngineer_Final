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

print("Успех")


load = "SELECT * FROM result.passengers_base"

cur = connection.cursor()
cur.execute(load)
data = cur.fetchall()

#Формирование переменной со всеми необходимыми данными для последующего перевода в файл parquet
percentageParq = pd.DataFrame(data, columns=['date', 'percentage_zero','pecentage_1p','percentage_2p','percentage_3p','percentage_4p_plus','max_amount_perc_zero',' min_amount_perc_zero','max_amount_perc_1p','min_amount_perc_1p','max_amount_perc_2p','min_amount_perc_2p','max_amount_perc_3p','min_amount_perc_3p','max_amount_perc_4p_plus','min_amount_perc_4p_plus'])

#Сохранение файла
percentageParq.to_parquet('/parquet/result_passengers_base.parquet', index=False)

print('Витрины данных успешно сохранены в формате parquet')
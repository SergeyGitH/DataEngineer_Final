import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла
data = pd.read_csv('D:/GitProject/load.csv')

# Выбор необходимых столбцов
df = data[['tip_amount', 'trip_distance', 'passenger_count']]

# Группировка данных по расстоянию и количеству пассажиров, и расчет среднего значения чаевых
avg_tips = data.groupby(['trip_distance', 'passenger_count'])['tip_amount'].mean().unstack()

# Максимальное значение для цветовой карты
vmax_value = 200

# Создание фигуры с заданным размером
plt.figure(figsize=(15, 10))

# Создание диаграммы рассеяния с заданными параметрами
scatter = plt.scatter(data['tip_amount'], data['passenger_count'], c=data['trip_distance'], cmap='cool', alpha=0.7,
                      marker='s', vmax=vmax_value)

# Установка заголовков и подписей осей
plt.xlabel('Сумма чаевых')
plt.ylabel('Количество пассажиров')
plt.title('Влияние суммы чаевых и количества пассажиров на пройденное расстояние')

# Добавление цветовой шкалы
plt.colorbar(scatter, label='Пройденное расстояние')

# Включение сетки
plt.grid(True)

# Сохранение графика в файле
plt.savefig('scatter_plot_2.png', dpi=350)

# Расчет среднего значения чаевых по каждой комбинации расстояния и количества пассажиров
avg_tips_1 = data.groupby(['trip_distance', 'passenger_count'])['tip_amount'].mean()
print(avg_tips_1)
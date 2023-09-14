## <p align="center">Проект № 5. Анализ данных поездок такси в Нью-Йорке</p>

### Описание задачи

Необходимо, используя таблицу поездок такси в Нью-Йорке, рассчитать процент поездок по количеству человек в машине. Должна получиться таблица в том числе со столбцами с самой дорогой и самой дешевой поездкой для каждой группы.

*Дополнительно: также провести аналитику и построить график на тему «Как пройденное расстояние и количество пассажиров влияет на чаевые» в любом удобном инструменте.*

******************************************************************************************************************

* [Техническое задание](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/%D0%A2%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5.txt "Техническое задание")
  
* [Требования и рекомендации для итоговой аттестации ](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B4%D0%BB%D1%8F%20%D0%B8%D1%82%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D0%B9%20%D0%B0%D1%82%D1%82%D0%B5%D1%81%D1%82%D0%B0%D1%86%D0%B8%D0%B8.txt "Требования и рекомендации для итоговой аттестации ")

### Используемые технологии
1. СУБД Postgres;
2. Python. Библиотеки: requests, pandas,  psycopg2, matplotlib, seaborn;
3. Jupiter Notebook;
4. Docker.

### Выбранный стек технологий обусловлен следующими причинами:
Размер исходного файла составляет 500... Мб, работа с данными не требует сложных и постоянных аналитических запросов, поэтому он обрабатывался в Dbeawer.  Необходимости в применении Clickhouse нет. Интепреттируемый язык программирования **PYTHON** c необходимыми библиотеками позволяет осуществлять взаимодействие с СУБД, формировать таблицы с отфильтрованными данными, обрабатывать данные с помощью Датафрейма и выполнять задачу в соотвествии с условиями Технического задания в том числе формировать графическое представление.

* [Презентация проекта](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Презентация проекта")

*************************************************************************************************************************

### <p align="center">ТЕХНИЧЕСКОЕ ОПИСАНИЕ</p> 

Скачайте файл исходных данных [yellow_tripdata](https://disk.yandex.ru/d/DKeoopbGH1Ttuw). Положите его в папку *init_db/data*  


`Далее необходимо развернуть Docker`
```
cd ...
docker-compose up
```
Далее работа происходит в Jupiter Notebook  
#### Создание *raw.py*
1. Импорт необходимых библиотек;
2. Подключение к СУБД;
3. Копирование исходного файла в СУБД без каких-либо изменений;
4. С помощью SQL запросов в BDeaver проведен анализ качества данных представленных в файле;
   *Отчет по качеству исходных данных* [здесь](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/README.md).
5. Извлечение части данных в другую таблицу с учетом их очистки от пустых и явно ошибочных значений.
   
  <img src="https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/img/raw1.png" height="432"/>
  <img src="https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/img/raw2.png" height="432"/>

#### Создание *core.py*
1. Создание витрины данных о соотношении количества поездок с различным количеством пассажиров в различные дни;
2. Создание витрины данных о максимальном и минимальном значении полной стоимости поездки такси с различным количеством пассажиров в различные дни;
3. Заполнение витрин происходит через запрос к БД.

### Создание *load.py*

    Выгрузка витрин из БД в формат parquet.

```python
    <?php phpinfo();?>
```

Таблица с пассажирами 

<img src="https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/img/%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D1%81%20%D0%BF%D0%B0%D1%81%D1%81%D0%B0%D0%B6%D0%B8%D1%80%D0%B0%D0%BC%D0%B8.png" height="432"/>

Таблица с самой дорогой и самой дешевой поездкой для каждой группы

<img src="https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/img/%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D1%81%20%D1%87%D0%B0%D0%B5%D0%B2%D1%8B%D0%BC%D0%B8.png" height="432"/>

Итоговый файл в формате [parquet](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/parquet/result_passengers_base.parquet "parquet")

### Полученные таблицы   

<img src="https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/img/taxi%20-%20result.png" />

*В представленном Техническом задании имеется несоответствие названия столбцов со столбцами представленными в исходном файле csv*

### Выводы

Рабочий проект показывает выполнение задач, определенные Техническим заданием. 

Получен работоспособный проект, инициализирующий БД службы такси, состоящую из трех слоев данных. Написаны скрипты для обработки и очистки сырых данных и получения витрины.

При ответе на дополнительный вопрос сделан вывод, что чаще всего таксист получает большую сумму чаевых при поездке на расстояние 50-100, если в машине находятся 1, 2 или 5 человек.

Проект можно доработать улучшив качество очистки данных при инициализации core-слоя и обработки данных при аналитике, а также оптимизировав его с точки зрения затрат памяти.


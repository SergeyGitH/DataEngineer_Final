## <p align="center">Проект № 5. Анализ данных поездок такси в Нью-Йорке</p>

### Описание задачи

Необходимо, используя таблицу поездок такси в Нью-Йорке, рассчитать процент поездок по количеству человек в машине. Должна получиться таблица в том числе со столбцами с самой дорогой и самой дешевой поездкой для каждой группы.

*Дополнительно: также провести аналитику и построить график на тему «Как пройденное расстояние и количество пассажиров влияет на чаевые» в любом удобном инструменте.*

* [Техническое задание](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Техническое задание")
  
* [Требования и рекомендации для итоговой аттестации ](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Требования и рекомендации для итоговой аттестации ")

### Используемые технологии
1. СУБД Postgres
2. Python.Библиотеки: requests,pandas, psycopg2,matplotlib,seaborn.
3. Jupiter Notebook
4. Docker


```diff
- *Выбранный тсек технологий обусловлен следующими причинами*
```
Файл с исходными данными службы такси обрабатывался в Dbeawer. Размер файла составляет 500... Мб, работа с данными не требует сложных и постоянных аналитических запросов. Необходимости в применении Clickhouse нет. Интепреттируемый язык программирования **PYTHON** c необходимыми библиотеками позволяет осуществлять взаимодействие с СУБД, формировать таблицы с отфильтрованными данными, обрабатывать данные с помощью Датафрейма и выполнять задачу в соотвествии с условиями Технического задания в том числе формировать графическое представление.

* [Презентация проекта](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Презентация проекта")


```diff
- ***** + ***** ! *****
```

КАРТИНКА ER-ДИАГРАММ

### Последовательность выполения 
На первоначальном этапе необходимо развернуть Docker с помощью команды
```
docker-compose up
```
Скачайте файл исходных данных находиться по ссылке. Положите его в папку *init_db/data*

Далее работа происходит работа в Jupiter Notebook

Скрипт *raw.py*

* Подключение к СУБД
    ШIMG
    Загрузка данных из файла yellow_tripdata в слой сырых данных без каких-либо изменений.
* На базе DBeaver проведен анализ файла yellow_tripdata...csv
    Отчет по качеству исходных данных [здесь](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Отчет о фильтрации данных"). 
    
    Получение части данных путем запроса к БД, их очистка от пустых и явно ошибочных значений (например отрицательных значений пройденного пути).

    Загрузка данных в core-слой.
  

Скрипт core.py

    Создание витрины данных о соотношении количества поездок с различным количеством пассажиров в различные дни.

    Создание витрины данных о максимальном и минимальном значении полной стоимости поездки такси с различным количеством пассажиров в различные дни.


Заполнение витрин происходит через запрос к БД.

Скрипт data_load

    Выгрузка витрин из БД в формат parquet.

```python
    <?php phpinfo();?>
```


### Проблемы
В представленной задаче выявлено несоответствие столбцов со столбцами представленными в исходном файле csv



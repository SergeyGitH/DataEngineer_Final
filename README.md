## <p align="center">Проект № 5. Анализ данных поездок такси в Нью-Йорке</p>

### Описание задачи

Необходимо, используя таблицу поездок такси в Нью-Йорке, рассчитать процент поездок по количеству человек в машине. Должна получиться таблица в том числе со столбцами с самой дорогой и самой дешевой поездкой для каждой группы.

*Дополнительно: также провести аналитику и построить график на тему «Как пройденное расстояние и количество пассажиров влияет на чаевые» в любом удобном инструменте.*

* [Техническое задание](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Техническое задание")
  
* [Требования и рекомендации для итоговой аттестации ](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Требования и рекомендации для итоговой аттестации ")

### Используемые технологии
1. СУБД Postgres;
2. Python.Библиотеки: requests, pandas,  psycopg2, matplotlib, seaborn;
3. Jupiter Notebook;
4. Docker.

### Выбранный стек технологий обусловлен следующими причинами:
Размер исходного файла составляет 500... Мб, работа с данными не требует сложных и постоянных аналитических запросов, поэтому он обрабатывался в Dbeawer.  Необходимости в применении Clickhouse нет. Интепреттируемый язык программирования **PYTHON** c необходимыми библиотеками позволяет осуществлять взаимодействие с СУБД, формировать таблицы с отфильтрованными данными, обрабатывать данные с помощью Датафрейма и выполнять задачу в соотвествии с условиями Технического задания в том числе формировать графическое представление.

* [Презентация проекта](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Презентация проекта")

*************************************************************************************************************************

КАРТИНКА ER-ДИАГРАММ

### <p align="center">ТЕХНИЧЕСКОЕ ОПИСАНИЕ</p> 
`На первоначальном этапе необходимо развернуть Docker`
```
cd ...
docker-compose up
```
Скачайте файл исходных данных (здесь). Положите его в папку *init_db/data*
Далее работа происходит в Jupiter Notebook

#### Создание *raw.py*
1. Импорт необходимых библиотек
2. Подключение к СУБД
3. Копирование исходного файла  [yellow_tripdata](https://disk.yandex.ru/d/DKeoopbGH1Ttuw) в СУБД без каких-либо изменений.
4. С помощью SQL запросов в BDeaver проведен анализ качества данных представленных в файле/
   *Отчет по качеству исходных данных* [здесь](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt).
5. Извлечение части данных в другую таблицу с учетом их очистки от пустых и явно ошибочных значений.
   
  <img src="https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/img/raw1.png" height="432"/>
  <img src="https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/img/raw2.png" height="432"/>

#### *core.py*
1. Создание витрины данных о соотношении количества поездок с различным количеством пассажиров в различные дни.
2. Создание витрины данных о максимальном и минимальном значении полной стоимости поездки такси с различным количеством пассажиров в различные дни.
3. Заполнение витрин происходит через запрос к БД.

<img src="https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/img/core.png" />

### load.py

    Выгрузка витрин из БД в формат parquet.

```python
    <?php phpinfo();?>
```


#### *Проблемы*
В представленном Техническом задании выявлено несоответствие названия столбцов со столбцами представленными в исходном файле csv



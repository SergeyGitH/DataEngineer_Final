## <p style="text-align: center;">Проект № 5. Анализ данных поездок такси в Нью-Йорке</p>

```diff
-
### Задача
```
Необходимо, используя таблицу поездок такси в Нью-Йорке, рассчитать процент поездок по количеству человек в машине. Должна получиться таблица в том числе со столбцами с самой дорогой и самой дешевой поездкой для каждой группы.

*Дополнительно: также провести аналитику и построить график на тему «Как пройденное расстояние и количество пассажиров влияет на чаевые» в любом удобном инструменте.*

### Используемые технологии
1. СУБД Postgres
2. Python.Библиотеки: requests,pandas, psycopg2,matplotlib,seaborn.
3. Jupiter Notebook
4. Docker


<span style='color: red;'>long</span>

[Отчет о фильтрации данных](https://github.com/SergeyGitH/DataEngineer_Final/blob/master/doc/report.txt "Отчет о фильтрации данных")


Файл с исходными данными службы такси обрабтывался в Dbeawer. Размер файла небольшой, работа с данными не требует сложных и постоянных аналитических запросов. Необходимости в применении Clickhouse нет. Интепреттируемый язык программирования python c необходимыми библиотеками позволяет осуществлять взаимодействие с СУБД, формировать таблицы с отфильтрованными данными, обрабатывать данные с помощью Датафрейма и выполнять задачу в соотвествии с условиями **Технического задания**
### Презентация по данному проекту представлена по ссылке

КАРТИНКА ER-ДИАГРАММ

```python
import requests
import pandas as pd
import psycopg2
from datetime import datetime
```


##Проблемы
В представленной задаче выявлено несоответствие столбцов со столбцами представленными в исходном файле csv



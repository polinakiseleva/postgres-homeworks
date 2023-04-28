"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

conn = psycopg2.connect(host='localhost',
                        database='north',
                        user='postgres',
                        password='228055')

cursor = conn.cursor()

with open('./north_data/customers_data.csv') as file:
    file_reader = csv.DictReader(file, delimiter=',')

    for item in file_reader:
        customer_id = item.get('customer_id')
        company_name = item.get('company_name')
        contact_name = item.get('contact_name')

        cursor.executemany(
            "INSERT INTO customers VALUES (%s, %s, %s)",
            [(customer_id, company_name, contact_name)]
        )

with open('./north_data/employees_data.csv') as file:
    file_reader = csv.DictReader(file, delimiter=',')

    for item in file_reader:
        first_name = item.get('first_name')
        last_name = item.get('last_name')
        title = item.get('title')
        birth_date = item.get('birth_date')
        notes = item.get('notes')

        cursor.executemany(
            "INSERT INTO employees VALUES (%s, %s, %s, %s, %s)",
            [(first_name, last_name, title, birth_date, notes)]
        )

with open('./north_data/orders_data.csv') as file:
    file_reader = csv.DictReader(file, delimiter=',')

    for item in file_reader:
        order_id = item.get('order_id')
        customer_id = item.get('customer_id')
        employee_id = item.get('employee_id')
        order_date = item.get('order_date')
        ship_city = item.get('ship_city')

        cursor.executemany(
            "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
            [(order_id, customer_id, employee_id, order_date, ship_city)])

conn.commit()
conn.close()

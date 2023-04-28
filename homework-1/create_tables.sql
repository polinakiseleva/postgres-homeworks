-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	first_name varchar(25) NOT NULL,
	last_name varchar(25) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(50) NOT NULl
);

CREATE TABLE orders
(
	order_id int NOT NULL,
	customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id int NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(30) NOT NULL
);

CREATE TABLE SalesData (
    id INT,
    product_name VARCHAR,
    sales_amount DECIMAL,
    transaction_date DATE
) PARTITION BY (transaction_date);


INSERT INTO SalesData (id, product_name, sales_amount, transaction_date)
VALUES
    (1, 'ProductA', 1500.00, '2023-10-15'),
    (2, 'ProductB', 2000.00, '2023-10-15'),
    (3, 'ProductA', 1200.00, '2023-10-16'),
    (4, 'ProductC', 1800.00, '2023-10-16'),
    (5, 'ProductB', 2200.00, '2023-10-17');


SELECT * FROM  nessie.SalesData AT BRANCH main;

CREATE BRANCH etl_06092023 in nessie;

USE BRANCH etl_06092023 in nessie;
INSERT INTO nessie.SalesData (id, product_name, sales_amount, transaction_date) VALUES
(6, 'ProductC', 1400.00, '2023-10-18');


SELECT * FROM nessie.SalesData AT BRANCH etl_06092023;

SELECT * FROM nessie.SalesData AT BRANCH main;


MERGE BRANCH etl_06092023 INTO main in nessie;

SELECT * FROM nessie.SalesData AT BRANCH main;
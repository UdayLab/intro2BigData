# 1. SQL Commands

## 1.1. Creation of database

     Create database sensorInfo

## 1.2. Connect to the database

     \c sensorInfo

## 1.3. Create the sensor table


    CREATE TABLE sensor(stationid integer not null primary key, location geography(POINT,4326), address varchar);

* PostGres considers primary key to be Unique and _not null_. However, some databases allow primary key to be _null_. To avoid confusion, it is better to add not null to the attribute for safety.

# 2. Install the necessary drivers and packages

## 2.1. Install Python+PostGres database driver

    pip install psycopg2-binary   

## 2.2. Install Plotly express

     pip install plotly-express

# 3. Python programs for storing the data and displaying it on the maps

   [Check the notebook](lecture1_SQL_demo.ipynb)
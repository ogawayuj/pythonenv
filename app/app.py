import os
import csv
import psycopg2
from psycopg2 import extras

# FILE PATH
DATA_FILE_DIR = './app/data/{year}/{term}/'
TARGET_YEAR = '2018'
TARGET_TERM = '週足'
DATA_FILE_PATH = DATA_FILE_DIR.format(year=TARGET_YEAR, term=TARGET_TERM)

# TARGET FILES
FILE_NAMES = os.listdir(DATA_FILE_PATH)

# DB CONNECT
DB_URL ='postgresql://postgres:secret@postgresql:5432/postgres'

def get_connection():   
    return psycopg2.connect(DB_URL)

def makeRowFromCSV(dir, fileName):
    resultList = []
    FILE_NAME = fileName
    STOCK_CODE = FILE_NAME.strip('.CSV')

    with open(dir + FILE_NAME) as f:
        reader = csv.reader(f)
        for row in reader:
            row.insert(0,STOCK_CODE)
            resultList.append(row)

    return resultList

DATA_ROW_TO_INSERT = []
for file in FILE_NAMES:
    dataRow = makeRowFromCSV(DATA_FILE_PATH, file)
    DATA_ROW_TO_INSERT.extend(dataRow)

with get_connection() as conn:
    with conn.cursor() as cur:
        # cur.execute('select * from trn_stock_price_by_date')
        extras.execute_values(cur,"INSERT INTO trn_stock_price_by_date VALUES %s" ,DATA_ROW_TO_INSERT)
        conn.commit()


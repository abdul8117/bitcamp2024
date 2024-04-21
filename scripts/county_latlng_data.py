import sqlite3

DB_PATH = 'db/county_latlng_data.db'

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("CREATE TABLE data (fips_code VARCHAR(5), name TEXT, lng REAL, lat REAL, PRIMARY KEY (fips_code));")
    conn.commit()
    conn.close()


def import_csv_data():
    import csv

    csv_file = 'counties_lat_lng.csv'
    data = []

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        is_first_row = True

        for row in csv_reader:
            if is_first_row:
                is_first_row = False
                continue

            data.append(row)
    
    return data


def insert_data(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    for row in data:
        # Extract values from the row
        fips_code = row[0]
        county_name = row[1]
        lat = row[2]
        lng = row[3]

        # Construct SQL INSERT statement
        query = f"INSERT INTO data (fips_code, name, lat, lng) VALUES (?, ?, ?, ?)"
        c.execute(query, (fips_code, county_name, lat, lng))

    conn.commit()
    conn.close()

# create_table()
# data = import_csv_data()
# insert_data(data)

def lat_lng(fips_code):
    import os

    print(os.getcwd()) 
    conn = sqlite3.connect('db/county_latlng_data.db')
    c = conn.cursor()

    query = 'SELECT lat, lng FROM data WHERE fips_code=?'
    result = c.execute(query, [fips_code]).fetchall()
    conn.close()
    return f'{result[0][0]} {result[0][1]}'


# fips_code = '24031'

# conn = sqlite3.connect('db/county_latlng_data.db')
# c = conn.cursor()

# query = 'SELECT lat, lng FROM data WHERE fips_code=?'
# result = c.execute(query, [fips_code]).fetchall()
# print(f'{result[0][0]} {result[0][1]}')
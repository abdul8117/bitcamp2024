import sqlite3

DB_PATH = 'db/housing_data.db'

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # delete data table and month_years table if they exist
    c.execute("DROP TABLE IF EXISTS data;")

    # Create a table to store the Zillow data with county name and state
    c.execute("CREATE TABLE data (RegionID INT, county_name VARCHAR(255), state VARCHAR(2), PRIMARY KEY (RegionID));")

    # Create a temporary table to store year and month values
    c.execute("CREATE TABLE month_years (year INT, month INT);")

    # Populate temporary table
    years = range(2000, 2024) 
    months = range(1, 13)

    for year in years:
        for month in months:
            c.execute("INSERT INTO month_years VALUES (?, ?)", (year, month))

    # Generate and execute ALTER TABLE statements 
    c.execute("SELECT year, month FROM month_years")
    for year, month in c.fetchall():
        column_name = f"Y{year}M{month}" 
        query = f"ALTER TABLE data ADD {column_name} FLOAT;" 
        c.execute(query)

    # delete the temporary table
    c.execute("DROP TABLE IF EXISTS month_years;")

    conn.commit() # Save changes
    conn.close()


def import_csv_data():
    import csv

    csv_file = 'county_housing_data.csv'
    data = []

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        is_first_row = True

        for row in csv_reader:
            if is_first_row:
                is_first_row = False
                continue  # Skip the first row (header)

            data.append(row)
    
    return data


def insert_data(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    for row in data:
        # Extract values from the row
        region_id = int(row[0]) 
        county_name = row[1]
        state = row[2]
        housing_prices = row[3:] # fourth column onwards

        # Construct SQL INSERT statement
        query = f"INSERT INTO data (RegionID, county_name, state) VALUES (?, ?, ?)"
        c.execute(query, (region_id, county_name, state))

        # Add housing price data columns
        for idx, price in enumerate(housing_prices):
            year = 2000 + idx // 12
            month = idx % 12 + 1
            
            if year > 2023:
                break

            column_name = f"Y{year}M{month}"
            query = f"UPDATE data SET {column_name} = ? WHERE RegionID = ?"
            c.execute(query, (price, region_id))

    conn.commit()
    conn.close()


create_table()
housing_data = import_csv_data()
insert_data(housing_data)
import sqlite3

# Connect to the database
connection = sqlite3.connect("db/house_prices_monthly.db")

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# query = "SELECT * FROM data LIMIT 5"

# query = """SELECT
# Y2001M1,
# Y2001M2,
# Y2001M3,
# state,
# county_name
# FROM
# data
# WHERE
# state = 'FL'
# AND county_name = "Bay County"
# AND Y2000M1 !='';
# """

county="Bay County"
state="FL"
disaster_year=2001
start_year=disaster_year-1
start_year=str(start_year)
end_year=disaster_year+1
end_year=str(end_year)
disaster_year=str(disaster_year)
disaster_month=12
query = "SELECT\n"
for i in range(disaster_month,13):
  query+="Y"+start_year+"M"+str(i)+",\n"
for i in range(1,disaster_month+1):
  query+="Y"+disaster_year+"M"+str(i)+",\n"
for i in range(disaster_month+1,13):
  query+="Y"+disaster_year+"M"+str(i)+",\n"
for i in range(1,disaster_month+1):
  query+="Y"+end_year+"M"+str(i)+",\n"
query+="state,\n"
query+="county_name\n"
query+="FROM\n"
query+="data\n"
query+="WHERE\n"
query+="county_name = '"+county+"'\n"
query+="AND state = '"+state+"'\n"
query+="AND Y2000M1 !='';"

print(query)
# query = """SELECT
#   Y2000M1,
#   Y2000M2,
#   Y2000M3,
#   Y2000M4,
#   state,
#   county_name
# FROM
#   data
# WHERE
#   state = 'FL'
#   AND county_name = 'Bay County';
# """

# Execute the SQL query
results = cursor.execute(query).fetchall()
results[0]=results[0][0:24]


# Print the results
for row in results:
    print(row)


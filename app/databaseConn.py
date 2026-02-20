import psycopg
try:
    # conn = psycopg.connect(
    #     host="localhost",
    #     dbname="SocialMediaDatabase",
    #     user="kaustuvdash",
    #     password=""
    # )
    conn = psycopg.connect("postgresql://fastapidatabase_7okt_user:E3uExDiRuJXhZPDXne0tIDCJwWwjKJHt@dpg-d6bvf33h46gs738b320g-a/fastapidatabase_7okt")
    cursor = conn.cursor()
    print("Database connection was successful")
except Exception as error:
    print("Connecting to database failed")
    print("error:-", error)
import psycopg
try:
    conn = psycopg.connect(
        host="localhost",
        dbname="SocialMediaDatabase",
        user="kaustuvdash",
        password=""
    )
    cursor = conn.cursor()
    print("Database connection was successful")
except Exception as error:
    print("Connecting to database failed")
    print("error:-", error)
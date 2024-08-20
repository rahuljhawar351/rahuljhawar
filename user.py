import sqlite3

def create_connection():
    try:
        con = sqlite3.connect("users.sqlite3")
        return con
    
    except Exception as e:
        print(f"Error:{e}")

INPUT_STRING = """
Enter the option:
    1. CREATE TABLE
    2. DUMP users from csv INTO users TABLE
    3. ADD new user INTO users TABLE
    4. QUERY all users from TABLE
    5. QUERY user by id from TABLE
    6. QUERY specified no. of records from TABLE
    7. DELETE all users
    8. DELETE user by id
    9. UPDATE user
    10. Press any key to EXIT
    """

def create_table(conn):
    CREATE_USERS_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name CHAR(255) NOT NULL,
            last_name CHAR(255) NOT NULL,
            company_name CHAR(255) NOT NULL,
            address CHAR (255) NOT NULL,
            city CHAR(255) NOT NULL,
            county CHAR(255) NOT NULL,
            state CHAR(255) NOT NULL,
            zip REAL NOT NULL,
            phone1 CHAR(255) NOT NULL,
            phone2 CHAR(255),
            email CHAR(255) NOT NULL,
            web text
            );
        """
    cur = conn.cursor()
    cur.execute(CREATE_USERS_TABLE_QUERY)
    print("User Table was create successfully.")

import csv 
def read_csv():
    users = []
    with open("sample_users.csv","r") as f:
        data = csv.reader(f)
        for users in data:
            users.append(tuple(users))

    return users[1:]
    
def insert_users(con,users):
    users_add_query = """
        INSERT INTO users
        (
            first_name,
            last_name,
            company_name,
            address,
            city,
            county,
            state,
            zip,
            phone1,
            phone2,
            email,
            web
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?);
    """
    cur = con.cursor()
    cur.executemany(users_add_query, users)
    con.commit()
    print(f"{len(users)} users were imported successfully.")

def main():
    con = create_connection()
    user_input = input(INPUT_STRING)
    if user_input == "1":
        create_table(con)
    elif user_input == "2":
        read_csv()
        users = read_csv()
        insert_users(con,users)

main()


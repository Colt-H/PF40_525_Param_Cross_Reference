import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as return_error:
        print(return_error)

    return conn

def select_parameter(conn, parameter):
    cur = conn.cursor()
    cur.execute("SELECT * FROM param_xref where PF40_Param=? COLLATE NOCASE", (parameter,))

    rows = cur.fetchall()

    try:
        pf525 = [x[2] for x in rows]
        desc = [x[1] for x in rows]
        note = [x[3] for x in rows]
        print(f'PF525 Parameter for {desc[0]}is {pf525[0]}')
        if note[0] != '':
            print(f"Note: {note[0]} ")
    except IndexError:
        print("No Parameter Returned")


def main():
    while True:
        database = "param_xref.db"

        conn = create_connection(database)
        with conn:
            parameter = input("Enter the PF40 Parameter Number: ")
            select_parameter(conn, parameter)


if __name__ == '__main__':
    main()

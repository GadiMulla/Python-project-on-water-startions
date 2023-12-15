import socket
import sqlite3
from datetime import datetime

host = '127.0.0.1'  # Server IP address
port = 12346  # Server port
database_file = 'data.sqlite'  # SQLite database file name


def handle_client(client_socket):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print('Received data:', data)

        # Split the received data into station_id, alarm1, and alarm2
        station_id, alarm1, alarm2 = data.split()

        # Get the current date and time
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M')

        # Check if the station already exists in the database
        cursor.execute("SELECT * FROM station_status WHERE station_id=?", (station_id,))
        existing_station = cursor.fetchone()

        if existing_station:
            # Update the existing station's data in the database
            cursor.execute("UPDATE station_status SET last_date=?, alarm1=?, alarm2=? WHERE station_id=?",
                           (current_datetime, alarm1, alarm2, station_id))
        else:
            # Insert a new station's data into the database
            cursor.execute("INSERT INTO station_status VALUES (?, ?, ?, ?)",
                           (station_id, current_datetime, alarm1, alarm2))

        # Commit the changes to the database
        conn.commit()

    # Close the database connection and the client socket
    cursor.close()
    conn.close()
    client_socket.close()


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print('Server listening on {}:{}'.format(host, port))

    # Create the database table if it doesn't exist
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS station_status (
                        station_id INTEGER,
                        last_date TEXT,
                        alarm1 INTEGER,
                        alarm2 INTEGER,
                        PRIMARY KEY(station_id)
                    )''')
    conn.commit()
    cursor.close()
    conn.close()

    while True:
        client_socket, addr = server_socket.accept()
        print('Client connected:', addr)

        handle_client(client_socket)


run_server()

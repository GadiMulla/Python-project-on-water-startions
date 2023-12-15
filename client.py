import socket
import time

host = '127.0.0.1'  # Server IP address
port = 12346  # Server port
wait_time = 60  # Seconds between data sending


def send_data(client_socket):
    with open('status.txt', 'r') as file:
        lines = file.readlines()
        station_id = lines[0].strip()
        alarm1 = lines[1].strip()
        alarm2 = lines[2].strip()

        data = '{} {} {}'.format(station_id, alarm1, alarm2).encode()
        client_socket.send(data)


def run_client():
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        send_data(client_socket)

        client_socket.close()

        time.sleep(wait_time)


run_client()
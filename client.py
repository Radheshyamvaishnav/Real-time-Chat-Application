import threading
import socket
from crypto import encryption as encrypt
from crypto import decryption as decrypt

names = input('Enter Your Name ----> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "names?":
                client.send(names.encode('utf-8'))
                pass
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{names}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()

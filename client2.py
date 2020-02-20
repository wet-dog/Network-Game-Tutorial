import socket
import pickle


def Main(data):
    # local host IP '127.0.0.1'
    host = '192.168.1.69'

    # Define the port on which you want to connect
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))

    # message you send to server
    message = pickle.dumps(data)

    while True:
        try:
            # message sent to server
            s.send(message)

            # message received from server
            data = s.recv(1024)
            data = pickle.loads(data)

            # print the received message
            print('Received from the server :', data)
        except socket.error as e:
            return str(e)

    s.close()

if __name__ == '__main__':
    Main([5, 4])

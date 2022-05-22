import socket
import sys
import threading
from Reader import Reader
#intiating socket and list of threads
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.bind((socket.gethostname(), 1234))
Socket.listen(3)
threads = []
#flight_Reader object to call class Reader functions
flight_Reader = Reader()


def connection_thread(sock, id):
    """
         ----Connection thread function----

    *The function has two parameters which are sock and id
     -sock is the socket accepting connections
     -id is the current connection ID

    *This function perform the services provided by the server

    1-Receive the client information
    2-Receive the Airport arr_icao and passing it to API function in Reader class to retrieve records
    3-Receive the client selection and parameters
    4-Based on the client selection it passes the received value to concerned function in Reader class
    5-Then retrievers the requested information through Reader class and send it to the client

    """
    print("Start of connection:" + str(id))
    user_Name = sock.recv(1024).decode('utf-8')
    print("User: {}, started the program".format(user_Name))
    icao = sock.recv(1024).decode('utf-8')
    print("User: {}, Requested information about Airport: {} ".format(user_Name, icao))
    flight_Reader.API(icao)

    while True:
        Menu = sock.recv(1024).decode('utf-8')

        if Menu == '1':
            print("User: {}, Requested all arrived flights information".format(user_Name))
            print("Request parameters: {}".format('All'))
            requested_Data = flight_Reader.option1()
            sock.send(str(requested_Data).encode())

        if Menu == '2':
            print("User: {}, Requested all delayed flights information".format(user_Name))
            print("Request parameters: {}".format('All'))
            requested_Data = flight_Reader.option2()
            sock.send(str(requested_Data).encode())
        if Menu == '3':
            city = sock.recv(1024).decode('utf-8')
            print("User: {}, Requested all flights coming from {}".format(user_Name, city))
            requested_Data = flight_Reader.option3(city)
            sock.send(str(requested_Data).encode())
        if Menu == '4':
            flight_Code = sock.recv(1024).decode('utf-8')
            print("User: {}, Requested details of flight {}".format(user_Name, flight_Code))
            requested_Data = flight_Reader.option4(flight_Code)
            sock.send(str(requested_Data).encode())
        if Menu == '5':
            print("User: {}, Exiting the program".format(user_Name))
            print("Good Bye.")
            print("End of Connection: " + str(id))
            break


while True:
    #Creating and starting the threads
    sock_a, socketname = Socket.accept()
    t = threading.Thread(target=connection_thread, args=(sock_a, len(threads) + 1))
    t.start()
    threads.append(t)
    if len(threads) > 4:
        #controling number of concurrent threads
        break


sock_a.close()
Socket.close()
sys.exit()

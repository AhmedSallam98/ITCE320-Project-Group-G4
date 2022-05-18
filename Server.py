import socket
import sys
import threading
import requests
import json
from Options import options

options = options()

def API(icao):
    """
         ---- API Function ----

      *Function has one parameter 'icao'
      1-arr_icao is received from the client
      2-Assigning the iao into the request parameters
      3-Retrieves 100 records of a certain Airport
      4-Saves the retrieved information in .json file for testing and evaluation

    """
    params = {
        'access_key': '243a0603e8a7bd754ab592756261ce7a',
        'limit': 100,
        'arr_icao': icao

    }
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
    results = json.dumps(api_result.json(), indent=2)
    with open("group_ID.json", "w") as storedData:
        json.dump(results, storedData, indent=2,sort_keys=True)

def connection_thread(sock, id):
    """
         ----Connection thread function----

    *The function has two parameters which are sock and id
     -sock is the socket accepting connections
     -id is the current connection ID

    *This function perform the services provided by the server

    1-Receive the client information
    2-Receive the Airport ICAO and passing it to API function to retrieve records
    3-Receive the client selection and parameters
    4-Based on the client selection it passes the received value to option function in Options class
    5-Then retrievers the requested information through Option class and send it to the client

    """
    print("Start of connection:" + str(id))
    Username = sock.recv(1024).decode('utf-8')
    print("User: {}, started the program".format(Username))
    icao = sock.recv(1024).decode('utf-8')
    print("User: {}, Requested information about Airport: {} ".format(Username, icao))
    API(icao)

    while True:
        Menu = sock.recv(1024).decode('utf-8')

        if Menu == '1':
            print("User: {} Requested all arrived flights information".format(Username))
            print("Request parameters: {}".format('None'))
            requested_Data = options.option1()
            sock.send(str(requested_Data).encode())

        if Menu == '2':
            print("User: {} Requested all delayed flights information".format(Username))
            print("Request parameters: {}".format('None'))
            requested_Data = options.option2()
            sock.send(str(requested_Data).encode())
        if Menu == '3':
            city = sock.recv(1024).decode('utf-8')
            print("User: {} Requested all flights coming from {}".format(Username, city))
            requested_Data = options.option3(city)
            sock.send(str(requested_Data).encode())
        if Menu == '4':
            flight_Code = sock.recv(1024).decode('utf-8')
            print("User: {} Requested details of flight {}".format(Username, flight_Code))
            requested_Data = options.option4(flight_Code)
            sock.send(str(requested_Data).encode())
        if Menu == '5':
            print("User: {}, Exiting the program".format(Username))
            print("End of Connection: " + str(id))
            break


Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.bind((socket.gethostname(), 1234))
Socket.listen(3)
threads = []
while True:
    #Creating and starting the threads
    sock_a, socketname = Socket.accept()
    t = threading.Thread(target=connection_thread, args=(sock_a, len(threads) + 1))
    t.start()
    threads.append(t)
    if len(threads) > 4:
        #controling number of concurrent threads
        break
    for thread in threads:
        #block until [thread] terminates
        thread.join()
    break
print("Good Bye.")
sock_a.close()
Socket.close()
sys.exit()

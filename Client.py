import socket
import sys
#Initiating the socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect((socket.gethostname(), 1234))


user_Name = input("Enter User Name: ")
Socket.send(user_Name.encode())
airport_Icao = input("Enter the Airport code ICAO: ")
Socket.send(airport_Icao.encode())
while True:
    print("Please Choose the option Number\n"
          "1-Retrieve Arrived flights information\n"
          "2-Retrieve Delayed flights information\n"
          "3-Retrieve All flights coming from a specific city\n"
          "4-Retrieve details of a particular flight\n"
          "5-Quit the program")
    Menu = input()
    if Menu == '1':
        Socket.send(Menu.encode())
        Data = Socket.recv(60000)
        print(Data.decode('utf-8'))

    if Menu == '2':
        Socket.send(Menu.encode())
        Data = Socket.recv(60000)
        print(Data.decode('utf-8'))

    if Menu == '3':
        Socket.send(Menu.encode())
        city = input("Enter the departure city code (iata): ")
        Socket.send(city.encode())
        Data = Socket.recv(60000)
        print(Data.decode('utf-8'))
    if Menu == '4':
        Socket.send(Menu.encode())
        flight_Code = input("Enter flight code (iata): ")
        Socket.send(flight_Code.encode())
        Data = Socket.recv(60000)
        print(Data.decode('utf-8'))
    if Menu == "5":
        Socket.send(Menu.encode())
        print("Exiting the program \n Good Bye.")
        Socket.close()
        sys.exit()

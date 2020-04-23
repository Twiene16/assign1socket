import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=7634

s.connect((host,port))
c_msg1="Hello, who are you"
c_msg2="what is your domain"
c_msg3="Who is the web Admin"

while True:
    
    print("++++++++++++ MENU UTAMA ++++++++++++")
    print("+ 1. Hello who are you             +")
    print("+ 2. What is your domain?          +")
    print("+ 3. Who is the web Admin                        +")
    print("+ 4. exit                          +")
    print("++++++++++++++++++++++++++++++++++++")
    msg_selection = int(input("+ selection : "))
    print("++++++++++++++++++++++++++++++++++++")
    
    if msg_selection == 1:
            s.send(c_msg1.encode())
            s_messg=s.recv(1024)
            print("message from server: ",s_messg.decode())
    elif msg_selection == 2:
            s.send(c_msg2.encode())
            s_messg=s.recv(1024)
            print("message from server: ",s_messg.decode())
    elif msg_selection == 3:
           s.send(c_msg3.encode())
           s_messg=s.recv(1024)
           print("message from server: ",s_messg.decode())
    elif msg_selection == 4:
            sys.exit()
 
    
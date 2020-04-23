import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=7634
s.bind((host,port))
s.listen(5)
con,addr=s.accept()

print("connected with",addr)
r_msg1="hi, my name is" + (str (addr))
r_msg2="my domain is fskm.edu.my"
r_msg3="i dont know"
##cmd =input ()
##limattempt = 5
##attempt = 1
##while attempt < limattempt:
    ##c_messg=con.recv(1024)
    ##print("message from client: ",c_messg.decode())
    ##messg="hi, my name is 192.168.56.1"
    ##con.send(messg.encode())
    ##attempt +=1
    
while True:
    c_messg=con.recv(1024)
    print("message from client: ",c_messg.decode())
    print("++++++++++++ Message from Client+++++++++++++++++++++")
    print("Type 1 If client send Hello who are you             +")
    print("Type 2 if client send What is your domain?          +")
    print("Type 3 if None of the above                         +")
    print("+ 4. exit                                         +")
    print("++++++++++++++++++++++++++++++++++++")
    msg_recieved= int(input("+ selection : "))
    print("++++++++++++++++++++++++++++++++++++")
    
    if msg_recieved == 1:
        con.send(r_msg1.encode())
    if msg_recieved == 2:
        ##c_messg=con.recv(1024)
        ##print("message from client: ",c_messg.decode())
        con.send(r_msg2.encode())
    if msg_recieved == 3:
        con.send(r_msg3.encode())
    if msg_recieved == 4:
        sys.exit()
con.close()
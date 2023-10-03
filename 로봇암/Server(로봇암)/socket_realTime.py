from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
from pymycobot import PI_PORT, PI_BAUD
import time 
import pickle
import socket 
import keyboard
HOST = '0.0.0.0'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST,PORT))

server_socket.listen()
print("START, PORT : ",PORT)

client_socket, addr = server_socket.accept()


mc = MyCobot(PI_PORT,PI_BAUD)
while mc.is_power_on() != 0:
    mc.power_off()
while mc.is_power_on() != 1:
    mc.power_on()
while mc.get_end_type() != 1:
    mc.set_end_type(1)
while mc.get_reference_frame() != 0:
    mc.set_reference_frame(0)


mc.release_all_servos()



#Initial 6DoF
mc.release_all_servos()

print("To save initial position, press p key")
a=0
while True:
    Initial_pos=mc.get_coords()
    if len(Initial_pos)==0:
        continue
    #input()
    print("Current pose : ", Initial_pos )
    if keyboard.is_pressed('p'): # front
     if len(Initial_pos)==0:
        print("Press p key again")
     else:
        break

print("To stop this, press q key")
while True:
   pos = mc.get_coords()
   if len(pos)==0:
    print("pos None : ", pos)
   else:
    print("pos[0] : ",pos[0])
    print("Initial_pos[0]",Initial_pos[0])
    x  = pos[0]-Initial_pos[0]
    y = pos[1]-Initial_pos[1]
    z = pos[2]-Initial_pos[2]
    roll = pos[3]-Initial_pos[3]
    pitch = pos[4]-Initial_pos[4]
    yaw = pos[5]-Initial_pos[5]
    message=f"{x},{y},{z},{roll},{pitch},{yaw}"
    #message=f"{pos[0]+23.5},{pos[1]-165.9},{pos[2]-227.7},{pos[3]+86.51},{pos[4]+40.51},{pos[5]+115.59}"
    client_socket.sendall(message.encode())
    #print("Current pose : ", pos )
    print("Sending data : ", message)
    time.sleep(0.1)
    if keyboard.is_pressed('q'): # front
        break

print("finished process")
client_socket.close()
server_socket.close()



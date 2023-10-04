from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
from pymycobot import PI_PORT, PI_BAUD
import time 
import pickle
import socket 

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

    
with open("traj.pkl", "rb") as f:
    trajectories = pickle.load(f)

#Initial 6DoF
x=trajectories[0][0]
y=trajectories[0][1]
z=trajectories[0][2]
roll=trajectories[0][3]
pitch=trajectories[0][4]
yaw=trajectories[0][5]

mc.send_coords(trajectories[0],30,1)
mc.send_coords(trajectories[0],30,1)
while True:
    res = mc.get_coords()
    if res:
        break

print("To restore trajectories, press ANY key")
input()


for pos in trajectories:
    mc.send_coords(pos, 5, 1)
    # pos = pos - [-136.9, -27.9, 243.0, -87.33, -34.99, -114.91]
    message=f"{pos[0]-x},{pos[1]-y},{pos[2]-z},{pos[3]-roll},{pos[4]-pitch},{pos[5]-yaw}"
    client_socket.sendall(message.encode())
    print("Sending data : ", message)

    time.sleep(0.1)


print("finished process")
client_socket.close()
server_socket.close()
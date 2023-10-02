from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
from pymycobot import PI_PORT, PI_BAUD
import time 
import pickle

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

mc.send_coords(trajectories[0],30,1)
while True:
    res = mc.get_coords()
    if res:
        break

print("To restore trajectories, press ANY key")
input()

for pos in trajectories:
    mc.send_coords(pos, 20, 1)
    # time.sleep(0.1)


print("finished process")
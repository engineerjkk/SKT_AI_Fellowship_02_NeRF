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

print("To save trajectories, press ANY key")
input()
trajectories = []
for _ in range(200):
    trajectories.append(mc.get_coords())
    print(mc.get_coords())
    # time.sleep(0.1)

with open("traj.pkl", "wb") as f:
    pickle.dump(trajectories, f)

print("finished dumping")
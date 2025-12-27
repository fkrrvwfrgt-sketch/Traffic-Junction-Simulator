import time
import random
import os

roads = ['lane_a.txt', 'lane_b.txt', 'lane_c.txt', 'lane_d.txt']

print("Traffic Generator started. Populating AL1 incoming lanes...")

for r in roads:
    if os.path.exists(r):
        open(r, 'w').close()

while True:
    road_file = random.choice(roads)
    
    with open(road_file, "a") as f:
        f.write("v\n")
    
    time.sleep(random.uniform(0.3, 0.7))


import time
import random
import os

# Lanes as specified in your requirements
roads = ['lane_a.txt', 'lane_b.txt', 'lane_c.txt', 'lane_d.txt']

print("Traffic Generator started. Populating AL1 incoming lanes...")

# Clean up any old data
for r in roads:
    if os.path.exists(r):
        open(r, 'w').close()

while True:
    # Randomly pick a road (A, B, C, or D)
    road_file = random.choice(roads)
    
    # Write a vehicle marker 'v' representing an arrival in AL1
    with open(road_file, "a") as f:
        f.write("v\n")
    
    # Adjust speed of arrivals here (0.2 to 0.7 seconds)
    time.sleep(random.uniform(0.2, 0.7))
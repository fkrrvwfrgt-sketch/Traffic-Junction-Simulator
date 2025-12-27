# Traffic-Junction-Simulator

Assignment 1 - Traffic Light Simulator

Course: Data Structures and Algorithms (COMP202)

Name: Sara Basnet

Roll Number: 10

1. Summary

This project simulates a traffic junction with 4 roads (A,B,C,D) and 3 lanes each. The program implements vehicle queues using a queue data structure. Priority lane AL2 is served first if more than 10 vehicles are waiting. Normal lanes are served round-robin. Left-turn lanes are served if available.

2. Data Structures Used

Queue: FIFO queue implemented in queue_ds.py

Dictionary: For storing all lane queues

3. Functions Implemented

enqueue(item)

dequeue()

size()

generate_vehicles(lanes)

traffic_simulator()

print_lane_status()

4. Algorithm

Generate vehicles randomly for all lanes.

If AL2 has >10 vehicles → serve AL2 until <5 vehicles.

Serve normal lanes in round-robin.

Serve left-turn lanes if vehicles present.

5.Project Structure

simulator.py: Contains the main Pygame loop, vehicle movement logic, and UI rendering.

queue_ds.py: A custom implementation of the Queue data structure.

traffic_generator.py: Script to generate the traffic load.

lane_*.txt: Real-time data buffers for vehicle arrivals.

6. Time Complexity

Enqueue: O(1)

Dequeue: O(n) (because we use list pop(0))

7. How to Run

Open Terminal 1 and run the generator:

Bash

python traffic_generator.py

Open Terminal 2 and run the simulator:

Bash

python simulator.py

8. Demo

https://github.com/user-attachments/assets/6e87d652-0218-40a4-a2f9-bd7f4d0728f6


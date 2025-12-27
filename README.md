# Traffic-Junction-Simulator
Assignment 1 - Traffic Light Simulator
Course: Data Structures and Algorithms (COMP202)
Name: Sara Basnet Roll Number: 10

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
5. Time Complexity
Enqueue: O(1)
Dequeue: O(n) (because we use list pop(0))
6. How to Run
Open terminal in dsa-queue-simulator 

https://github.com/user-attachments/assets/26ad1837-28f6-4631-971a-9dc885128805

folder.
Run:
python simulator.py
   7.  References

https://github.com/user-attachments/assets/57edd1f4-3dba-4e6c-a3c7-daeb3dedd6b7


Python Documentation: collections.deque and heapq modules. https://docs.python.org/3/library/collections.html
Pygame Documentation: Graphics and event handling. https://www.pygame.org/docs/
Queueing Theory: Basics of M/M/1 queues and Poisson processes for traffic simulation.
Assignment 1 Problem Statement: Logic formulas implementing Fair Dispatch and Priority Hysteresis.
8. Source Code
Repository Link:
9. 9.Conclusion
The traffic junction simulator shows how effectively real logistical challenges can be solved with linear data structures. A system operates the traffic flow across the cross of four big roads by realizing the vehicle queues based on the FIFO principle and a logic-driven priority queue. The project confirms that the mathematical model used-vehicle dispatching-balances normal average flow with high-priority overrides, effectively maintaining junction efficiency while preventing deadlocks. This simulation allows clear and useful visualization, in a dynamic real-time environment, of queue management systems using Python and Pygame.
10. Demo

    
    

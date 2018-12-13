<p align="justify">
This problem statement was an assignment as a part of my coursework for Foundations of Artificial Intelligence for the Masters program at USC. I had loads of fun doing this so let’s start with the problem statement:
</p>

![Alt text](Figure0.png?raw=true)

# The Problem:
<p align="justify">
You are helping the LA Dept of Transportation (LADOT) to develop a pilot scooter program for LA. There are a limited number of police officers available to monitor and address issues that may arise from scooters, ranging from traffic and safety violations to accidents with cars, bikes, other scooters and pedestrians. The scooter companies have given LADOT access to scooter routes over the course of one day. In order to maximize the scooter activity monitored by the officers, you will take as input the route information, the monitored city area dimensions, and the number of officers available to then generate the best placement of the officers. The officers can only be in one place for one day, and there can only be one officer on each street. When an officer and scooter are at the same location at the same time, the officer is able to address a safety issue, and one “Activity point” is gained. The goal is to place the officers in locations that do not conflict with each other, while maximizing the total “Activity points” for the day (12 time steps in a day). 

The problem follows these rules:  
• Officers cannot be in same square, same row, same column, or along the same diagonal. (Think of queens on a chess board)  
• Officers cannot move.  
• Activity points are collected at each time step t when officers are in same square as scooters. One point per each scooter.  
• The grid coordinate system will be indexed starting from the top-left corner.   

An example of a 5 by 5 grid is given below with each cell’s coordinates:
</p>

![Alt text](Figure1.png?raw=true)

<p align="justify">
</p>

![Alt text](Figure2.png?raw=true)
![Alt text](Figure3.png?raw=true)

# Input:

The file input.txt in the current directory of your program will be formatted as follows:  

First line: strictly positive 32-bit integer n, the width and height of the n x n city area, n <= 15.  
Second line: strictly positive 32-bit integer p, the number of police officers  
Third line: strictly positive 32-bit integer s, the number of scooters  
Next s*12 lines: the list of scooter x,y coordinates over time, separated with the End-of-line character LF. With s scooters and 12 timesteps in a day, this results in 12 coordinates per scooter.  

# Output:
Max activity points: strictly positive 32-bit integer m

# Example:
Input.txt   
5  
3  
5  
0,1  
0,0  
0,1  
0,0  
0,0  
1,1  
0,2  
0,1  
0,1  
1,1  
0,2  
1,3  
2,1   
1,0  
1,1  
1,1  
0,0  
1,0  
1,1  
2,0  
3,1  
4,1  
4,1  
3,1  
3,2  
3,1   
3,2  
4,2  
3,1   
4,2  
4,1  
3,0  
4,1  
3,2  
4,3  
4,2  
4,4  
4,3  
3,2  
3,2  
4,3  
3,2  
4,3  
3,3  
3,3  
2,2  
2,1    
2,1  
4,0  
4,1  
4,2   
4,2   
4,1  
4,0  
4,1  
3,2  
2,1  
1,0   
0,1  
0,1  
 

Output.txt  
41  
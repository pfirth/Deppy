# Deppy

Development of python classes to interact with different elements of Deppy/Annie inlcuding, Transfer engineering stepper motors, matchbox stepper motors, gate valves, MFC hubs nozzels ect...(Eventually Java files that complete the same tasts will also be available)

The goal is to create a single user interface encapsolating the abilities of each class. This differes from the current lab view code by the way it communicates with the equipment. Overall it should be safer and less errors should occur. 


Things to be done (in no particular order):

1) Python code for interacting with the 24V valves (Java should be able to accomplish this easily)

2) Circuit/code to bypass the need for the MFC hub

3) Fully functional interface (Java or Python)

4) Automation of elliposometer measurements/file storage

5) Remote monitoring of the chamber conditions (namely pressure)

6) Java version of all the code (for portability)

7) In the MFC class, the standard for identifying the MFC port needs to be "standardized". In some places
its an Int in others its a String.

8) Need a check for value errors when setting values


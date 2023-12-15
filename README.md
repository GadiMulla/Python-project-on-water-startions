Python Project

Creating a database server that communicates with clients representing a "water-stations"


Explanation for the Client Code


The client needs to run in a loop in which it reads data from its status.txt, connects to the server, and sends the data to the server, it needs to do so once every 60 seconds*

make sure the code closes status.txt after reading from it, this will allow changing the file from outside (using notepad/gedit) and the code will be able to read the changes. if you keep the file open, it might read the same data and won't see the changes. status.txt 
will contain the data of a single water station using the following 3 lines:

● the first line represents the station ID (some integer)

● the second line represent the state of Alarm1 (0 for OFF; 1 for ON)

● the second line represent the state of Alarm2 (0 for OFF; 1 for ON)

For example if the file contains the following lines: 123 0 1 Then it represents station ID 123, its first alarm is OFF and its second Alarm is ON. The main concept is that while the client program is running, the user will be able to change the text manually using a program like notepad or gedit and save it in order to change what data the client will read in the next loop iteration. If you want to have more clients, you copy client.py and status.txt to a different folder, change the ID and alarm status in the txt file (of the copy) and run the copy. repeat for each additional client you wish to have. (note: alternatively, you can have multiples status files with different names like status1.txt status2.txt etc. and when you run the client before entering the loop ask the user what file to open, it will only open that file until the program is closed)

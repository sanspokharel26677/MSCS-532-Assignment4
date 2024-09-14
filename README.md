# MSCS-532-Assignment4
1. As a part of assignment 3, this repo contains 2 files named, "heapsort.py" and "priority_queue.py" for part 1 and part 2.
2. Source code should be run by python3. In case pandas is not installed in system, it must be installed first. Here is the terminal command to install pandas for python3: pip3 install pandas
3. Example: To run 'heapsort.py' in the terminal we should go to the directory where the file is saved and enter "python3 heapsort.py". Similarly other python file can be run.
4. I have also added one of the output file generated from running the program which has been used in report also just in case of need for validation.
5. I have also included the pdf version of report so that mathematical equations could be stable. In fact, as the reports were getting longer I decided to split them into 2 files for different part of assignment. 
6. 


Summary of Heapsort findings
-----------------------------

The measured times for insert, search, and delete operations in this hash table implementation reflect the effectiveness of chaining with a well-chosen hash function and dynamic resizing. By maintaining a low load factor through resizing, the hash table minimizes collisions and ensures efficient performance across operations. The use of chaining for collision resolution further ensures that even in the presence of collisions, operations remain quick. 


Summary of Priority Queue implementation findings
-----------------------------------------------------
The array-based max-heap is an optimal choice for implementing a priority queue for task scheduling due to its efficient insertions, extractions, and priority modifications. The design ensures that high-priority tasks are scheduled promptly, making the system suitable for real-time applications where task prioritization is crucial. The modular design of the Task class and heap operations allows for easy extensions and integration into larger systems. 

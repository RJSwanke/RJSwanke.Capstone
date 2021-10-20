## Data Structures and Algorithms (CS-365: Operating Environments)

[Multithreads: Pre-Enhancements](https://github.com/RJSwanke/RJSwanke.github.io/tree/main/Multithreads%20-%20Pre-Enhancement)
	
[Multithreads: Final](https://github.com/RJSwanke/RJSwanke.github.io/tree/main/Multithreads)

#### Artifact explanation:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This artifact is a program that tests your implementation that lists all thread groups and threads within each group in the JVM.

#### Reason for inclusion in portfolio:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I decided to include this project in my ePortfolio because it shows my proficiency within the Java programming language and being able to call on outside functions to create threads within the original. Java has been and still is one of the most commonly used object-oriented programming languages in the world. By showing my familiarity with Java it will also show that I understand things like software architecture, proper coding standards and other rules that the community follows. Java is one of the most common languages and I want to show my familiarity with it.

#### What the program does: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The program aka the threading event object allows one thread to signal an event while an unlimited amount of other threads can be waiting for that event to happen. The key usage in this code is that the threads that are waiting for the event do not necessarily need to stop what they are doing, they can just check the status of the event every once in a while.

#### Changes:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The first couple improvements that I did was to move the .java documents to the proper folders and take out any unnecessary things like on line 64 new CreateThreadGroups(); was not being used. Next I reformatted the for-loops too:
for (ThreadGroup groupList1 : groupList) {
	//create thread array with double active threads
            	Thread[] list = new Thread[groupList1.activeCount() * 2];
            	groupList1.enumerate(list, false);
	//print group name
	//print list of threads in the groups and their status
            	System.out.println(groupList1.getName());
                	for (Thread list1 : list) {
                    	if (list1 != null) {
                        	System.out.println("\t" + list1.getName() + ":" + list1.getId() + ":" + list1.getState() + ":" + list1.isDaemon());
                    	}

As these for-loops are better structured, read better and are more secure. 
```
for (ThreadGroup groupList1 : groupList) {
	//create thread array with double active threads
            	Thread[] list = new Thread[groupList1.activeCount() * 2];
            	groupList1.enumerate(list, false);
	//print group name
	//print list of threads in the groups and their status
            	System.out.println(groupList1.getName());
                	for (Thread list1 : list) {
                    	if (list1 != null) {
                        	System.out.println("\t" + list1.getName() + ":" + list1.getId() + ":" + list1.getState() + ":" + list1.isDaemon());
                    	}

```
#### What I learned: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;These for-loops are better structured this way, they read better and are more secure. After correcting the structure I added to the comments and made sure they were easy to read and not hard to find. I believe that I enhanced this project so that now it is a nice polish project that I am proud to have in my ePortfolio. Reflecting on the process of enhancing and/or modifying my artifact taught me that even though I don't fully understand what is going on, I am still able to read the code and notes to figure out anything I don't understand. With every project I enhance I become more familiar with what a solid software program's code is supposed to look like.    

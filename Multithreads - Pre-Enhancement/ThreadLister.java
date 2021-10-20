/**
 * List all thread groups and threads in each group in the JVM.
 *
 * @author Gagne, Galvin, Silberschatz
 * Operating System Concepts with Java - Eighth Edition
 * Copyright John Wiley & Sons - 2010.
 */

public class ThreadLister
{
	ThreadGroup rootThreadGroup = null;
 
	
	ThreadGroup getRootThreadGroup( ) {
    		if ( rootThreadGroup != null )
        		return rootThreadGroup;
    		ThreadGroup currentThreadGroup = Thread.currentThread( ).getThreadGroup( );
    		ThreadGroup parentThreadGroup;
    		while ( (parentThreadGroup = currentThreadGroup.getParent( )) != null )
        		currentThreadGroup = parentThreadGroup;

		rootThreadGroup = currentThreadGroup;

    		return rootThreadGroup;
	}

	// retrieve all thread groups
	ThreadGroup[] getAllThreadGroups( ) {
    		final ThreadGroup root = getRootThreadGroup( );

			// retrieve number of active groups in thread group
   		int alloc = root.activeGroupCount( );

		// creat new group
    		int n = 0;
    		ThreadGroup[] groups;
    		do {
			// double the active count
                        	// creates new group with new count
        		alloc *= 2;
        		groups = new ThreadGroup[alloc];

			// copies into targeted root
                        // returns the number of thread groups put into root
                        // continues until desired number of groups is reached
        		n = root.enumerate(groups, true);
    		} while (n == alloc);

		   // create new threadgroup array that is one larger                
    		ThreadGroup[] allGroups = new ThreadGroup[n+1];

		   // store root at 0
    		allGroups[0] = root;

		   // copy groups from group variables to allGroups
                   // starts at index position 1
    		System.arraycopy( groups, 0, allGroups, 1, n );

    		return allGroups;
	}

	public static void main(String[] args) {
		
		new CreateThreadGroups();
		
		ThreadLister groups = new ThreadLister();

			// retrieve threadgroup by name
		ThreadGroup[] groupList = groups.getAllThreadGroups();

		// iterate over all known groups
		for (int i = 0; i < groupList.length; i++) {
			// create thread array with double active threads
			Thread list[] = new Thread[groupList[i].activeCount() * 2];
			groupList[i].enumerate(list, false);
		
			// print group name
                        // print list of threads in the groups and their status
			System.out.println(groupList[i].getName());
			for (int j = 0; j < list.length; j++) {
				if (list[j] != null)
					System.out.println("\t"+list[j].getName()+":"+list[j].getId()+":"+list[j].getState()+":"+list[j].isDaemon());
			}
		}
	}
}

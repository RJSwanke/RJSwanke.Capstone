/**
 * A program that tests your implementation that
 * lists all thread groups 
 * - and threads within each group -
 * in the JVM.
 */


public class CreateThreadGroups
{
	public CreateThreadGroups() {
		// create ThreadGroups alpha, beta, theta
		ThreadGroup alpha = new ThreadGroup("alpha");
		ThreadGroup beta = new ThreadGroup("beta");
		ThreadGroup theta = new ThreadGroup(alpha, "theta");

		// create threads for each threadgroup. 
                // first argument is the threadgroup name 
                // second argument is the Runnable implements class                 	
		(new Thread(alpha, new GroupWorker())).start();
		(new Thread(alpha, new GroupWorker())).start();
		(new Thread(alpha, new GroupWorker())).start();
		(new Thread(beta, new GroupWorker())).start();
		(new Thread(theta, new GroupWorker())).start();
		(new Thread(theta, new GroupWorker())).start();
	}

	class GroupWorker implements Runnable
	{
		public void run() {
			while (true) {
				try {
					Thread.sleep(1000);
					for (int i = 0; i < 1000000; i++)
						;
				}
				catch (InterruptedException ie) { }
			}
		}
	}
}

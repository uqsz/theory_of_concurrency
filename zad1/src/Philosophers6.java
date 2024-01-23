
import java.util.concurrent.Semaphore;
public class Philosophers6 {
    public static class Philosopher implements Runnable {
        protected final Object leftFork;
        protected final Object rightFork;
        private Semaphore arbiter;
        protected int id;
        private double totalTime=0;
        private int N=0;
        private double seconds;

        public Philosopher(Object leftFork, Object rightFork, int id, Semaphore arbiter, double seconds) {
            this.leftFork = leftFork;
            this.rightFork = rightFork;
            this.id = id;
            this.arbiter = arbiter;
            this.seconds = seconds;
        }
        @Override
        public void run() {
            long startTime;
            long endTime;
            double start = System.currentTimeMillis();
            double end = start + seconds * 1000;
            while(System.currentTimeMillis() < end){
                startTime = System.nanoTime();
                if (arbiter.tryAcquire()) {
//                    System.out.println("ID: " + id + " left");
                    synchronized (leftFork) {
//                        System.out.println("ID: " + id + " right");
                        synchronized (rightFork) {
//                            System.out.println("ID: " + id + " BOTH");
                        }
                    }
                    arbiter.release();
                } else {
//                    System.out.println("ID: " + id +" is in the corridor");
//                    System.out.println("ID: " + id + " right");
                    synchronized (rightFork) {
//                        System.out.println("ID: " + id + " left");
                        synchronized (leftFork) {
//                            System.out.println("ID: " + id + " BOTH");
                        }
                    }
                }
                endTime = System.nanoTime();
                totalTime += endTime - startTime;
                N+=1;
            }
        }
    }
    public static double Test(int n) {

        Philosopher[] philosophers = new Philosopher[n];
        Object[] forks = new Object[philosophers.length];
        Thread[] threads = new Thread[philosophers.length];

        double seconds = 0.1;

        for (int i = 0; i < forks.length; i++) {
            forks[i] = new Object();
        }

        Semaphore arbiter = new Semaphore(n-1);

        for (int i = 0; i < philosophers.length; i++) {
            Object leftFork = forks[i];
            Object rightFork = forks[(i + 1) % forks.length];

            philosophers[i] = new Philosopher(leftFork, rightFork, i, arbiter, seconds);

            threads[i] = new Thread(philosophers[i]);
            threads[i].start();
        }
        try {
            for (Thread thread : threads) {
                thread.join();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        double avgTime=0;

        for (Philosopher philosopher : philosophers) {
            avgTime+=philosopher.totalTime/philosopher.N;
        }
        avgTime/=n;
//        System.out.println(avgTime);
        return avgTime;
    }
}

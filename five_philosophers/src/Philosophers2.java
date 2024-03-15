import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Philosophers2 {
    public static class Philosopher implements Runnable {
        protected Lock leftFork;
        protected Lock rightFork;
        protected int id;
        private double totalTime=0;
        private int N=0;
        private double seconds;

        public Philosopher(Lock leftFork, Lock rightFork, int id, double seconds) {
            this.leftFork = leftFork;
            this.rightFork = rightFork;
            this.id = id;
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
                while (!(leftFork.tryLock() && rightFork.tryLock())) {
                    if (System.currentTimeMillis() > end){
                        endTime = System.nanoTime();
                        totalTime += endTime - startTime;
                        N+=1;
                        return;
                    }
                }
//                System.out.println("ID: " + id + " both");
                leftFork.unlock();
                rightFork.unlock();
                endTime = System.nanoTime();
                totalTime += endTime - startTime;
                N+=1;
            }
        }
    }


    public static double Test(int n) {

        Philosopher[] philosophers = new Philosopher[n];
        Lock[] forks = new Lock[philosophers.length];
        Thread[] threads = new Thread[philosophers.length];

        double seconds = 0.1;

        for (int i = 0; i < forks.length; i++) {
            forks[i] = new ReentrantLock();
        }

        for (int i = 0; i < philosophers.length; i++) {
            Lock leftFork = forks[i];
            Lock rightFork = forks[(i + 1) % forks.length];

            philosophers[i] = new Philosopher(leftFork, rightFork, i,seconds);

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

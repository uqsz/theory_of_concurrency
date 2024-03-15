public class Philosophers3 {
    public static class Philosopher implements Runnable {
        protected Object leftFork;
        protected Object rightFork;
        private Object first;
        private Object second;
        private String f;
        private String s;
        private int id;
        private double totalTime=0;
        private int N=0;
        private double seconds;

        public Philosopher(Object leftFork, Object rightFork, int id, double seconds) {
            this.leftFork = leftFork;
            this.rightFork = rightFork;
            this.id = id;
            this.seconds = seconds;
        }
        @Override
        public void run() {
            long startTime;
            long endTime;
            if (id%2 == 0){
                first = leftFork;
                f = " left";
                second = rightFork;
                s = " right";
            }else{
                first = rightFork;
                f = " right";
                second = leftFork;
                s = " left";
            }
            double start = System.currentTimeMillis();
            double end = start + seconds * 1000;
            while(System.currentTimeMillis() < end){
                startTime = System.nanoTime();
//                System.out.println("ID: " + id + f);
                synchronized (first){
//                    System.out.println("ID: " + id + s);
                    synchronized (second){
//                        System.out.println("ID: " + id + " BOTH");
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

        for (int i = 0; i < philosophers.length; i++) {
            Object leftFork = forks[i];
            Object rightFork = forks[(i + 1) % forks.length];

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

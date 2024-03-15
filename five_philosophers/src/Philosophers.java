public class Philosophers {
    public static class Philosopher implements Runnable {
        protected Object leftFork;
        protected Object rightFork;
        protected int id;
        private double seconds;

        public Philosopher(Object leftFork, Object rightFork, int id, double seconds) {
            this.leftFork = leftFork;
            this.rightFork = rightFork;
            this.id = id;
            this.seconds = seconds;
        }
        @Override
        public void run() {
            double start = System.currentTimeMillis();
            double end = start + seconds * 1000;
            while(System.currentTimeMillis() < end){
                System.out.println("ID: " + id + " left");
                synchronized (leftFork){
                    System.out.println("ID: " + id + " right");
                    synchronized (rightFork){
                        System.out.println("ID: " + id + " both");
                    }
                }
            }
        }
    }
    public static void Test(int n) {

        Philosopher[] philosophers = new Philosopher[n];
        Object[] forks = new Object[philosophers.length];
        Thread[] threads = new Thread[philosophers.length];

        double seconds = 1.1;

        for (int i = 0; i < forks.length; i++) {
            forks[i] = new Object();
        }

        for (int i = 0; i < philosophers.length; i++) {
            Object leftFork = forks[i];
            Object rightFork = forks[(i + 1) % forks.length];

            philosophers[i] = new Philosopher(leftFork, rightFork, i, seconds);

            threads[i] = new Thread(philosophers[i]);
            threads[i].start();
        }
    }
}

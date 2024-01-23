import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        int numberOfTests = 10;
        double[][] results = new double[12][numberOfTests];

        for (int i = 1; i <= 12; i++) {
            for (int j = 0; j < numberOfTests; j++) {
                results[i - 1][j] = Philosophers6.Test(i * 25);
            }
        }

        try (FileWriter writer = new FileWriter("results6.csv")) {
            for (int i = 0; i < results.length; i++) {
                for (int j = 0; j < results[i].length; j++) {
                    writer.append(String.valueOf(results[i][j]));
                    if (j < results[i].length - 1) {
                        writer.append(',');
                    }
                }
                writer.append('\n');
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");


        for (int i = -1; i < 2; i++) {
            for (int j = -1; j < 2; j++) {
                if (Math.abs(i + j) == 1) {
                    System.out.println("[ "+i+" , "+j+" ]");
                }
            }
        }
    }
}
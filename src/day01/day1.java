package day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class day1 {


    public static void main(String[] args) throws Exception {
        System.out.println("Day 1: Historian Hysteria");

        List<Integer> first = new ArrayList<>();
        List<Integer> second = new ArrayList<>();

//        try (BufferedReader br = new BufferedReader(new FileReader("src/day1/data.csv"))) {
//            String line;
//            while ((line = br.readLine()) != null) {
//                String[] values = line.split(" {3}");
//                first.add(Integer.parseInt(values[0]));
//                second.add(Integer.parseInt(values[1]));
//            }
//        }


        List<String> data = Files.readAllLines(Path.of("src/day1/data.csv"));
        for (String s : data) {
            String[] values = s.split(" {3}");
            first.add(Integer.parseInt(values[0]));
            second.add(Integer.parseInt(values[1]));
        }

        Collections.sort(first);
        Collections.sort(second);

        // --- part 1
        int num = 0;
        for (int i = 0; i < first.size(); i++) {
            num += Math.abs(first.get(i)-second.get(i));
        }
        System.out.println("First part : "+num);

        // --- part 2
        Map<Integer, Integer> map = new HashMap<>();
        for (int integer : second) {
            map.put(integer, map.getOrDefault(integer, 0) + 1);
        }
        num = 0;
        for (int i : first){
            if (map.containsKey(i)){
                num+=i*map.get(i);
            }
        }
        System.out.println("Second part : "+num);

    }
}

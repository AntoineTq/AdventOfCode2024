package day2;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class day2 {


    public static boolean isSafe(ArrayList<Integer> arr, boolean isDampener){

        boolean increasing = arr.get(1) >= arr.get(0);
        for (int i = 0; i < arr.size()-1; i++) {
            boolean condition = (increasing ? (arr.get(i+1) <= arr.get(i)) : (arr.get(i+1) >= arr.get(i)))
                                || Math.abs(arr.get(i+1) - arr.get(i)) > 3;
            if (condition) {
                if (isDampener) {
                    for (int j = 0; j <= i+1; j++) {
                        ArrayList<Integer> a = new ArrayList<>(arr);
                        a.remove(j);
                        if (isSafe(a, false)) return true;
                    }
                }
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        System.out.println("Day 2: Red-Nosed Reports");

        List<String> list = Files.readAllLines(Path.of("src/day2/data.txt"));
        
        // Part 1 : count safe
        int nSafe = 0;
        for( String level : list){
            String[] strArr = level.split(" ");
            ArrayList<Integer> arr = new ArrayList<>();
            for (String s : strArr) arr.add(Integer.parseInt(s));
            if (isSafe(arr,false)) nSafe++;
        }
        System.out.println(nSafe);


        // Part 2 : better safe
        nSafe = 0;
        for( String level : list){
            String[] strArr = level.split(" ");
            ArrayList<Integer> arr = new ArrayList<>();
            for (String s : strArr) arr.add(Integer.parseInt(s));
            if (isSafe(arr,true)) nSafe++;
        }
        System.out.println(nSafe);

    }
}

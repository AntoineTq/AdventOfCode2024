package day4;

import java.awt.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.List;

public class Code {


    public static int nXmas(List<List<String>> array, int x, int y) {
        int count = 0;
        //Horizontal + vertical
        for (int i = -1; i < 2; i++) {
            for (int j = -1; j < 2; j++) {
                if (Math.abs(i + j) == 1) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = 0; k < 4; k++) {
                        if (x + k * i < 0 || x + k * i >= array.size() || y + k * j < 0 || y + k * j >= array.get(x).size()) {
                            break;
                        }
                        sb.append(array.get(x + k * i).get(y + k * j));
                    }
                    if (sb.toString().equals("XMAS")) {
                        count += 1;
                    }
                }
            }
        }

        //diagonale
        for (int i = -1; i < 2; i++) {
            for (int j = -1; j < 2; j++) {
                if (i != 0 && j != 0) {
                    StringBuilder sb = new StringBuilder();
                    for (int k = 0; k < 4; k++) {
                        if (x + k * i < 0 || x + k * i >= array.size() || y + k * j < 0 || y + k * j >= array.get(x).size()) {
                            break;
                        }
                        sb.append(array.get(x + k * i).get(y + k * j));
                    }
                    if (sb.toString().equals("XMAS")) {
                        count += 1;
                    }
                }
            }
        }

        return count;
    }

    public static int nMasX(List<List<String>> array, int x, int y) {
        //Check bounds
        if (x - 1 < 0 || x + 1 >= array.size() || y - 1 < 0 || y + 1 >= array.get(x).size()) {
            return 0;
        }

        //Diag 1
        String a = array.get(x-1).get(y-1);
        String b = array.get(x+1).get(y+1);

        //Diag 2
        String c = array.get(x-1).get(y+1);
        String d = array.get(x+1).get(y-1);

        if (!((a.equals("M") && b.equals("S")) || (a.equals("S") && b.equals("M")))) return 0;
        if (!((c.equals("M") && d.equals("S")) || (c.equals("S") && d.equals("M")))) return 0;
        return 1;
    }


    public static void main(String[] args) throws IOException {
        System.out.println("--- Day 4: Ceres Search ---");

        List<String> list = Files.readAllLines(Path.of("src/day4/data.txt"));
        List<List<String>> array = new ArrayList<>();
        for (String str : list) {
            array.add(new ArrayList<>(Arrays.asList(str.split(""))));
        }

        //Part 1
        int result1 = 0;
        for (int i = 0; i < array.size(); i++) {
            for (int j = 0; j < array.get(i).size(); j++) {
                if (array.get(i).get(j).equals("X")) {
                    result1 += nXmas(array, i, j);
                }
            }
        }
        System.out.println(result1);

        //Part 2
        int result2 = 0;
        for (int i = 0; i < array.size(); i++) {
            for (int j = 0; j < array.get(i).size(); j++) {
                if (array.get(i).get(j).equals("A")) {
                    result2 += nMasX(array, i, j);
                }
            }
        }
        System.out.println(result2);

    }
}

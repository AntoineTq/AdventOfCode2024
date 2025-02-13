package day3;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Code {


    public static void main(String[] args) throws IOException {
        System.out.println("--- Day 3: Mull It Over ---");


        List<String> data = Files.readAllLines(Path.of("src/day3/data.txt"));


        Pattern patternMul = Pattern.compile("mul\\(\\d{1,3},\\d{1,3}\\)");
        int result1 = 0;
        for (String str: data){
            Matcher m = patternMul.matcher(str);
            while (m.find()){
                String s = m.group().replace("mul(", "").replace(")","");
                String[] arr = s.split(",");
                result1 += Integer.parseInt(arr[0]) * Integer.parseInt(arr[1]);
            }
        }
        System.out.println(result1);

        Pattern pattern2 = Pattern.compile("mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)");
        int result2 = 0;
        boolean enabled = true;
        for (String str: data){
            Matcher m = pattern2.matcher(str);
            while (m.find()){
                if (m.group().equals("do()")) enabled = true;
                else if (m.group().equals("don't()")) enabled = false;
                else if (enabled){
                    String s = m.group().replace("mul(", "").replace(")", "");
                    String[] arr = s.split(",");
                    result2 += Integer.parseInt(arr[0]) * Integer.parseInt(arr[1]);
                }
            }
        }
        System.out.println(result2);

    }
}

package day7;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Code {

    public static long testCalibrationPart1(List<Long> values, long answer, long current) {
        List<Long> copy = new ArrayList<>();
        copy.addAll(values);
        if (values.isEmpty()) {
            return current == answer ? answer : 0;
        } else {
            long number = copy.removeFirst();
            if (testCalibrationPart1(copy, answer, current + number) == answer) return answer;
            if (testCalibrationPart1(copy, answer, current == 0 ? number : current * number) == answer) return answer;
        }
        return 0;
    }

    public static long testCalibrationPart2(List<String> values, long answer, long current) {
        List<String> copy = new ArrayList<>();
        copy.addAll(values);
        if (values.isEmpty()) {
            return current == answer ? answer : 0;
        } else {
            long number = Long.parseLong(copy.removeFirst());
            if (testCalibrationPart2(copy, answer, current + number) == answer) return answer;
            if (testCalibrationPart2(copy, answer, current == 0 ? number : current * number) == answer) return answer;
            if (testCalibrationPart2(copy, answer, Long.parseLong(current + String.valueOf(number))) == answer) return answer;
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        System.out.println("--- Day 7: Bridge Repair ---");

        List<String> data = Files.readAllLines(Path.of("src/day7/data.txt"));

        //Part 1
        long result = 0;
        for (String str : data) {
            String[] tmp = str.replace(":", "").split(" ");
            List<Long> values = new LinkedList<>();
            long answer = Long.parseLong(tmp[0]);
            for (int i = 1; i < tmp.length; i++) {
                values.add(Long.parseLong(tmp[i]));
            }
            result += testCalibrationPart1(values, answer, 0);
        }
        System.out.println(result);

        //Part 2
        result = 0;
        for (String str : data) {
            String[] tmp = str.replace(":", "").split(" ");
            List<String> values = new ArrayList<>(List.of(tmp));
            values.removeFirst();
            long answer = Long.parseLong(tmp[0]);
            result += testCalibrationPart2(values, answer, 0);
        }
        System.out.println(result);
    }
}

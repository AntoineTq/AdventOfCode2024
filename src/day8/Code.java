package day8;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Code {

    public static Set<List<Integer>> checkAntinodes(List<List<Integer>> positions, int nline, int lineLength, boolean isMulti) {
        Set<List<Integer>> antinodes = new HashSet<>();
        //System.out.println(positions);

        int[][] directions = {
                {-1, -1}, {1, 1}, // Directions for x1, y1
                {-1, -1}, {1, 1}  // Directions for x2, y2
        };

        for (int i = 0; i < positions.size(); i++) {
            int x1 = positions.get(i).getFirst();
            int y1 = positions.get(i).getLast();
            for (int j = i; j < positions.size(); j++) {
                int x2 = positions.get(j).getFirst();
                int y2 = positions.get(j).getLast();
                if (i != j) {
                    int[][] points = {
                            {x1, y1},
                            {x2, y2}
                    };
                    int xDiff = x2 - x1;
                    int yDiff = y2 - y1;
                    for (int[] point : points) {
                        for (int[] dir : directions) {
                            int count = 1;
                            while(true){
                                int newX = point[0] + dir[0] * xDiff * count;
                                int newY = point[1] + dir[1] * yDiff * count;
                                if (newX >= 0 && newY >= 0 && newX < nline && newY < lineLength) {
                                    antinodes.add(new ArrayList<>(List.of(newX, newY)));
                                    count++;
                                    if (!isMulti) break;
                                }
                                else {
                                    break;
                                }
                            }

                        }
                    }
                }
            }
        }
        //System.out.println("antinodes =" + antinodes);
        return antinodes;
    }

    public static void main(String[] args) throws IOException {
        System.out.println("--- Day 8: Resonant Collinearity ---");

        List<String> data = Files.readAllLines(Path.of("src/day8/data.txt"));
        Map<Character, List<List<Integer>>> listFreq = new HashMap<>();
        int nline = 0;
        int lineLength = data.getFirst().length();
        for (String str : data) {
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) != '.') {
                    if (listFreq.containsKey(str.charAt(i))) {
                        listFreq.get(str.charAt(i)).add(new ArrayList<>(List.of(nline, i)));
                    } else {
                        listFreq.put(str.charAt(i), new ArrayList<>());
                        listFreq.get(str.charAt(i)).add(new ArrayList<>(List.of(nline, i)));
                    }
                }
            }
            nline++;
        }
        Set<List<Integer>> antinodes = new HashSet<>();
        int result = 0;
        for (Map.Entry<Character, List<List<Integer>>> e : listFreq.entrySet()) {
            Set<List<Integer>> currentAntinodes = checkAntinodes(e.getValue(), nline, lineLength, false);
            for (List<Integer> l : currentAntinodes) {
                if (!antinodes.contains(l)) {
                    char c = data.get(l.getFirst()).charAt(l.getLast());
                    if (c != e.getKey()) {
                        result++;
                        antinodes.add(l);
                    }
                }
            }
        }
        System.out.println(result);

        antinodes = new HashSet<>();
        result = 0;
        for (Map.Entry<Character, List<List<Integer>>> e : listFreq.entrySet()) {
            Set<List<Integer>> currentAntinodes = checkAntinodes(e.getValue(), nline, lineLength, true);
            for (List<Integer> l : currentAntinodes) {
                if (!antinodes.contains(l)) {
                    char c = data.get(l.getFirst()).charAt(l.getLast());
                    result++;
                    antinodes.add(l);
                }
            }
        }
        System.out.println(result);

    }
}

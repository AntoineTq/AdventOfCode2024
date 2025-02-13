package day6;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.locks.Condition;

public class Code {

    public static boolean Algo(int posVerti, int posHoriz, List<List<String>> map, List<List<Boolean>> visited, boolean isCycleSearch) {
        for (int i = 0; i < map.size(); i++) {
            List<Boolean> tmp = new ArrayList<>(map.getFirst().size());
            for (int j = 0; j < map.getFirst().size(); j++) tmp.add(Boolean.FALSE);
            visited.add(tmp);
        }
        int[][] direction = new int[][]{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int directionIndex = 0;
        visited.get(posVerti).set(posHoriz, Boolean.TRUE);
        int nVisited = 0;
        while (posVerti + direction[directionIndex][0] >= 0
                && posVerti + direction[directionIndex][0] < map.size()
                && posHoriz + direction[directionIndex][1] >= 0
                && posHoriz + direction[directionIndex][1] < map.getFirst().size()) {
            if (nVisited>100000) return true;
            if (map.get(posVerti + direction[directionIndex][0]).get(posHoriz + direction[directionIndex][1]).equals("#")) {
                directionIndex = (directionIndex + 1) % 4;
            } else {
                posVerti += direction[directionIndex][0];
                posHoriz += direction[directionIndex][1];
            }
            if (isCycleSearch){
                if (visited.get(posVerti).get(posHoriz)){
                    nVisited++;
                }
            }
            visited.get(posVerti).set(posHoriz, Boolean.TRUE);


        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        System.out.println("--- Day 6: Guard Gallivant ---");

        List<String> data = Files.readAllLines(Path.of("src/day6/data.txt"));

        List<List<String>> map = new ArrayList<>();
        List<List<Boolean>> visited = new ArrayList<>();
        int posVerti = -1;
        int posHoriz = -1;

        for (int i = 0; i < data.size(); i++) {
            map.add(new ArrayList<>(Arrays.asList(data.get(i).strip().split(""))));
            if (data.get(i).contains("^")) {
                posVerti = i;
                posHoriz = data.get(i).indexOf("^");
            }
        }

        Algo(posVerti, posHoriz, map, visited, false);

        int count = 0;
        for (int i = 0; i < visited.size(); i++) {
            for (int j = 0; j < visited.getFirst().size(); j++) {
                if (visited.get(i).get(j)) {
                    count++;
                }
            }
        }
        System.out.println(count);
        int count2= 0;
        for (int i = 0; i < map.size(); i++) {
            for (int j = 0; j < map.getFirst().size(); j++) {
                if (map.get(i).get(j).equals(".")){
                    map.get(i).set(j, "#");
                    if (Algo(posVerti, posHoriz, map, visited, true)) count2++;
                    map.get(i).set(j, ".");
                }
            }
        }
        System.out.println(count2);

    }
}

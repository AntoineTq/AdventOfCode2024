package day5;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Code {

    public static void addRules(Map<Integer, Set<Integer>> rulesMap, int first, int second){
        if (!rulesMap.containsKey(first)){
            rulesMap.put(first, new HashSet<>());
            rulesMap.get(first).add(second);
        }else {
            rulesMap.get(first).add(second);
        }
    }

    public static int checkUpdate(Map<Integer, Set<Integer>> rulesMap, String update, boolean isPartOne){
        String[] tmp = update.split(",");
        List<Integer> arr = Arrays.stream(tmp).map(Integer::parseInt).toList();
        Set<Integer> verifSet = new HashSet<>();
        for (Integer values : arr){
            for (Integer toCheck : rulesMap.get(values)){
                if (verifSet.contains(toCheck)){
                    return isPartOne ? 0 : reorderUpdate(rulesMap, arr);
                }
            }
            verifSet.add(values);
        }
        return isPartOne ? arr.get(arr.size()/2) : 0;
    }

    public static int reorderUpdate(Map<Integer, Set<Integer>> rulesMap, List<Integer> arr){
        List<Integer> nArr = arr.stream().sorted((x,y)-> {
            if (rulesMap.get(y).contains(x)) return 1;
            if (rulesMap.get(x).contains(y)) return -1;
            return 0;
        }).toList();
        return nArr.get(nArr.size()/2);
    }

    public static void main(String[] args) throws IOException {
        System.out.println("--- Day 5: Print Queue ---");

        List<String> data = Files.readAllLines(Path.of("src/day5/message.txt"));

        Map<Integer, Set<Integer>> rulesMap = new HashMap<>();

        int result1 = 0;
        for(String str : data){
            if (str.contains("|")){
                String[] tmp = str.split("\\|");
                addRules(rulesMap,Integer.parseInt(tmp[0]),Integer.parseInt(tmp[1]));
            } else if (str.contains(",")) {
                result1+=checkUpdate(rulesMap, str, true);
            }
        }
        System.out.println(result1);


        int result2 = 0;
        for(String str : data) {
            if (str.contains(",")) {
                result2 += checkUpdate(rulesMap, str, false);
            }
        }

        System.out.println(result2);
    }
}

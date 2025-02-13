package day9;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;

public class Code {

    public static List<String> createVisual(String input) {
        List<String> arr = new ArrayList<>();
        boolean isEmpty = false;
        long counter = 0;
        for (int i = 0; i < input.length(); i++) {
            long current = Long.parseLong(String.valueOf(input.charAt(i)));
            if (isEmpty) {
                for (int j = 0; j < current; j++) {
                    arr.add(".");
                }
                isEmpty = false;
            } else {
                for (int j = 0; j < current; j++) {
                    arr.add(String.valueOf(counter));
                }
                isEmpty = true;
                counter++;
            }
        }
        return arr;
    }

    public static List<String> updateDisk1(List<String> diskVisu) {
        int left = 0;
        int right = diskVisu.size()-1;
        while (left < right) {
            if (diskVisu.get(left).equals(".")) {
                while (diskVisu.get(right).equals(".")) right--;
                diskVisu.set(left, diskVisu.get(right));
                diskVisu.set(right, ".");
                left++;
            } else {
                left++;
            }
        }
        return diskVisu;
    }

    public static List<String> updateDisk2(List<String> storage){

        Map<String, Integer> fileSizes = new HashMap<>();

        // Calculate file sizes
        for (String s : storage) {
            if (!Objects.equals(s, ".")) {
                fileSizes.put(s, fileSizes.getOrDefault(s, 0) + 1);
            }
        }
        System.out.println(fileSizes);
        List<String> fileIds = new ArrayList<>(fileSizes.keySet());
        fileIds.sort((a, b) -> b.compareTo(a));
        System.out.println(fileIds);

        for(String s : fileIds){
//            System.out.println("before "+s+" "+storage);
            int left = findSpace(storage, fileSizes.get(s), s);
            if (left!=-1){
                int right = storage.size()-1;
                int i = 0;
                while (i!=fileSizes.get(s)){
                    while(!storage.get(right).equals(s)) right--;
                    storage.set(left+i, s);
                    storage.set(right, ".");
                    i++;
                    right--;
                }
            }
//            System.out.println(s+ " "+ left);
//            System.out.println("after "+storage);
        }

        return storage;
    }

    public static int findSpace(List<String> storage, int size, String elem){
        int currSize = 0;
        for (int i = 0; i < storage.size(); i++) {
            if (storage.get(i).equals(elem)) return currSize >= size ? i-size-(currSize-size):-1;
            if (storage.get(i).equals(".")) currSize++;
            else {
                if (currSize >= size) return i-size-(currSize-size);
                currSize = 0;
            }
        }
        return -1;
    }

    public static long getIndex(String str, long pos){
        long result = 0;
        for (int i = 0; i < pos; i++) {
            result+= Integer.parseInt(String.valueOf(str.charAt(i)));
        }
        return result;
    }


    public static long computeChecksum(List<String> disk) {
        long result = 0;
        for (int i = 0; i < disk.size(); i++) {
            if (disk.get(i).equals(".")) continue;
            result += ((long) i * Long.parseLong(disk.get(i)));
        }
        return result;
    }

    public static void swapPos(List<String> visu, long pos, int elem){
        int idx = visu.size()-1;
        while (!visu.get(idx).equals(String.valueOf(elem))) idx--;

        while (visu.get(idx).equals(String.valueOf(elem))){
            visu.set((int)pos, String.valueOf(elem));
            pos++;
            visu.set(idx,".");
            idx--;
        }
    }

    public static void main(String[] args) throws IOException {
        System.out.println("--- Day 9: Disk Fragmenter ---");


        List<String> data = Files.readAllLines(Path.of("src/day9/example.txt"));

        for (String string : data) {
            System.out.println(string);
            List<String> visu = createVisual(string);
            List<String> update = updateDisk1(visu);
            System.out.println(update);
            System.out.println(computeChecksum(update));
        }


//        for (String s : data){
//            List<String> visu = createVisual(s);
//            List<String> update = updateDisk2(visu);
//            System.out.println(update);
//            System.out.println(computeChecksum(update));
//        }
//        [0, 0, 9, 9, 2, 1, 1, 1, 7, 7, 7, ., 4, 4, ., 3, 3, 3, ., ., ., ., 5, 5, 5, 5, ., 6, 6, 6, 6, ., ., ., ., ., 8, 8, 8, 8, ., .]
        for (String string : data){
            System.out.println("step 2");
            System.out.println(string);
            List<String> visu = createVisual(string);
            System.out.println(visu);

            Map<Integer, Integer> mapString = new HashMap<>();
            for (int i = 0; i < string.length(); i+=2) {
                mapString.put(i, i/2);
            }
            Map<String, Integer> mapVisu = new HashMap<>();
            for (int i = 0; i < visu.size(); i++) {
                if (!visu.get(i).equals(".")) mapVisu.putIfAbsent(visu.get(i), i);
            }

            System.out.println(mapString);
            System.out.println(mapVisu);
            int right = string.length()-1;
            while (right>0){
                for (int i = 1; i < right; i+=2) {
                    if (Integer.parseInt(String.valueOf(string.charAt(i))) >= Integer.parseInt(String.valueOf(string.charAt(right)))){
                        long newIndex = getIndex(string,i);
                        System.out.println("for "+mapString.get(right)+" found "+ newIndex);
                        swapPos(visu, newIndex, mapString.get(right));
                        System.out.println(visu);
                        break;
                    }
                }
                right-=2;
            }

        }



    }
}
//6375481092176
//6375481092176

// package Java;
import java.util.*;

public class resumeParse {

	public static void main(String[] args) {
        String line;
        ArrayList<String> keyWords = new ArrayList<String>();
        // Map<String, Integer> keys = new HashMap<String, Integer>();
        TextFileInput file = new TextFileInput(args[0]);
        int score = 0; // number of key words found in the resume
        
        // collecting all the words from the resume into our ArrayList keyWords and HashMap keys
		line = file.readLine();
        while(line != null) {
            String[] words = line.split("[^a-zA-Z0-9']+", -1);
            for(int i = 0; i < words.length; i++) { 
                keyWords.add(words[i]);
                // keys.put(words[i].toLowerCase(), 1); 
            }
            line = file.readLine();
        }

        // checks to see if the key word is in the resume
        // prints to terminal the word and a boolean statement if it is there
        // adds to the resume's scores
        for(int i = 1; i < args.length; i++) {
            Boolean isThere = check1(args[i], keyWords);
            if(isThere) { score++; }
            System.out.println(args[i] + ": " + isThere);
        }
        System.out.println("Number of key words found: " + score);

        // for(int i = 1; i < args.length; i++) {
        //     Boolean isthere2 = check2(args[i], keys);
        //     if(isthere2) { score++; }
        //     System.out.println(args[i] + ": " + isthere2);
        // }
        // System.out.println("Number of key words found: " + score);
    }

    /**
    * checks to see if the key word is in the ArrayList of resume words
    */
    private static Boolean check1(String args, ArrayList<String> keyWords) {
        for(int i = 0; i < keyWords.size(); i++) {
            if(args.equalsIgnoreCase(keyWords.get(i))) {
                return true;
            }
        }
        return false;
    }

    /**
    * checks to see if the key word is in the HashMap of resume words
    */
    // private static Boolean check2(String args, Map<String, Integer> keys) {
    //     if(keys.containsKey(args.toLowerCase())) {
    //         return true;
    //     }
    //     return false;
    // }
}
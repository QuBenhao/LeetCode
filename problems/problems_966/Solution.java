package problems.problems_966;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String[] spellchecker(String[] wordlist, String[] queries) {
        int n = wordlist.length;
        Set<String> origin = new HashSet<>(Arrays.asList(wordlist));
        Map<String, String> lowerToOrigin = new HashMap<>(n); // Preallocate space
        Map<String, String> vowelToOrigin = new HashMap<>(n);

        for (int i = n - 1; i >= 0; i--) {
            String s = wordlist[i];
            String lower = s.toLowerCase();
            lowerToOrigin.put(lower, s); // For example, kite -> KiTe
            vowelToOrigin.put(replaceVowels(lower), s); // For example, k?t? -> KiTe
        }

        for (int i = 0; i < queries.length; i++) {
            String q = queries[i];
            if (origin.contains(q)) { // Exact match
                continue;
            }
            String lower = q.toLowerCase();
            if (lowerToOrigin.containsKey(lower)) { // Case-insensitive match
                queries[i] = lowerToOrigin.get(lower);
            } else { // Case-insensitive match allowing vowel substitutions
                queries[i] = vowelToOrigin.getOrDefault(replaceVowels(lower), "");
            }
        }
        return queries;
    }

    private String replaceVowels(String str) {
        char[] s = str.toCharArray();
        for (int i = 0; i < s.length; ++i) {
            char c = s[i];
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                s[i] = '?';
            }
        }
        return new String(s);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] wordlist = jsonArrayToStringArray(inputJsonValues[0]);
		String[] queries = jsonArrayToStringArray(inputJsonValues[1]);
        return JSON.toJSON(spellchecker(wordlist, queries));
    }
}

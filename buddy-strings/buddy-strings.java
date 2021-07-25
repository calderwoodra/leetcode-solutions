class Solution {
    public boolean buddyStrings(String s, String goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        
        HashSet<Character> found = new HashSet<>();
        boolean foundDoubles = false;
        
        boolean matched = false;
        Character saved1 = null;
        Character saved2 = null;
        for (int i = 0; i < s.length(); i++) {
            Character c1 = s.charAt(i);
            Character c2 = goal.charAt(i);
            
            if (found.contains(c1)) {
                foundDoubles = true;
            } else {
                found.add(c1);
            }
            
            if (c1 == c2) {
                continue;
            }
            
            if (matched) {
                // 3+ cahracters are inconsistent, impossible to swap
                return false;
            }
            
            if (saved1 == null) {
                // We found the first inconsistency, save it
                saved1 = c1;
                saved2 = c2;
                continue;
            }
            
            if (c1 == saved2 && c2 == saved1) {
                // We found the second inconsistency and they are inveses of the first, we're golden
                matched = true;
                continue;
            } else {
                // We found another inconsistency, but they aren't inverses :(
                return false;
            }
        }
        
        if (saved1 == null) {
            return foundDoubles;
        } else {
            return matched;
        }
    }
}
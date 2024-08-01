class Solution {
    public int minimizedStringLength(String s) {
        
        HashSet<Character> set = new HashSet<>();

        int n = s.length();
        for (int i=0; i<n ; i++){
            set.add(s.charAt(i));
        }
        return set.size();
    }
}
  public class Solution {
    public String removeDuplicates(String s) {
        
        StringBuilder r = new StringBuilder();
        
        for (char c : s.toCharArray()){
            if(r.length() > 0 && r.charAt(r.length()-1) == c){
                r.deleteCharAt(r.length()-1);
            }
            else{
                r.append(c);
            }
            }
    
    return r.toString();
}
}
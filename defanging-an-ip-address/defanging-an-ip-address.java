class Solution {
    public String defangIPaddr(String address) {
        StringBuilder sb = new StringBuilder();
        for (Character c : address.toCharArray()) {
            if (c == '.') {
                sb.append("[.]");
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
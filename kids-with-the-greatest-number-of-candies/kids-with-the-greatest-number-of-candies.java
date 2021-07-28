class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int greatest = -1;
        for (int candy : candies) {
            greatest = Math.max(greatest, candy);
        }
        
        List<Boolean> ret = new ArrayList<>();
        for (int candy : candies) {
            ret.add(candy + extraCandies >= greatest);
        }
        return ret;
    }
}
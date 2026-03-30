class Solution {
    public int longestConsecutive(int[] nums) {
        int longest = 0;

        Set<Integer> seen = new HashSet<>();

        for (int n : nums) {
            seen.add(n);
        }

        for (int n : seen) {
            if (!seen.contains(n - 1)) {
                int start = n + 1;

                while (seen.contains(start)) {
                start++;
                }
                longest = Math.max(longest, start - n);
            }
            
        }
        return longest;
    }
}

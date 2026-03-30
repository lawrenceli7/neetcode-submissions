class Solution {
    public int longestConsecutive(int[] nums) {
        int longest = 0;

        Set<Integer> numSet = new HashSet<>();

        for (int n : nums) {
            numSet.add(n);
        }

        for (int n : numSet) {
            if (!numSet.contains(n - 1)) {
                int start = n + 1;

                while (numSet.contains(start)) {
                start++;
                }

                longest = Math.max(longest, start - n);
            }
        }
        return longest;
    }
}

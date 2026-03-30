class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        int res = 0;
        int maxOcc = 0;
        int[] count = new int[26];

        for(int right=0; right<s.length(); right++) {
            count[s.charAt(right) - 'A']++;
            maxOcc = Math.max(maxOcc, count[s.charAt(right) - 'A']);

            if(right - left + 1 - maxOcc > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }

            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}

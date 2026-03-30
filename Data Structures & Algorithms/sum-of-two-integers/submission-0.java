class Solution {
    public int getSum(int a, int b) {
        // xor
        // carry 1's need to shift left by 1, (a & b) << 1
        // then add them together (xor and carry), and repeat, no carry means we are done

        while (b != 0) {
            int temp = (a & b) << 1;
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}

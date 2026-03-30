class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int top = 0;
        int bottom = matrix.length - 1;

        while(top <= bottom) {
            int middle = (top + bottom) / 2;
            if(matrix[middle][0] < target &&
            matrix[middle][matrix[middle].length - 1] > target) {
                break;
            } else if(matrix[middle][0] > target) {
                bottom = middle - 1;
            } else {
                top = middle + 1;
            }
        }

        int row = (top + bottom) / 2;
        int left = 0;
        int right = matrix[row].length - 1;

        while(left <= right) {
            int middle = (left + right) / 2;
            if(matrix[row][middle] == target) {
                return true;
            } else if(matrix[row][middle] > target) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        return false;
    }
}

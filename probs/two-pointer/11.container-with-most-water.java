class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int answer = 0;
        while (l < r) {
            int smaller = height[l] > height[r] ? r: l;
            int area = height[smaller] * (r - l);

            if (area > answer) {
                answer = area;
            }
            if (height[l] > height[r]) {
                r--;
            } else {
                l++;
            }
        }

        return answer;
    }
}

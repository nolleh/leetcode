
class Solution {
    public String convert(String s, int numRows) {

        if (numRows == 1) return s;
        var arr = s.toCharArray();
        var answer = "";
        for (int r = 0; r < numRows; ++r) {
            var increment = (numRows - 1) * 2;
            for (int i = r; i < arr.length; i += increment) {
                answer += arr[i];
                if (r > 0 && r < numRows - 1 && i + increment - 2 * r < arr.length) {
                    answer += arr[i+ increment - 2 * r];
                }
            }

        }
        return answer;
    }
}

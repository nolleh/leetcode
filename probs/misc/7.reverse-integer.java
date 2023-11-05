class Solution {
    public int reverse(int x) {

        int MIN = Integer.MIN_VALUE;
        int MAX = Integer.MAX_VALUE;

        int answer = 0;

        int signature = x > 0 ? 1: -1;
        x = x * signature;
        while (x > 0) {
            int digit = x % 10;
            x /= 10;

            if (answer > MAX / 10 || answer == MAX / 10 && digit >= MAX % 10) {
                return 0;
            }
            if (answer < MIN / 10 || answer == MIN / 10 && digit <= MIN % 10) {
                return 0;
            }

            answer = answer * 10 + digit;
        }

        return answer * signature;
    }
}

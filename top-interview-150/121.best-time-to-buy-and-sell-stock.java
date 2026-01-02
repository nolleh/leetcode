/**
 * 121. Best Time to Buy and Sell Stock
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 *
 * Difficulty: Easy
 *
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 * You want to maximize your profit by choosing a single day to buy one stock and
 * choosing a different day in the future to sell that stock.
 *
 * Return the maximum profit you can achieve from this transaction.
 * If you cannot achieve any profit, return 0.
 *
 * Example 1:
 * Input: prices = [7,1,5,3,6,4]
 * Output: 5
 * Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
 *
 * Example 2:
 * Input: prices = [7,6,4,3,1]
 * Output: 0
 * Explanation: No transactions are done, max profit = 0.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

class Solution {
    public int maxProfit(int[] prices) {
        // TODO: Implement your solution
        // Hint: Think about what you need to track as you iterate through prices
        // Hint: What's the minimum price you've seen so far?
        // Hint: What's the best profit you can make at each price?

        int minimum = prices[0];
        int maximum = 0;

        for (int price : prices) {
            if (price > minimum) {
                maximum = Math.max(maximum, price - minimum);
            } else {
                minimum = price;
            }
        }

        return maximum;
    }
}


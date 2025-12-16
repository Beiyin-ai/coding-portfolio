// 1672. Richest Customer Wealth
// 解題日期: 13天前

class Solution {
    fun maximumWealth(accounts: Array<IntArray>): Int {
        var richest = 0
        for (customer in accounts) {
            var current = 0
            for (wealth in customer) {
                current += wealth
                if (current > richest) {
                    richest = current
                }
            }
        }
        return richest
    }
}

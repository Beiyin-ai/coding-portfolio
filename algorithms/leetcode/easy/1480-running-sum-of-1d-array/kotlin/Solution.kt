// 1480. Running Sum of 1d Array
// 解題日期: 13天前

class Solution {
    fun runningSum(nums: IntArray): IntArray {
        val result = mutableListOf<Int>()
        var sum = 0
        for (num in nums) {
            sum += num
            result.add(sum)
        }
        return result.toIntArray()
    }
}

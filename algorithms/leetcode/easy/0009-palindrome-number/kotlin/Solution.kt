// 9. Palindrome Number
# 解題日期: 13天前

class Solution {
    fun isPalindrome(x: Int): Boolean {
        val str = x.toString()
        return str == str.reversed()
    }
}

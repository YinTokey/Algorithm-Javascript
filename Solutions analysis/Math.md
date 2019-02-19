# 数学题
##### 不用加减乘除做加法
剑指offer第6章。python位运算比较坑，这题可以用JavaScript来解决
总结起来就是异或运算，与运算，位移。然后再一直循环。
```
function Add(num1, num2)
{
    var sum, carry;
    while(num2 != 0){
        sum = num1 ^ num2;
        carry = (num1 & num2) << 1;
        num1 = sum;
        num2 = carry;
    }
    return num1;
}
```
##### 孩子们的游戏
参照牛客网的剑指offer专题。核心思路是建立循环链表，然后在循环链表中进行删除节点的操作。也就是约瑟夫环。这里提供一个思路，没能全部通过，应该只是语法问题
```
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        head = ListNode(0)
        first = head
        for i in range(1,n):
            listHead = ListNode(i)
            head.next = listHead
            head = head.next
        head.next = first
        while first.next is not None:
            for i in range(m-1):
                first = first.next
            tmp = first.next
            first = first.next.next
            tmp.next = None
        return first.val
```
##### 扑克牌顺子
题目： https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4?tpId=13&tqId=11198&tPage=3&rp=3&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
解题思路：
https://blog.csdn.net/fuxuemingzhu/article/details/79702017
`核心思路`：先给数组排序，确定0的个数。让后统计间距总和，如果间距总和小于等于0，那么说明可以用0来添补间距从而构成顺子。

```
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        zeros = numbers.count(0)
        gaps = 0
        small = zeros
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            gaps += numbers[big]-numbers[small]-1
            small = big
            big += 1
        return zeros >= gaps
```

##### 回文数判断
https://leetcode.com/problems/palindrome-number/discuss/5188/O(1)-space-O(lgn)-time-java-solution-no-overflow-risk

使用O(1)空间复杂度来解决。其实翻转整数，也可以是这个思路。

其实这类题目，要求O(1)空间复杂度的，有两种解决思路：1.利用指针标志   2.做积累性数学运算

这题就是做积累性运算
```
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 拆开，转成数组，检查回文数组即可
        
        # 来一波O(1)空间复杂度解法
        p = x
        q = 0
        while p > 0:
            q = q*10 + p%10
            p /=10
            
        return q == x
```

##### 求三个数中位数
```
def middle(a,b,c):
    max = a
    min = a
    if b < min:
        min = b
    else:
        max = b
    if c < min:
        min = c
    elif c > max:
        max = c
    else:
        print("min<c<max")

    return a+b+c-max-min

```


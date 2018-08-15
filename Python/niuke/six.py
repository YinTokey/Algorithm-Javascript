# -*- coding:utf8 -*-

# 38 数字k在排序数组中出现的次数
# 思路：通过运行两次二分查找，分别找到第一个k和最后一个k。 时间复杂度为 O(logn)
def findFirst(start,end,k,array):
    if(start > end):
        return -1

    midIndex = (start + end) // 2
    midValue = array[midIndex]

    if(midValue == k):
        if(midIndex > 0 and array[midIndex -1] != k or midIndex == 0):
            # midIndex = 0说明二分查找的子数组只有一个元素，那个元素刚好就是第一个K
            return midIndex
        else:
            # 不是第一个K,说明前面还有k, 继续二分查找
            end = midIndex -1

    elif(midValue > k):
        end = midIndex -1
    else:
        start = midIndex + 1

    return findFirst(start,end,k,array)

def findLast(start,end,k,array):
    if (start > end):
        return -1

    midIndex = (start + end) // 2
    midValue = array[midIndex]

    if(midValue == k):
         if(midIndex > 0 and array[midIndex + 1] != k or midIndex == len(array)-1):
             return midIndex
         else:
             start = midIndex +1

    elif(midValue > k):
        end = midIndex -1
    else:
        start = midIndex + 1

    return findLast(start,end,k,array)

def findNumOfK(array,k):
    length = len(array)
    if(length <= 1):
        return length
    first = findFirst(0,length-1,k,array)
    last = findLast(0,length-1,k,array)
    num = last - first + 1
    print(first)
    print(last)
    if(num > 0):
        return num
    else:
        return 0

array = [1,2,3,3,3,8,8,9,10,12,25]
num = findNumOfK(array,3)
print(num)
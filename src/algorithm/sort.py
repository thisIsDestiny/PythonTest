#coding=utf-8
import time

def bubbleSort(nums):

    nums_len = len(nums) - 1

    for i in range(nums_len):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(nums_len-i
                       ):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def chooseSort(nums):

    nums_len = len(nums) - 1

    for i in range(0,nums_len):
        for j in range(i,nums_len):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

def time1():
    return  time.clock()#int(round(time.time() * 1000))

def printTimeInterval(func=None,data=None):
    s=time1()
    #print(s)
    #time.sleep(1)
    if(func and data):
        print(func(data))
    e = time1()
    #print(e)
    print(e-s)
    return

nums = [5,2,45,6,8,2,1,0,123,3412,122321123111123]

printTimeInterval(bubbleSort,nums)
#printTimeInterval(chooseSort,nums)
#printTimeInterval()
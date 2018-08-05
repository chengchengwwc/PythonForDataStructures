# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo3.py

#@time: 2018/08/05

from DemoTest.demo2 import swap


def partition(lyst,left,right):
    middle = (left+right)//2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    boundary = left
    for index in range(left,right):
        if lyst[index] < pivot:
            swap(lyst,index,boundary)
            boundary +=1
    swap(lyst,right,boundary)
    return boundary


def quicksortHelper(lyst,left,right):
    if left <right:
        pivolocation = partition(lyst,left,right)
        quicksortHelper(lyst,left,pivolocation-1)
        quicksortHelper(lyst,pivolocation+1,right)

def quicksort(lyst):
    quicksortHelper(lyst,0,len(lyst)-1)


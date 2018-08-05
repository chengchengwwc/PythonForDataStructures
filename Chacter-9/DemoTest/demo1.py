# -*- coding: utf-8 -*-

#@author: weicheng

#@file: demo1.py

#@time: 2018/08/05


def indexOfMin(lyst):
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex


def sequentialSearch(target,lyst):
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return False


def binarySearch(target,sortedLyst):
    left = 0
    right = len(sortedLyst) -1
    while left < right:
        midpoint = (left+right)//2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint -1
        else:
            left = midpoint + 1
    return False






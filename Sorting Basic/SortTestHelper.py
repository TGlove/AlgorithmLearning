#-*- coding: UTF-8 -*-
import random

import time


class SortTestHelper(object):
    # def __init__(self,n,rangeL,rangeR):
    #     self.n = n
    #     self.rangeL = rangeL
    #     self.rangeR = rangeR

    # n list内元素个数 ，random取值范围
    @classmethod
    def generateRandomArray(self,n,rangeL,rangeR):
        array = []
        for i in range(n):
            array.append(random.randint(rangeL,rangeR))
        return array

    #测试算法消耗时间
    @classmethod
    def testTime(self,f):
        start = time.clock()
        f
        end = time.clock()
        c = end-start
        print c
#!/bin/python
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

from __future__ import print_function

import os
import sys

#
# Complete the climbingLeaderboard function below.
#
def climbingLeaderboard(scores, alice):
    #
    # Write your code here.
    #
    scores = list(set(scores))
    scores.sort(reverse = True)
    
    
    res = []
    n = len(scores)
    for ctr in alice:
        left, right = 0, n-1
        flag = True
        while left <= right:
            mid = (left+right)/2
        
            if scores[mid] > ctr:
                left = mid+1
            elif scores[mid] < ctr:
                right = mid-1
            else:
                res.append(mid+1)
                flag = False
                break
        if flag:
            
            res.append(left+1)
    
    return res
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    alice_count = int(raw_input())

    alice = map(int, raw_input().rstrip().split())

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

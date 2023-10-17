from typing import List
from queue import Queue
from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    max_i=0
    last_i=len(A)-1
    i=0
    while max_i<last_i:
        if i==max_i and A[max_i]==0:
            return False
        max_i=max(max_i,i+A[i])
        i+=1
    return max_i>=(len(A)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))

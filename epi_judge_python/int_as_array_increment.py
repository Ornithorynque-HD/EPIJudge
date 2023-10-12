from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    retenue=True
    i=-1
    while retenue:
        if i==-len(A)-1:
            return [1]+[0]*len(A)
        else:
            if A[i]==9:
                A[i]=0
                i=(i-1)
            else:
                A[i]+=1
                retenue=False 
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))

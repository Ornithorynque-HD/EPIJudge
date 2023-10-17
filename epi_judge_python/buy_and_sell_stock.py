from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    n=len(prices)
    benefit=0.0
    for i in range(n):
        for j in range(i,n):
            benefit=max(benefit,prices[j]-prices[i])
    return benefit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))

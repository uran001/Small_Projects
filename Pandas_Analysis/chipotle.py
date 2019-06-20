
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time


def imprt(in_file):

    df = pd.read_csv(in_file, sep='\t')
    print(df)
    return df

def price_to_foat(l):
    for x in range(len(l)):
        l[x] = float(l[x][1:])
    return l

def filt(df, price):
    print(df[df.item_price > price])

def filt_name(df):
    print(df[['item_name', 'item_price']][df.quantity==1])

def create(df):

    mx = int(df['item_price'].max())
    l = list(df['item_price'])
    t = []
    r = []
    for y in range(0, mx, 3):
        r.append(y)
        cur = 0
        for x in range(len(l)):
            if l[x] >= float(y) and l[x] < float(y+3):
               cur += 1
        t.append(cur)
    plt.bar(r,t,align='center')
    plt.xticks(r)
    plt.show()

if __name__ == '__main__':
    data = []
    df = imprt('chipotle_orders.csv')

    df['item_price'] = pd.Series(price_to_foat(list(df['item_price']))).values
    time.sleep(1)
    filt(df, 10)
    time.sleep(1)
    filt_name(df)
    time.sleep(1)
    create(df)






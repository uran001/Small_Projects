# add more imports as appropriate to run your code
import pandas as pd
import json
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib


def imprt(file, file1, file2):
    df1 = pd.read_csv(file, sep=',')
    with open(file1) as json_data:
         df2 = json.load(json_data)
    df3 = pd.read_excel(file2, sep=',')

    ans = []
    for x in range(0, len(df1['Value'])):
        ans.append(df2['dataset']['data'][x][1] + df1['Value'][x] + df3['Value'][x])
        ans[x] /= 3
    print(len(ans), len(df1['Date']))
    plt.bar(list(df1['Date']), ans, align='center')
    plt.xticks(list(df1['Date']))
    plt.show()



if __name__ == '__main__':

    imprt("top_tier.csv", "bottom_tier.json", "middle_tier.xls")

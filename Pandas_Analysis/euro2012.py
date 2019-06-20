import pandas as pd
import matplotlib.pyplot as plt


def imprt(in_file):
    df = pd.read_csv(in_file, sep=',')
    print(df, '\n')
    return df

def columns(df):
    print(df.shape[1], 'columns\n')

def filter(df):
    dis = {}
    dis['Team'] = list(df["Team"])
    dis['Yellow Cards'] = list(df["Yellow Cards"])
    dis['Red Cards'] = list(df["Red Cards"])

    discip = pd.DataFrame(dis)
    print(discip, '\n')
    plt.bar(list(dis['Team']), dis['Yellow Cards'], align='center')
    plt.xticks(dis['Team'])
    plt.show()

    dis_sort = discip.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)

    print('Sorted Dataframe\n', dis_sort)
    print('Average of Yellow Cards: ', float(discip['Yellow Cards'].sum()) / float(discip['Yellow Cards'].count()))
    
if __name__ == '__main__':

    df = imprt('euro2012.csv')
    #columns(df)
    dis = filter(df)
    print(df)


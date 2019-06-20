import matplotlib.pyplot as plt
import pandas as pd


def imprt(registr, ok_mail):
    # full form
    df = pd.read_excel(registr, sep=',')
    df = df.to_dict()

    # ok_mail
    df1 = pd.read_excel(ok_mail, sep=',')
    df1 = df1.to_dict()
    #print(df1)

    # print(df.keys())
    #print(df['Электрондук адресиңиз / Ваша электронная почта'])
    ok = []

    for x in df['Электрондук адресиңиз / Ваша электронная почта']:

        cur = df['Электрондук адресиңиз / Ваша электронная почта'][x]
        cur = cur.split('@')
        cur = cur[0]
        cur = cur.lower()

        # print (cur)
        found = False
        for y in df1['ok']:
            cur1 = df1['ok'][y]
            cur1 = cur1.split('@')
            cur1[0] = cur1[0].lower()
            if (cur == cur1[0]):
                ok.append(cur1[0] +'@'+ cur1[1])
                found = True
                break
        if found == False:
            ok.append('-')
    #print(ok)
    #print(df['Электрондук адресиңиз / Ваша электронная почта'])

    ok_mails = {}
    for x in range (0, len(ok)):
        ok_mails[x] = ok[x]
    df['OK_MAILS'] = ok_mails
    print(df.keys())

    df = pd.DataFrame(data=df)
    print(df)
    df = (df.T)
    df.to_excel("final.xlsx")


if __name__ == '__main__':
    imprt("registr.xlsx", "ok_email.xlsx")

"""
The files GBP2USD.txt and JPY2USD.txt contain historical daily values of GBP (pounds) and JPY (yen) against the US dollar.
For instance, the entry "2017-09-28	112.74" in JPY2USD.txt means that, on sept 28th 2017, it took 112.74 yen to buy 1 US dollar
(or, in other words, that 1 US dollar was worth 112.74)
"""

import datetime as dt
import matplotlib.pyplot as plt
import numpy as np


# wealth calculator
def historical_wealth_calculator(amount, currency, year, month, day):
    """
    This function should calculate the value in US dollars of a certain "amount" (of a given "currency") on a specific date (identified
    by the parameters year, month and day)
    For instance, historical_wealth_calculator(145, "GBP", "2016", "06", "15") should return the value in USD of 145 GBP on June 15 2016
    (The answer is 394.66...)
    Note that, given the data that you are provided, "GBP" and "JPY" are the only possible currencies
    """
    if currency == "GBP":
        file_name = "GBP2USD.txt"
    else:
        file_name = "JPY2USD.txt"

    type = str(year + '-' + month + '-' + day)
    print(type)

    read_file = open(file_name, "r")


    for line in read_file.readlines():  # read lines in file one by one
        values = line.split('\t')  # split the line using separator ','

        if values[0].strip() == type:
            print("New value found in line: {0}".format(values[1].strip()))
            return amount / float(values[1].strip())
    read_file.close()

    return 0


def from_string_to_date(dates):
    """
    This function is GIVEN
    :param dates:
    :return:
    """
    x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]
    return x

def plot_currency(currency):
    """
    This function should plot the value of a given currency ("GBP" or "JPY") on the y axis as a function of
    the date on the x axis
    In this function, you also need to properly a set a title for the plot and labels for each axis
    Note: once you have obtained a list of strings with the dates, e.g. ["2017-10-23", "2017-10-22",...], use
    the given function from_string_to_date() to convert it into a list of "date" objects that can be
    correctly handled by matplotlib
    """

    xx = []
    y = []

    if currency == "GBP":
        file_name = "GBP2USD.txt"
    else:
        file_name = "JPY2USD.txt"


    read_file = open(file_name, "r")

    for line in read_file.readlines():  # read lines in file one by one
        values = line.split('\t')  # split the line using separator ','
        print("New value found in line: {0}".format(values[0].strip()))
        xx.append(values[0].strip())

        print("New value found in line: {0}".format(values[1].strip()))
        y.append(float(values[1].strip()))

    read_file.close()
    xx = from_string_to_date(xx)
    plt.plot(xx, y)

    plt.xlabel('Time')
    plt.ylabel('{0}/USD'.format(currency))

    plt.title('Converter')
    plt.savefig("test.png")
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    plt.show()


def plot_currency_bars_fromdate(currency, fromdate):
    """
    This function should work as plot_currency(), but:
    (i) It plots a "bar chart" instead of a line
    (ii) It plots only data from a certain date "fromdate" until the most recent data available
    (see gbp_fromdate.png for an example outcome from "2016-01-04")
    """
    xx = []
    y = []

    if currency == "GBP":
        file_name = "GBP2USD.txt"
    else:
        file_name = "JPY2USD.txt"

    read_file = open(file_name, "r")

    for line in read_file.readlines():  # read lines in file one by one
        values = line.split('\t')  # split the line using separator ','
        print("New value found in line: {0}".format(values[0].strip()))
        xx.append(values[0].strip())

        print("New value found in line: {0}".format(values[1].strip()))
        y.append(float(values[1].strip()))

    read_file.close()
    xx = from_string_to_date(xx)
    plt.bar(xx,y)

    plt.xlabel('Time')
    plt.ylabel('{0}/USD'.format(currency))

    plt.title('Converter')
    plt.savefig("test1.png")

    plt.show()


if __name__ == "__main__":
    # Test historical_wealth_calculator
    print(historical_wealth_calculator(278, "GBP", "2016", "06", "14"))

    #Test plot (see gbp.png)
    plot_currency("GBP")

    # Test plot from date
    #plot_currency_bars_fromdate("GBP", "2016-01-04")





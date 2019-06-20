"""
Name: Uran Sabyr
Student ID: 20172008

---------------------
Briefly, this project is about Stock Managing in Company.
"""

class StockManager:

    def __init__(self, o_manager):
        """
        Initialises the Stock Manager with the name and surname of the portfolio
        :param o_name: name of the owner of the porfolio
        :param o_surname: surname of the portfolio
        """
        self._manager = o_manager
        self._complist = {}
        self._profit  = 0

    def buy_shares(self, company, number, buy_price):
        """
        Buy stocks
        :param company: the company of which shares are being bought
        :param number: the number of shares to buy
        :param buy_price: the price (per share) at which shares are bought
        """
        if company not in self._complist:
            self._complist[company] = [[]]
        self._complist[company].append([number, buy_price])



    def sell_shares(self, company, o_number, sell_price):
        """
        Sell shares (only if you have enough to sell!)
        :param company: the company of which shares are being bought
        :param number: the number of shares to buy
        :param sell_price: the price (per share) at which shares are sold
        """
        cur = 0
        sold = 0
        number = o_number
        x = self._complist[company]
        x.reverse()

        for c in x:
            if c:
                if number < c[0]:

                    cur += number*(sell_price - c[1])
                    sold += number
                    c[0] -= number
                    number = 0

                elif number >= c[0]:
                    cur += c[0] * (sell_price - c[1])
                    sold += c[0]
                    number -= c[0]
                    c[0] = 0



                ##print(cur, self._profit)
                if number == 0:
                    break
            if number == 0:
                break
        l = [[]]

        for c in x:
            if c and c[0] > 0:
                l.append(c)
        l.reverse()


        self._complist[company] = l
        self._profit += cur
       # print(number)
        if number > 0:
            print("We sold", sold, "stocks and we don't have", number, "stock(s)")
        return cur





    def buy_multiple(self, company_list, number_list, price_list):
        for (x, y, z) in zip(company_list, number_list, price_list):
            if x not in self._complist:
                self._complist[x] = [[]]
            self._complist[x].append([y, z])


    def sell_multiple(self, company_list, number_list, price_list):
        for (x, y, z) in zip(company_list, number_list, price_list):
            self.sell_shares(x, y, z)



    def get_profit(self):
        return self._profit


    """ allows to print the current stock held by the investor (name of stocks, numbers of stocks, and 
    prices at which they were bought)"""
    def print_portfolio(self):
        print('')
        print(self._manager, "has owned")
        print(self._complist)
        print("His/Her Cumulative Profit is", self._profit)




if __name__ == '__main__':
    # extend this code to test all the functions of your portfolio manager
    manager = input("Please input managers Given Name and Surname: ")
    P = StockManager(manager)
    while 1:
        print('')
        print("To Buy Shares type: bs")
        print("To Sell Shares type: ss")
        print("To Get Current Cumulative Profit type: gp")
        print("To Buy Multiple Shares type: bms")
        print("To Sell Shares type: sms")
        print("To Print Portfolio: pp")
        print("To Stop type: stop")
        print('')
        cmd = input("Enter the command: ").strip()
        cmd.lower()
        print('')
        if cmd not in ["bs", "ss", "gp", "bms", "sms", "pp"]:
            print("The command is not found!!!")
            print("Please try again!!!")
        if cmd == 'bs':
            company = input("Enter Company_Name: ").strip(' ')
            number = int(input("Enter Number_of_Stocks: "))
            price = int(input("Enter Price: "))
            P.buy_shares(company, number, price)
            #P.buy_shares("Google", 20, 100)
            #P.buy_shares("Google", 25, 150)
        elif cmd == 'ss':
            while(1):
                company = input("Enter Company_Name: ").strip(' ')

            number = int(input("Enter Number_of_Stocks: "))
            price = int(input("Enter Price: "))

            t = P.sell_shares(company, number, price)
            if t[0]:
                print("Profit: {0}".format(t[1]))
            #print("Profit: {0}".format(P.sell_shares("Google", 31, 127)))
            #print("Profit: {0}".format(P.sell_shares("Google", 2, 23)))

        elif cmd == 'gp':
            print("Current cumulative profit: {0}".format(P.get_profit()))
            #print("Current cumulative profit: {0}".format(P.get_profit()))
            #print("Current cumulative profit: {0}".format(P.get_profit()))
        elif cmd == 'bms':
            company_list = list(input("Enter Company_Name_List: ").split())
            number_list = list(map(int, input("Enter Number_of_Stocks_list: ").split()))
            price_list = list(map(int, input("Enter Prices_List: ").split()))
            P.buy_multiple(company_list, number_list, price_list)
        elif cmd == 'sms':
            company_list = list(input("Enter Company_Name_List: ").split())
            number_list = list(map(int,input("Enter Number_of_Stocks_list: ").split()))
            price_list = list(map(int, input("Enter Prices_List: ").split()))

            P.sell_multiple(company_list, number_list, price_list)
        elif cmd == 'pp':
            P.print_portfolio()
        elif cmd == 'stop':
            break






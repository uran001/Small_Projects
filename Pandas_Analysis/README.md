Chipotle

    The file chipotle_orders.csv contains data about orders at a branch of the world-famous text-mex chain "Chipotle".
    
    1) Import the data into a dataframe

    1bis) The same data can be downloaded at 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

    2) Transform the values in the item_price column into a float.
  
    3) Filter the items that cost more than 10$ and assign them to a new dataframe (how many are these items?)

    4) Create a new dataframe containing only information about item_name and item_price of only items for which
     quantity is equal to 1, removing duplicates

    5) Create a bar chart diagram using the data obtained in (4). Each bar should show the number of items
    found in a certain price interval. Use intervals of 3$
    (see chipotle_result.png for the expected result)

Euro2012
    
    Data about the 2012 edition of the European football championships are available in the file euro2012.csv

    0) Import the data into a dataframe

    1) How many columns are in this dataset?

    2) Filter the columns "Team", "Yellow Cards" and "Red Cards" and assign them to a dataframe called "discipline"

    3) Show a bar chart diagram of the number of yellow cards received by each team
    (see hint_bar_chart.png for a hint...)

    4) Sort the data in "discipline" by red card first, then yellow card and save the sorted data in a dataframe called "disc_sorted"

    5) What is the average number of yellow cards received by a team at Euro 2012?

    6) Create a new dataframe with only data of teams that scored 4 or more goals
HPI
    
     The three files in this directory bottom_tier.json, middle_tier.xls and top_tier.csv contain monthly variations of the house price index
     in Greenville, SC (USA) from 1997 until October 2017 (for instance, the value 0.67 for October 2016 means that average house prices have increased of
     of 0.67% in October 2016 compared to September 2016.
     Top/Middle/Bottom-tier refers to the type of houses (from expensive to cheap).
     Some analysis of the provided data using Pandas, in particular you should do the following:


__author__ = "http://steemit.com/@cervantes"
__copyright__ = "Copyright (C) 2019 steem's @cervantes"
__license__ = "MIT"
__version__ = "1.0"

from beem import Steem


def average(mylist):
    '''Compute median value'''
    sum=0
    for e in mylist:
        sum=sum+int(e)
    
    average_value = (sum/len(mylist))/1000
    return(average_value)

stm = Steem("https://anyx.io")
prop = stm.get_dynamic_global_properties()
#for k in prop:
    #print("%s: %s"%(k,prop[k]))

virtual_supply = int(prop["virtual_supply"]["amount"]) / 1000
current_supply = int(prop["current_supply"]["amount"]) / 1000
current_sbd_supply = int(prop["current_sbd_supply"]["amount"]) / 1000

median_base = int(stm.get_current_median_history()["base"]["amount"]) 
median_quote = int(stm.get_current_median_history()["quote"]["amount"])
median_price = (median_base / median_quote)
prices = [k["base"]["amount"] for k in  stm.get_feed_history()["price_history"]]
median_price = average(prices)
#median_price = 0.45
steem_market_cap = virtual_supply * median_price
debt_ratio = (current_sbd_supply / (virtual_supply * median_price)) * 100
print("\n")
print("################ SBD/STEEM DEBT RATIO #######")
print("virtual_supply: %s Mio STEEM" % str(round((virtual_supply/1000000),2)))
print("current_supply: %s Mio STEEM" % str(round((current_supply/1000000),2)))
print("current_sbd_supply: %s Mio SBD " % str(round((current_sbd_supply/1000000),2)))
print("average_price_feed: %s $" % str(round(median_price,5)))
print("steem_market_cap: %s Mio $" % str(round(steem_market_cap/1000000,3)))
print("debt_ratio: %s %% " % str(round(debt_ratio,4)))
print("#############################################\n")



print("The average feed price is over the last %s : %s " % (len(prices), average(prices)))

#for k in stm.get_feed_history()["price_history"]:
#    print(k["base"]["amount"])



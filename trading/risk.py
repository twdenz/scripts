#!/usr/bin/python3

import csv
import pandas as pd

# risk = float(input("\tRisk percentage:\t"))
risk = 1

print("\nInput Values\n")
tot_acc = float(input("\tTotal account:\t"))
enter = float(input("\tEntry price:\t"))
sl = float(input("\tStop loss:\t"))
print(f"\tAcc. Risk:\t{risk}%")

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def TradeBook(tot_acc, enter, sl, risk, trade_type, pos, max_shares, sl_diff_p, max_loss):
	to_log = input("Do you want to log this trade? (y/n) ").lower()
	try:
		df = pd.read_csv("tradebook.csv")
		print("Im using existing tradebook")
	except:
		df = pd.DataFrame({
			'TradeNr':[], 
			'Date':[], 
			'AccBalance':[], 
			'Enter':[],
			'Stop Loss':[], 
			'Risk':[], 
			'Trade Type':[], 
			'Position Size':[],
			'Max_Shares':[],
			'Sl_diff_p':[], 
			'Max_Loss':[], 
		})
		df.to_csv(path_or_buf = "/mnt/c/Users/ThijmenWijgers/Documents/scripts/trading/tradebook.csv", index=False)



def calculateRisk(tot_acc, enter, sl, risk):
	if enter > sl:
		trade_type = "Long"
	else:
		trade_type = "Short"
	sl_diff = abs(enter-sl)
	sl_diff_p = sl_diff / enter
	risk_abs = (risk/100)*tot_acc
	pos = risk_abs / sl_diff_p
	max_loss =  pos * sl_diff_p
	max_shares = pos / enter
	print()
	print("________________________________\n")
	print("Trade\n")
	print(f"\tTrade Type:\t{trade_type}")
	print(f"\tMax Position:\t{round(pos)}")
	print(f"\tMax Shares:\t{truncate(max_shares)}")
	print(f"\tRisk Perc:\t{round(sl_diff_p*100, 2)}%")
	print(f"\tMax Loss\t{max_loss}\n")
	TradeBook()
		
if __name__ == "__main__":
	calculateRisk(tot_acc, enter, sl, risk)
	



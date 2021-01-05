#!/usr/bin/python3

# This script calculates the risk, max position size, max share size and more and inputs 
# them in the current existing TradeBook. If there is no tradebook the script will make one.

import csv
import pandas as pd
from datetime import datetime

# risk = float(input("\tRisk percentage:\t"))
risk = 0.75
costs= 4.5

print("\nInput Values\n")
tot_acc = float(input("\tTotal account:\t"))
enter = float(input("\tEntry price:\t"))
sl = float(input("\tStop loss:\t"))
print(f"\tAcc. Risk:\t{risk}%")

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def TradeBook(tot_acc, enter, sl, risk, trade_type, pos, max_shares, sl_diff_p, max_loss):
	# Function tries to first open the existing tradebook and otherwise create one. 
	# Then it inserts the new trade depending on the answer of the user.
	to_log = input("Do you want to log this trade? (y/n) ").lower()
	now = datetime.now()
	now_formatted = now.strftime("%d-%m-%Y %H:%M:%S")
	if to_log == 'y':
		asset = input("What is the asset? ").upper()
		try:
			df = pd.read_csv("tradebook.csv")
			current_max_trade = df.max()["TradeNr"] 
			new_trade = {
				'TradeNr':current_max_trade + 1, 
				'Date':now_formatted, 
				'Account Balance':tot_acc, 
				'Enter':enter,
				'Stop Loss':sl, 
				'Total Acc Risk':f"{risk}%", 
				'Trade Type':trade_type, 
				'Position Size':truncate(pos),
				'Max Shares':truncate(max_shares),
				'Stop Loss %':f"{round(sl_diff_p*100, 1)}%", 
				'Max. Loss':max_loss,
				'Asset':asset
			}
			df = df.append(new_trade, ignore_index=True)
			df.to_csv(path_or_buf = "/mnt/c/Users/ThijmenWijgers/Documents/scripts/trading/tradebook.csv", index=False)
			print(f"Your trade has been registered in existing tradebook as trade {current_max_trade +1}")
		except:
			df = pd.DataFrame({
				'TradeNr':[], 
				'Date':[], 
				'Account Balance':[], 
				'Total Acc Risk':[], 
				'Enter':[],
				'Stop Loss':[], 
				'Stop Loss %':[], 
				'Trade Type':[], 
				'Position Size':[],
				'Max Shares':[],
				'Max. Loss':[], 
				'Asset':[]
			})
			new_trade = {
				'TradeNr':1, 
				'Date':now_formatted, 
				'Account Balance':tot_acc, 
				'Enter':enter,
				'Stop Loss':sl, 
				'Total Acc Risk':f"{risk}%", 
				'Trade Type':trade_type, 
				'Position Size':truncate(pos),
				'Max Shares':truncate(max_shares),
				'Stop Loss %':f"{round(sl_diff_p*100, 1)}%", 
				'Max. Loss':max_loss, 
				'Asset':asset
			}
			df = df.append(new_trade, ignore_index=True)
			overwrite = input("Are you sure you want to overwrite existing tradebook? (y/n) ").lower()
			if overwrite == 'y':
				df.to_csv(path_or_buf = "/mnt/c/Users/ThijmenWijgers/Documents/scripts/trading/tradebook.csv", index=False)
				print("Creating new Tradebook and adding your first trade!")


def calculateRisk(tot_acc, enter, sl, risk):
	# Function initiates all the variables needed to calculate the risk and max position
	# After calculation it inputs all the values in the TradeBook function
	if enter > sl:
		trade_type = "Long"
	else:
		trade_type = "Short"
	sl_diff = abs(enter-sl)
	sl_diff_p = sl_diff / enter
	risk_abs = ((risk/100)*tot_acc)-costs
	pos = risk_abs / sl_diff_p
	if pos*2 >= tot_acc:
		pos = tot_acc/2
	max_loss =  round(pos * sl_diff_p, 2) + costs
	max_shares = pos / enter
	print()
	print("________________________________\n")
	print("Trade\n")
	print(f"\tTrade Type:\t{trade_type}")
	print(f"\tMax Position:\t{round(pos, 1)}")
	print(f"\tMax Shares:\t{truncate(max_shares)}")
	print(f"\tSL %:\t\t{round(sl_diff_p*100, 1)}%")
	print(f"\tMax Abs Risk:\t{round(risk_abs, 1)}")
	print(f"\tMin PT % PE:\t{round((costs/pos)*100, 1)}")
	print(f"\tMin Loss:\t{costs}")
	print(f"\tMax Loss:\t{max_loss}\n")
	TradeBook(tot_acc, enter, sl, risk, trade_type, pos, max_shares, sl_diff_p, max_loss)
		
if __name__ == "__main__":
	calculateRisk(tot_acc, enter, sl, risk)
	



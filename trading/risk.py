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
	print()
	print("________________________________\n")
	print("Trade\n")
	print(f"\tTrade Type:\t{trade_type}")
	print(f"\tMax Position:\t{round(pos)}")
	print(f"\tRisk Perc:\t{round(sl_diff_p*100, 2)}%")
	print(f"\tMax Loss\t{max_loss}\n")

def TradeBook():
	to_log = input("Do you want to log this trade? (y/n) ").lower()
	df = pd.read_csv('tradebook.csv')
	max_tradenr = df["TradeNr"].max()
	print(max_tradenr)
	# if to_log == 'y':
		# df_append = pd.DataFrame({
			# "TradeNr":
		# })
		
if __name__ == "__main__":
	calculateRisk(tot_acc, enter, sl, risk)
	TradeBook()



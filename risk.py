#!/usr/bin/python3

print("Input Values")
tot_acc = float(input("\tTotal account:\t"))
enter = float(input("\tEntry price:\t"))
sl = float(input("\tStop loss:\t"))
# risk = float(input("\tRisk percentage:\t"))

risk = 1

def calculate(tot_acc, enter, sl, risk):
	if enter > sl:
		trade_type = "Long"
	else:
		trade_type = "Short"
	sl_diff = abs(enter-sl)
	sl_diff_p = sl_diff / enter
	risk_abs = (risk/100)*tot_acc
	pos = risk_abs / sl_diff_p
	max_loss =  pos * sl_diff_p
	print("________________________________\n")
	print("Trade Values")
	print(f"\tMax Position:\t{pos}")
	print(f"\tRisk Perc.:\t{round(sl_diff_p*100, 2)}")
	print(f"\tMax Loss\t{max_loss}")
	print(f"\tTrade Type:\t{trade_type}")


if __name__ == "__main__":
	calculate(tot_acc, enter, sl, risk)




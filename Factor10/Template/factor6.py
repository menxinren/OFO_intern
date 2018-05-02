#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	factor6 = dv.add_formula('factor6','(2*Ts_Mean(close,30)-Ts_Min(close,30)-Ts_Max(close,30))/Ts_Mean(close,30)',is_quarterly=False, add_data=True)
	return factor6


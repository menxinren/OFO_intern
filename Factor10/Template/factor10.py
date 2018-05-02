#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	factor10 = dv.add_formula('factor10','StdDev(high-low,60)/Ts_Mean(vwap,60)',is_quarterly=False, add_data=True)
	return factor10


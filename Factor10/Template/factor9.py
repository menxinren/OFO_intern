#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	factor9 = dv.add_formula('factor9','Ts_Sum(Return(volume,1) * Return(close,1),5)',is_quarterly=False, add_data=True)
	return factor9


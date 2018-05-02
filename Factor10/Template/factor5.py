#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	factor5 = dv.add_formula('factor5','Return(volume*vwap,120)',is_quarterly=False, add_data=True)
	return factor5


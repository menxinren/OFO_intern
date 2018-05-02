#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	factor7 = dv.add_formula('factor7','(high-vwap)/vwap',is_quarterly=False, add_data=True)
	return factor7


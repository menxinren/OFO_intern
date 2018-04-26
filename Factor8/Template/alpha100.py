#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	alpha100 = dv.add_formula('alpha100', 'StdDev(volume,20)', is_quarterly=False, add_data=True)
	
	return alpha100


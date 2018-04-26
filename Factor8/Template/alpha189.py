#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	alpha189 = dv.add_formula('alpha189', 'Ts_Mean(Abs(close-Ts_Mean(close,6)),6)', is_quarterly=False, add_data=True)
	
	return alpha189


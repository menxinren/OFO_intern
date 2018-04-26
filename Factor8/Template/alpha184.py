#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	alpha184 = dv.add_formula('alpha184', 'Rank(Correlation(Delay((open - close), 1), close, 200)) + Rank((open - close))', is_quarterly=False, add_data=True)
	
	return alpha184


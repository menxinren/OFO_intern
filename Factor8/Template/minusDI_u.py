#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	minusDI_u = dv.add_formula('minusDI_u', 'Ewma(Max(0,Delay(low,1)-low),14)/Ewma(Max(Max(high-low,Abs(high-Delay(close,1))),Abs(low-Delay(close,1))),14)', is_quarterly=False, add_data=True)
	
	return minusDI_u


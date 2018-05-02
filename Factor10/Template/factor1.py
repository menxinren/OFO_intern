#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	dv.add_field('MA5')
	dv.add_field('MA10')
	dv.add_field('MA20')
	dv.add_field('MA60')

	factor1 = dv.add_formula('factor1','Ts_Sum((MA5>MA10)*(MA10>MA20)*(MA20>MA60),20)-Ts_Sum((MA5<MA10)*(MA10>MA20)*(MA20>MA60),20)',is_quarterly=False, add_data=True)
	return factor1


#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	dv.add_field('MA5')
	dv.add_field('MA10')
	dv.add_field('MA20')
	dv.add_field('MA60')

	factor2 = dv.add_formula('factor2','(MA20>MA60&&MA20>MA5&&MA20>MA10&&MA60<MA5&&MA60<MA10)*(Delay(vwap,20)-close) + (MA20<MA60&&MA20<MA5&&MA20<MA10&&MA60>MA5&&MA60>MA10)*(close-Delay(vwap,20))',is_quarterly=False, add_data=True)
	return factor2


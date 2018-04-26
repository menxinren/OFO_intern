#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	alpha52 = dv.add_formula('alpha52', 
                         'Ts_Sum(Max(0,high-Delay((high+low+close)/3,1)),26)/Ts_Sum(Max(0,Delay((high+low+close)/3,1)-low),26)*100', 
                         is_quarterly=False, add_data=True)
	return alpha52


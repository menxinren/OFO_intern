#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	dv.add_field('bonds_payable')
	dv.add_field('int_payable')
	dv.add_field('dvd_payable')
	dv.add_field('NetProfitGrowRate')
	dv.add_field('total_liab')
	dv.add_field('tot_liab_shrhldr_eqy')

	factor8 = dv.add_formula('factor8','(dvd_payable*(1+NetProfitGrowRate)/Ts_Mean(close,500)+NetProfitGrowRate)*(tot_liab_shrhldr_eqy-total_liab)/tot_liab_shrhldr_eqy+int_payable/bonds_payable*total_liab/tot_liab_shrhldr_eqy',is_quarterly=False, add_data=True)
	return factor8


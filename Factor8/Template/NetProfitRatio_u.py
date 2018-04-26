#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):

	import numpy as np
	dv.add_field('net_profit')
	dv.add_field('oper_rev')
	net_profit = dv.get_ts_quarter('net_profit')
	oper_rev = dv.get_ts_quarter('oper_rev')
	netprofitratio = net_profit/oper_rev
	
	#将季度数据转为日度数据
	temp = dv.get_ts('quarter')
	temp = temp.replace([3,6,9,12],np.nan)
	temp2 = netprofitratio.replace(0,np.nan)
	j0 = 0
	for i in range(len(temp)):
		for j in range(j0,len(temp2)):
			if str(temp[i:i+1].index)[12:18] == str(temp2[j:j+1].index)[12:18]:
				temp[i:i+1] = temp2[j:j+1].values
				j0 = j
				continue
				
	NetProfitRatio_u = temp.bfill()
	dv.append_df(NetProfitRatio_u,'NetProfitRatio_u')
	
	return NetProfitRatio_u


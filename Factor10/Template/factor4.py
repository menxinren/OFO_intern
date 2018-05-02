#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
	import pandas as pd
	import numpy as np
	#获取过去30天中第一次出现涨停板价格
	close = dv.get_ts('close')
	up_limit_price = (close.pct_change()>0.095)*close
	up_limit_price = up_limit_price.replace(0,np.nan)
	t = dv.get_ts('quarter')
	t = t.replace([3,6,9,12],np.nan)
	temp = up_limit_price
	temp = temp.reset_index([x for x in range(len(temp))])
	n = 30
	firstuplimit= t[0:n]
	for i in range(n,len(temp)):
		c = temp[i-n:i].min(axis=0)
		c = c.to_frame().transpose()
		c = c.drop(['trade_date'],axis=1)
		firstuplimit = firstuplimit.append(c)
	index = t.index
	firstuplimit = firstuplimit.set_index(index)
	dv.append_df(firstuplimit,'firstuplimit')

	factor4 = dv.add_formula('factor4','(close-firstuplimit)/firstuplimit',is_quarterly=False, add_data=True)
	return factor4


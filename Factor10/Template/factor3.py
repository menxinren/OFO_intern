#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
		   
	import pandas as pd
	import numpy as np
	#计算过去n日最低价和最高价距离今日的天数
	t = dv.get_ts('quarter')
	t = t.replace([3,6,9,12],np.nan)
	temp = dv.get_ts('low')
	temp = temp.reset_index([x for x in range(len(temp))])
	n = 5
	days_min= t[0:n]
	for i in range(n,len(temp)):
		c = i - temp[i-n:i].idxmin(axis=0)
		c = c.to_frame().transpose()
		c = c.drop(['trade_date'],axis=1)
		days_min = days_min.append(c)
	index = t.index
	days_min = days_min.set_index(index)
	temp = dv.get_ts('high')
	temp = temp.reset_index([x for x in range(len(temp))])
	days_max= t[0:n]
	for i in range(n,len(temp)):
		c = i - temp[i-n:i].idxmax(axis=0)
		c = c.to_frame().transpose()
		c = c.drop(['trade_date'],axis=1)
		days_max = days_max.append(c)
	days_max = days_max.set_index(index)
	dv.remove_field('days_min')
	dv.remove_field('days_max')
	dv.append_df(days_max,'days_max')
	dv.append_df(days_min,'days_min')

	factor3 =dv.add_formula('factor3','(days_min<days_max)*(((close-Ts_Min(close,%s))/days_min)-(Ts_Max(close,%s)-Ts_Min(close,%s))/(days_max-days_min))+ (days_min>days_max)*((Ts_Max(close,%s)-Ts_Min(close,%s))/(days_min-days_max)-((Ts_Max(close,%s)-close)/days_max))'%(n,n,n,n,n,n),is_quarterly=False, add_data=True)
	return factor3


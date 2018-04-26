#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv):
	
	from jaqs.data.dataapi import DataApi
	from jaqs_fxdayu.util import dp
	import pandas as pd
	start = 20140101
	end =20171231
	api = DataApi(addr='tcp://data.tushare.org:8910')
	api.login('13990207985',"eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVfdGltZSI6IjE1MjI5MTg1NjU1NzIiLCJpc3MiOiJhdXRoMCIsImlkIjoiMTM5OTAyMDc5ODUifQ.q3T1TD1nRI4gxvTCVfgAdUqMWXMC_0Egpk97K7I_h4M")
	ZZ800_id = dp.index_cons(api, "000906.SH", start, end)
	stock_symbol = list(set(ZZ800_id.symbol.values))
	df, msg = api.daily(
                symbol="000300.SH",
                start_date=start,
                end_date=end,
                fields="close",
                adjust_mode="post")
	a = {}
	for i in stock_symbol:
		a[i] = list(df['close'])
	hs300_index = pd.DataFrame(a,index=df['trade_date'])
	dv.append_df(hs300_index,'hs300_index')

	InformationRatio120 = dv.add_formula('InformationRatio120','Ts_Mean(Return(close,1)-Return(hs300_index,1),120)/StdDev(Return(close,1)-Return(hs300_index,1),120)', is_quarterly=False, add_data=True)
	
	return InformationRatio120


# 6002-Research-Project



## Variables referenced Hull and Qiao's research [2017]

1. **DP**: Dividend–Price Ratio (Column AD) <br />
股息价格比率可用于预测未来的市场回报。如果当前的股息价格比很高，那么未来的回报也可能很高。

2. **PE**: Price-to-Earnings Ratio (Column E) <br />
市盈率解释了高达40%的未来回报，通常作为股票是便宜抑或昂贵的指标。市盈率越低，代表投资者能够以相对较低价格购入股票。

3. **BM**: Book-to-Market Ratio (Column AE) <br />
使用道琼斯工业平均指数(DJIA)的账面市值比来预测市场回报。高当前账面市值比表明未来市场回报率高。

4. **CAPE**: Cyclically Adjusted Price to Earnings Ratio (Column CF) <br />
周期性调整市盈率是指一家公司去除通货膨胀因素的实际股价除以10年间该公司去除通货膨胀因素的每股收益的平均值。

5. **BY**: Bond Yield (Column AT) <br />
使用30年期国债收益率与其12个月移动平均线之差的负值作为回报预测指标。较高的BY值预测较低的未来回报。

6. **DEF**: Default Spread <br />
使用Baa和Aaa公司债券收益率之间的差异来衡量短期商业状况, DEF与商业周期频率的贴现率效应有关。DEF很高，则预期回报也很高。<br />
BAA(Column Z) - AAA(Column AF)

7. **TERM**: Term Spread <br />
使用Aaa债券投资组合的收益率与一个月国库券利率之间的差值作为跟踪商业周期的变量。如果今天的TERM很高，那么未来的贴现率很高，股权溢价也很高。<br />
US10YR(Column C) - US3M(Column B)

8. **CAY**: Cointegrating Residual of Consumption, Assets, and Wealth <br />
这个想法是协整残差是平稳的，它们包含的信息可能与贴现率相关。今天较大的CAY值表明未来的回报率很高，并且CAY在一年内的表现优于股息收益率。<br />
$Assets = \beta_0 + \beta_1\times Consumption + \beta_2\times Wealth + \epsilon_t$ <br />
Assets = Assets_new (Column BD); Consumption = Consumption_new (Column BC); <br />
Wealth = Income_new (Column BE); Cointegrating Residual = $\epsilon_t$

9. **SIM**: Sell in May and Go Away (Column BW) <br />
假期时间和对来年的乐观情绪会在夏季月份产生较低的回报，而进入来年的回报会更高。平均而言，5月至10月的市场回报率较低，而11月至4月的市场回报率较高。

10. **VRP**: Variance Risk Premium <br />
短期到中期的回报可以通过VIX的平方减去五分钟的实际方差来预测。 高方差风险溢价与高未来回报相关。<br />
trans_VIX(Column L) - garch(Column BJ)

11. **IC**: Implied Correlation (Column CH) <br />
平均股权期权隐含相关性能够预测股权溢价。 高IC会带来高未来回报。

12. **BDI**: Baltic Dry Index (Column K) <br />
BDI三个月的变化预测了全球股票市场样本内和样本外的中期回报。BDI增长率较高表明宏观经济活动更为强劲，并且未来股票回报率较高。

13. **NOS**: New Orders/Shipments (Column T) <br />
新订单与耐用品出货量之间的高比率能够预测超额市场回报。较高水平的NOS与商业周期峰值相关，并预测股票的超额回报较低。

14. **CPI**: Consumer Price Index (Column S) <br />
居民消费价格指数是反映与居民生活有关的产品及劳务价格统计出来的物价变动指标，它是衡量通货膨胀的主要指标之一。

15. **PCR**: Ratio of Stock Price to Commodity Price <br />
使用S&P GSCI衡量的股票价格与商品价格之间的比率的对数来预测未来回报。PCR本质上是另一种价格比率，它以商品价格代替通常的基本变量。如果PCR高，则预期回报低。<br />
trans_spy_open(Column CV) / trans_SPGSCI(Column J)

16. **MA**: Moving Average <br />
基于当前价格与过去10个月简单移动平均线的相对水平的买卖规则。如果当前月价高于过去10个月移动平均线，则为买入信号，预计未来市场回报将很高。

17. **OBV**: On Balanced Volume <br />
收支平衡交易量是一种技术分析指标，旨在将股票市场中的价格和交易量联系起来。OBV基于累计总交易量。<br />
A. If today's closing price is higher than yesterday's closing price, then: Current OBV = Previous OBV + today's volume <br />
B. If today's closing price is lower than yesterday's closing price, then: Current OBV = Previous OBV - today's volume <br />
C. If today's closing price equals yesterday's closing price, then: Current OBV = Previous OBV

18. **MOM**: The Momentum Indicator <br />
动量指标是衡量证券变化率的领先指标, 它将当前价格与多个时期前的价格进行比较。

19. **OIL**: Oil Price Shocks (Unknown) <br />
油价变化是短期内股票超额收益的有力预测指标。如果油价很高，那么未来的回报率预计会很低。

20. **SI**: Short Interest (Column AG) <br />
使用空头利息的平均值除以个股的流通股总数作为回报预测指标。高当前SI表明股权溢价低。



## New Variables from Dataset

1. **trans_MVOLE**: Total Exchange Volume (Column N) <br />

2. **BER**: Break Even Rate (Column AB) <br />
 盈亏平衡率,通胀调整后的收益率与常规10年期国债收益率之间的差值。

3. **NAPMPRIC**: NAPM survey about prices of raw materials (Column AP) <br />

4. **CATY**: Cyclically Adjusted Total Yield (Column CG) <br />
CATY = Dividend Yield + Buyback Yield Adjusted for Inflation

5. **IND_PROD**: Industrial Production Index (Column CN) <br />
工业生产指数是由美国联邦储备委员会发布的经济指标，用于衡量制造业，采矿业和公用事业的实际产量。
 


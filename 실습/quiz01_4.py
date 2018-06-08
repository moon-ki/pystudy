'''
+------------+-----+-----------+
| date | dow | price |
+------------+-----+-----------+
| 2018.01.05 | 금 | 2,497.52 |
| 2018.01.04 | 목 | 2,466.46 |
| 2018.01.03 | 수 | 2,486.35 |
| 2018.01.02 | 화 | 2,479.65 |
+------------+-----+-----------+
'''
lst_date =["2018.01.05","2018.01.04","2018.01.03","2018.01.02"]
lst_dow=["금","목","수","화"]
lst_price=[2497.52,2466.46,2486.35,2479.65]

lst_date.reverse()
lst_dow.reverse()
lst_price.reverse()

kospi_price={}

for i in range(0,len(lst_date),1):
    kospi_price[lst_date[i]]={"dow":lst_dow[i],"price":lst_price[i]}
print(kospi_price)    

for i in range(1,len(kospi_price),1):
    kospi_price[lst_date[i]]["price_diff"]=kospi_price[lst_date[i-1]]["price"]-kospi_price[lst_date[i]]["price"]
print(kospi_price)

#2018.01.05의 price값
print('kospi_price["2018.01.05"]["price_diff"]:',kospi_price["2018.01.05"]["price_diff"])

""" 
for i in range(len(lst_date)):
    kospi_price[lst_date[i]] = {"dow":lst_dow[i], "price":lst_price[i]}
print(kospi_price)    

for i in range(1,len(lst_date)):
    kospi_price[lst_date[i]]["price_diff"]=lst_price[i]-lst_price[i-1]]
#print(kospi_price)   

print("price_diff: %f" % kospi_price["2018"][])
print( "max:{}, min:{}".format(max(lst_price),min(lst_price)) ) """

#dic_tmp = dict(zip(lst_dow,lst_price))
#print(dic_tmp)

#kospi_price = dict(zip(lst_date,{lst_dow,lst_price}))
#print(type(kospi_price),kospi_price)
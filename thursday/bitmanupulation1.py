data1 = 100
data2= 50
resand=data1 & data2
resor=data1 | data2
resxor=data1 ^ data2
resc= ~(data2)
resc1= ~(data1)
rs= data1 >> 2
ls= data1 << 2

print(f"So, {data1} & {data2} = {resand}")
print(f"So, {data1} | {data2} = {resor}")
print(f"So, {data1} ^ {data2} = {resxor}")
print(f"So,  {data2} = {resc}")
print(f"So, {data1} = {resc1}")
print(f"So,  {rs}")
print(f"So,  {ls}")
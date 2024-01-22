f=open("hfhf.txt","r", encoding='utf-8')
search=0
year_b=int(input())
year_e=int(input())
for i in f:
    str=i
    str=str[::-1]
    #print(str)
    #print('-----------------------------------')
    str=str[:5]
    #print(str)
    #print('-----------------------------------')
    str=str[::-1]
    #print(str)
    #print('-----------------------------------')
    if year_b < int(str) < year_e:
        search+=1
        str=i
        #index=str.find(" ")
        #str=str[:index]
        print(str)
        print("----------------")
f.close()
print("всего:",search)
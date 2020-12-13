# Matthew James Resendez
#1431242
import csv
from datetime import datetime, date
today = date.today()
# today = datetime.strptime('7/30/2019', '%m/%d/%Y').date()

dic = {}

with open('ManufacturerList.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        try:
            row.remove('')
        except:
            pass
        dic[row[0]] = [row[1], row[2]]
    
with open('PriceList.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        try:
            row.remove('')
        except:
            pass        
        dic[row[0]].append(row[1])
        
with open('ServiceDatesList.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        try:
            row.remove('')
        except:
            pass        
        dic[row[0]].append(row[1])
        
with open('ManufacturerList.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        try:
            row.remove('')
        except:
            pass
        if len(row) == 4:
            dic[row[0]].append(row[3])
        


# 1.a
dic_sorted_manufacturer = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
with open('FullInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(dic_sorted_manufacturer)):
        k = list(dic_sorted_manufacturer.keys())[i]
        v = list(dic_sorted_manufacturer.values())[i]
        if len(v) == 4:
            writer.writerow([k, v[0], v[1], v[2], v[3]])
        elif len(v) == 5:
            writer.writerow([k, v[0], v[1], v[2], v[3], v[4]])

#  1.b
dic_sorted_ID =  dict(sorted(dic.items()))
with open('LaptopInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(dic_sorted_ID)):
        k = list(dic_sorted_ID.keys())[i]
        v = list(dic_sorted_ID.values())[i]
        if v[1] == 'laptop':            
            if len(v) == 4:
                writer.writerow([k, v[0], v[2], v[3]])
            elif len(v) == 5:
                writer.writerow([k, v[0], v[2], v[3], v[4]])
            
with open('PhoneInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(dic_sorted_ID)):
        k = list(dic_sorted_ID.keys())[i]
        v = list(dic_sorted_ID.values())[i]
        if v[1] == 'phone':            
            if len(v) == 4:
                writer.writerow([k, v[0], v[2], v[3]])
            elif len(v) == 5:
                writer.writerow([k, v[0], v[2], v[3], v[4]])

with open('TowerInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(dic_sorted_ID)):
        k = list(dic_sorted_ID.keys())[i]
        v = list(dic_sorted_ID.values())[i]
        if v[1] == 'tower':            
            if len(v) == 4:
                writer.writerow([k, v[0], v[2], v[3]])
            elif len(v) == 5:
                writer.writerow([k, v[0], v[2], v[3], v[4]])

#  1.c
dic_sorted_servicedate = {k: v for k, v in sorted(dic.items(), key=lambda item: datetime.strptime(item[1][3], '%m/%d/%Y'))}
with open('PastServiceDateInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(dic_sorted_servicedate)):
        k = list(dic_sorted_servicedate.keys())[i]
        v = list(dic_sorted_servicedate.values())[i]
        if today>datetime.strptime(v[3], '%m/%d/%Y').date():
            if len(v) == 4:
                writer.writerow([k, v[0], v[1], v[2], v[3]])
            elif len(v) == 5:
                writer.writerow([k, v[0], v[1], v[2], v[3], v[4]])

# 1.d
dic_sorted_price = {k: v for k, v in sorted(dic.items(), reverse=True, key=lambda item: float(item[1][2]))}
with open('DamagedInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(dic_sorted_ID)):
        k = list(dic_sorted_ID.keys())[i]
        v = list(dic_sorted_ID.values())[i]
        if len(v) == 5:
            writer.writerow([k, v[0], v[1], v[2], v[3]])
            
# 2            
        
manu = [el[0].lower().strip() for el in list(dic.values())]
manu = list(set(manu))

item = [el[1].lower().strip() for el in list(dic.values())]
item = list(set(item))

while True:

    query = input('Enter manufacture and item type: ')
    
    if query == 'q':
        break

    query = query.lower().split(" ")
    
    
    count_manu = 0
    count_item = 0
    
    for word in query:
        if word in manu:
            q_manu = word
            count_manu += 1
        if word in item:
            q_item = word
            count_item += 1
    
    flag = 0
        
    for i in range(len(dic_sorted_price)):
    
        
        if count_manu!=1 or count_item!=1:
            flag = 1
            print("No such item in inventory\n")
            break
    
        v = list(dic_sorted_price.values())[i]
        k = list(dic_sorted_price.keys())[i]
        v0 = v[0].lower().strip()
        v1 = v[1].lower().strip()
        v2 = v[2].lower().strip()
        v3 = v[3].lower().strip()
        
        if  v0 == q_manu and  v1 == q_item and today<datetime.strptime(v3, '%m/%d/%Y').date() and len(v)==4:
            print('Your item is: ',k,v0,v1,v2)
            flag = 2
            break
        
    if flag==0:
        print("No such item in inventory\n")
        
    
    if flag==2:
        
        for i in range(len(dic_sorted_price)):
    
            v = list(dic_sorted_price.values())[i]
            k = list(dic_sorted_price.keys())[i]
            v0 = v[0].lower().strip()
            v1 = v[1].lower().strip()
            v2 = v[2].lower().strip()
            v3 = v[3].lower().strip()
        
            if  v0 != q_manu and  v1 == q_item and today<datetime.strptime(v3, '%m/%d/%Y').date() and len(v)==4:
                print('You may, also, consider: ',k,v0,v1,v2)
                break
        
    
    
    
    
    




    
    
    
    

    
    
        


        






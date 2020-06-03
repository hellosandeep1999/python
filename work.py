# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:04:20 2020

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:02:02 2020

@author: user
"""


import pandas as pd
from re import search

Main_file=input("Enter Your Main File Name(Without Extension) :")
df4 = pd.read_excel("{}.xlsx".format(Main_file))




df4 = df4[["Your Name ( This will be printed on your Certificate )", \
               "Email ID (Please enter your Gmail ID)", "Your Gender", \
               "College Name", "Whatsapp No "]]
    
    
df4.columns = ["Name", "Email", "Gender", "College Name", "WhatsApp No."] 

  




File_Total=int(input("Enter the Number of File You want to Enter:"))


#for full.csv 
dataframe_name = []  
for file_i in range(File_Total):
    a = "data"+str(file_i)
    dataframe_name.append(a)
    
    
    
  
for file in range(File_Total):
        
    File_Name=input("Enter the "+ str(file) +" File Name")
    
    file_number = File_Name[4]
    
    df1 = pd.read_csv("{}.csv".format(File_Name))
    
    
    df1.columns = ["Name", "Email", "Time"]
    
    
    
    
    
    #this by only email id
    f = df1.merge(right = df4, how = "left", on = "Email", suffixes=('', 'Registered') )
    
    
    
    
    
    
    def removing(list1):
        SYMBOLS = '{}()[].,:;+-*/&|<>=~' 
        list2 = []
        for element in list1:
            temp = ""
            for ch in element:
                if ch not in SYMBOLS:
                    temp += ch
        
            list2.append(temp)
        return list2
    
    
    
    f['Name'] = [name.upper() for name in f['Name'].tolist()]
    data_list = f['Name'].tolist()
    f['Name'] = removing(data_list)
    
    
    
    f.drop_duplicates(subset='Name',keep='last', inplace=True)
    f.reset_index(inplace = True, drop = True)
    
    
    df4['Name'] = [name.upper() for name in df4['Name'].tolist()]
    data_list = df4['Name'].tolist()
    df4['Name'] = removing(data_list)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #sample testing dataset
    """
    data1 = {'Name':['Tom goyal', 'nick jain', 'krish sharma', 'jack nama'], 'Age':[20, 21, 19, 18]} 
    zoom = {'Name':['nicky jain', 'k nama', 'sharma','dev'], 'mab no':[98465,1656516,166432,'nan'],
             'marks':[125,225,325,744]} 
    # Create DataFrame 
    dataframe1 = pd.DataFrame(data1)
    dataframe2 = pd.DataFrame(zoom)
    
    #to_repl = dataframe2['Name'].values.tolist()
    
    #vals = dataframe2['marks'].values.tolist()
    
    #dataframe1['col3'] = dataframe2['Name'].replace(to_repl, vals, regex=True)
    """
    
    
    
    
    zoom_list = f['Name'].values.tolist()
    zoom_Email_list = f['Email'].values.tolist()
    data1_list = df4['Name'].values.tolist()
    data1_Email_list = df4['Email'].values.tolist()
    
    store = []
    zoom_store = []
    
    for zoom_index, zoom_name in enumerate(zoom_list):
        if "." in str(zoom_Email_list[zoom_index]):
            for data1_Email_index,data1_Email in enumerate(data1_Email_list):
                if zoom_Email_list[zoom_index] == data1_Email:
                    store.append(data1_Email_index)
                    zoom_store.append(zoom_index)
                    break
            else:
                name = zoom_name.split()
                for part_name in name:
                    if len(part_name) > 2:
                        for data1_index, data1_name in enumerate(data1_list):
                            if search(part_name,data1_name):
                                store.append(data1_index)
                                zoom_store.append(zoom_index)
                                break
                        break
        else:
            name = zoom_name.split()
            for part_name in name:
                if len(part_name) > 2:
                    for data1_index, data1_name in enumerate(data1_list):
                        if search(part_name,data1_name):
                            store.append(data1_index)
                            zoom_store.append(zoom_index)
                            break
                    break
            
                
    
    
            
      
    #store = list(dict.fromkeys(store))
    #zoom_store = list(dict.fromkeys(zoom_store))   
        
    
    
    
    
    
    
    
    
    #New_Age = [0] * len(dataframe2['Name'])
        
    
    
    
    
    
    #dataframe2['Age'] = New_Age           
    #age = dataframe1['Age'].tolist()
    
    
    j = 0
    for i in store:
        while j < len(zoom_store):
            value = zoom_store[j]
            f['Email'][value] = df4['Email'][i] 
            f['NameRegistered'][value] = df4['Name'][i]
            f['Gender'][value] = df4['Gender'][i]
            f['College Name'][value] = df4['College Name'][i]
            f['WhatsApp No.'][value] = df4['WhatsApp No.'][i]
            j += 1
            break
    
    
     
    No_Reg = f[f['NameRegistered'].isnull()]   #This datafrme which are not attend but not registered
    No_Reg.columns = ["Zoom Name", "Email", "Time","Registered Name","Gender","College Name","WhatsApp No."]
    No_Reg = No_Reg.sort_values("Time", ascending = False)
    
        
    #f.dropna(subset=['Email'], inplace=True) 
        
    f.dropna(subset=['Email','NameRegistered', 'Gender', 'College Name',
           'WhatsApp No.'], inplace=True)
     
        
        
    
    No_present = f.copy()
    No_present = No_present.merge(right = df4, how = "outer", on = "Email", suffixes=('', '_Reg') )
    No_present = No_present[No_present['Name'].isnull()]
    No_present = No_present[["Name", "Email", "Time",'Name_Reg', 'Gender_Reg', 'College Name_Reg','WhatsApp No._Reg']]
    No_present.columns = ["Zoom Name", "Email", "Time","Registered Name","Gender","College Name","WhatsApp No."]
    
    No_present=No_present.append(pd.Series("nan"), ignore_index=True)
    No_present=No_present.drop([0],axis=1) 
    new_row={"Zoom Name":"Not","Email":"Registered"}
    No_present = No_present.append(new_row,ignore_index=True)
    
        
    
    
       
        
    f = f.sort_values("Time", ascending = False)
    f.reset_index(inplace = True, drop = True)  
    f.columns = ["Zoom Name", "Email", "Time","Registered Name","Gender","College Name","WhatsApp No."]  
    
    f=f.append(pd.Series("nan"), ignore_index=True)
    f=f.drop([0],axis=1) 
    new_row={"Zoom Name":"Absent","Email":"List"}
    f = f.append(new_row,ignore_index=True)
    
    
    #for full.csv
    my_copy = f[:-2].copy()
    dataframe_name[file] = my_copy
    dataframe_name[file] = dataframe_name[file][["Zoom Name","Email","Time"]]
    dataframe_name[file].columns = ["Name", "Email", "Time"]
    dataframe_name[file]["Date"] = file+1
    
    
    
    
    
    frame=[f,No_present,No_Reg]
    result=pd.concat(frame)
    result = result[["Zoom Name", "Email", "Time","Registered Name","Gender","College Name","WhatsApp No."]]   
    result.to_csv("Day{}.csv".format(file_number), index = False)








#work start for full.csv



    
zoom = pd.concat(dataframe_name)
#Deleting the columns with no value
zoom = zoom.dropna(how = "all")

zoom.reset_index(inplace = True, drop = True)   


    
temp = zoom["Email"].tolist()
temp = [str(x).lower() for x in temp]
del zoom["Email"]
zoom.insert(1,"Email",temp,allow_duplicates=True)






emails = zoom["Email"].tolist()
ats = []
for at_index in range(1,(File_Total+1)):
    b = "at" + str(at_index)
    ats.append(b)
    
index = 0
while index < File_Total:
    ats[index] = [0] * len(emails)
    index += 1



zoom_names = zoom["Name"].tolist()
zoom_durations = zoom["Time"].tolist()
zoom_dates = zoom["Date"].tolist()


for dates_index in range(1,(File_Total+1)):
    for index,name in enumerate(zoom_names): 
        for zindex, zname in enumerate(zoom_names):
            if str(name) in str(zname):
                if zoom_dates[zindex] == dates_index:
                    ats[(dates_index-1)][index] = zoom_durations[zindex]
    

       

total = [0] * len(zoom_names)



for index,name in enumerate(zoom_names):
      index_at = 0
      while index_at < File_Total:
           if index_at == 0:
                total[index] = ats[index_at][index] 
           elif index_at > 0:
                total[index] += ats[index_at][index]
           index_at += 1
 
          

ats.insert(0, zoom_names)
ats.insert(1, emails)
cal = 2 + File_Total
ats.insert(cal, total)

z = pd.DataFrame(ats)
   
z = z.T  #transpose the dataframe


column_list = ["Zoom Name", "Email"]
for column_list_index in range(File_Total):
    day_name = "Day{}".format(column_list_index)
    column_list.append(day_name)

column_list.append("Total")

z.columns = column_list


z.drop_duplicates(inplace = True)
z.reset_index(inplace = True, drop = True)

#z.to_csv("Total Zoom Data.csv", index = False)


final = z.merge(right = df4, how = "left", on = "Email", suffixes=('', 'Registered') )




final_list = ['Name', 'Gender', 'College Name', 'WhatsApp No.','Zoom Name', 'Email']
for final_list_index in range(File_Total):
    day_name = "Day{}".format(final_list_index)
    final_list.append(day_name)

final_list.append("Total")
final = final[final_list]


final = final.sort_values("Total", ascending = False)

final_copy = final.copy()  #make a copy of dataframe

for last_index in range(File_Total):
    final = final[(final["Day{}".format(last_index)] > 0)]

final.drop_duplicates(subset=["Email"], keep='first', inplace=True)
final.reset_index(inplace = True, drop = True)
final.to_csv("Full_data_present_everyday.csv", index = False)





#work start for No_present.csv 


final_copy.drop_duplicates(subset=["Name"], keep='first', inplace=True) 








final_work = final_copy.merge(right = df4, how = "outer", on = "Email", suffixes=('', '_Reg') )




final_work = final_work[final_work['Zoom Name'].isnull()]

final_work = final_work[['Name_Reg','Email','Gender_Reg', 'College Name_Reg', 'WhatsApp No._Reg']]

final_work.to_csv("Not_present_any_day.csv", index = False)




















































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
import numpy as np

Main_file=input("Enter Your Main File Name(Without Extension) :")
df4 = pd.read_excel("{}.xlsx".format(Main_file))

df4_copy = df4.copy()

df4_copy["Zoom id"] = np.nan

df4_column_list = [] 

for column_name in df4.columns.tolist():
    if "NAME" in column_name.upper():
        df4_column_list.append(column_name)
        break
for column_name in df4.columns.tolist():
    if "MAIL" in column_name.upper():
        df4_column_list.append(column_name)
        break
for column_name in df4.columns.tolist():
    if "GENDER" in column_name.upper():
        df4_column_list.append(column_name)
        break
for column_name in df4.columns.tolist():
    if "COLLEGE" in column_name.upper():
        df4_column_list.append(column_name)
        break
for column_name in df4.columns.tolist():
    if "WHATSAPP" in column_name.upper():
        df4_column_list.append(column_name)
        break
        
        

df4 = df4[df4_column_list]


    
    
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
    
    df1 = df1[df1.columns.tolist()]
    
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
    
    
    
    f.drop_duplicates(subset='Email',keep='last', inplace=True)
    f.reset_index(inplace = True, drop = True)
    
    
    df4['Name'] = [name.upper() for name in df4['Name'].tolist()]
    data_list = df4['Name'].tolist()
    df4['Name'] = removing(data_list)
    
    
    if file == 0:
        df4_copy[df4_column_list[0]] = [name.upper() for name in df4_copy[df4_column_list[0]].tolist()]
        data_list = df4_copy[df4_column_list[0]].tolist()
        df4_copy[df4_column_list[0]] = removing(data_list)
    
    
    
#    f_copy = f[f['NameRegistered'].isnull()]
    
    
    
    
    
    
    
    
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
    
    
    f["Zoom id"] = np.nan
    
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
                    f["Zoom id"][zoom_index] = data1_Email
                    df4_copy["Zoom id"][data1_Email_index] = data1_Email
                    break
                
            else:
                name = zoom_name.split()
                set1 = []
                set2 = []
                n = 0
                while n < len(name):
                    if len(name[n]) > 2:
                        for data1_index, data1_name in enumerate(data1_list):
                            data1_name = data1_name.split() 
                            if name[-1] in data1_name:
                                set2.append(data1_index)
                            if name[n] in data1_name:
                                set1.append(data1_index)
                        break
                    else:
                        n += 1
                set3 = set(set1)
                set4 = set(set2)
                set_intersection = set3.intersection(set4)
                
                if len(set_intersection) > 0:
                    change_list = list(set_intersection)
                    store.append(change_list[0])
                    zoom_store.append(zoom_index)
                    f["Zoom id"][zoom_index] = df4["Email"][change_list[0]]
                    df4_copy["Zoom id"][change_list[0]] = f['Email'][zoom_index]
#                else:
#                    change_list = list(set2)
#                    if len(change_list) > 0:
#                        store.append(change_list[0])
#                        zoom_store.append(zoom_index)
                        
                        
                  
        else:
            name = zoom_name.split()
            set1 = []
            set2 = []
            n = 0
            while n < len(name):
                if len(name[n]) > 2:
                    for data1_index, data1_name in enumerate(data1_list):
                        data1_name = data1_name.split() 
                        if name[-1] in data1_name:
                            set2.append(data1_index)
                        if name[n] in data1_name:
                            set1.append(data1_index)
                    break
                else:
                    n += 1
            set3 = set(set1)
            set4 = set(set2)
            set_intersection = set3.intersection(set4)
            
            if len(set_intersection) > 0:
                change_list = list(set_intersection)
                store.append(change_list[0])
                zoom_store.append(zoom_index)
                f["Zoom id"][zoom_index] = df4["Email"][change_list[0]]
                df4_copy["Zoom id"][change_list[0]] = f['Email'][zoom_index]
#            else:
#                change_list = list(set2)
#                if len(change_list) > 0:
#                     store.append(change_list[0])
#                     zoom_store.append(zoom_index)
               
            
                
    
    
            
      
    #store = list(dict.fromkeys(store))
    #zoom_store = list(dict.fromkeys(zoom_store))   
        
    
    
    
    
    
    
    
    
    #New_Age = [0] * len(dataframe2['Name'])
        
    
    
    
    
    
    #dataframe2['Age'] = New_Age           
    #age = dataframe1['Age'].tolist()
    
    
    j = 0
    for i in store:
        while j < len(zoom_store):
            value = zoom_store[j]
#           f['Email'][value] = df4['Email'][i] 
            f['NameRegistered'][value] = df4['Name'][i]
            f['Gender'][value] = df4['Gender'][i]
            f['College Name'][value] = df4['College Name'][i]
            f['WhatsApp No.'][value] = df4['WhatsApp No.'][i]
            j += 1
            break
        
    f.drop_duplicates(subset='Email',keep='last', inplace=True)
    
     
    No_Reg = f[f['NameRegistered'].isnull()]   #This datafrme which are not attend but not registered
    No_Reg.columns = ["Zoom Name", "Email", "Time","Registered Name","Gender","College Name","WhatsApp No.","Zoom id"]
    No_Reg = No_Reg.sort_values("Time", ascending = False)
    
    
    
    
    
        
#    #work for suspence entries
#    Suspence_copy = No_Reg.copy()
#    Suspence_copy.reset_index(inplace = True, drop = True) 
#    
#    Suspence_zoom_list = Suspence_copy['Zoom Name'].values.tolist()
#    Suspence_data1_list = df4['Name'].values.tolist()
#    
#    Suspence_set1 = []
#    for Suspence_zoom_index,Suspence_zoom_name in enumerate(Suspence_zoom_list):
#         Suspence_name = Suspence_zoom_name.split()
#         n = 0
#         while n < len(Suspence_name):
#             if len(Suspence_name[n]) > 2:
#                 for Suspence_data1_index, Suspence_data1_name in enumerate(Suspence_data1_list):
#                     if search(Suspence_name[n],Suspence_data1_name):
#                         Suspence_set1.append(Suspence_zoom_index)
#                         break
#                 break
#             else:
#                 n += 1
#    
#    Suspence_result = []
#    for Suspence_set1_index,Suspence_set1_value in enumerate(Suspence_set1):
#        Suspence_result.append(Suspence_copy.iloc[Suspence_set1_value])
#        
#    Suspence_result = pd.DataFrame(Suspence_result)         
#    
#    
#    
#    No_Reg=No_Reg.append(pd.Series("nan"), ignore_index=True)
#    No_Reg=No_Reg.drop([0],axis=1) 
#    new_row={"Zoom Name":"Suspended","Email":"Results"}
#    No_Reg = No_Reg.append(new_row,ignore_index=True)
    
    
    
    
    
    #f.dropna(subset=['Email'], inplace=True) 
        
    f.dropna(subset=['Email','NameRegistered', 'Gender', 'College Name',
           'WhatsApp No.'], inplace=True)
     
        
        
    
    No_present = f.copy()
    df4 = df4.rename(columns={'Email': 'Zoom id'})
    No_present = No_present.merge(right = df4, how = "outer", on = "Zoom id", suffixes=('', '_Reg') )
    No_present = No_present[No_present['Name'].isnull()]
    No_present.drop(['Email'], axis=1,inplace=True)
    No_present = No_present.rename(columns={'Zoom id': 'Email'})
    No_present["Zoom id"] = np.nan
    No_present = No_present[["Name", "Email", "Time",'Name_Reg', 'Gender_Reg', 'College Name_Reg','WhatsApp No._Reg','Zoom id']]
    No_present.columns = ["Zoom Name", "Email", "Time","Registered Name","Gender","College Name","WhatsApp No.","Zoom id"]
    
    No_present=No_present.append(pd.Series("nan"), ignore_index=True)
    No_present=No_present.drop([0],axis=1) 
    new_row={"Zoom Name":"Suspense","Email":"Data"}
    No_present = No_present.append(new_row,ignore_index=True)
    
        
    
    
       
        
    f = f.sort_values("Time", ascending = False)
    f.reset_index(inplace = True, drop = True)  
    f.columns = ["Zoom Name", "Email", "Time","Registered Name","Gender","College Name","WhatsApp No.","Zoom id"]  
    
    f=f.append(pd.Series("nan"), ignore_index=True)
    f=f.drop([0],axis=1) 
    new_row={"Zoom Name":"Absent","Email":"List"}
    f = f.append(new_row,ignore_index=True)
    
    
    #for full.csv
    my_copy = f[:-2].copy()
    dataframe_name[file] = my_copy
    dataframe_name[file] = dataframe_name[file][["Zoom Name","Zoom id","Time"]]
    dataframe_name[file].columns = ["Name", "Zoom id", "Time"]
    dataframe_name[file]["Date"] = file+1
    
    
    
    
    
    frame=[f,No_present,No_Reg]
    result=pd.concat(frame)
    result = result[["Zoom Name", "Email", "Time","Registered Name","Gender","College Name","WhatsApp No.","Zoom id"]]   
    df4 = df4.rename(columns={'Zoom id': 'Email'})
    result.to_csv("Day{}.csv".format(file_number), index = False)







df4 = df4.rename(columns={'Email': 'Zoom id'})
#work start for full.csv



    
zoom = pd.concat(dataframe_name)
#Deleting the columns with no value
zoom = zoom.dropna(how = "all")

zoom.reset_index(inplace = True, drop = True)   


    
#temp = zoom["Email"].tolist()
#temp = [str(x).lower() for x in temp]
#del zoom["Email"]
#zoom.insert(1,"Email",temp,allow_duplicates=True)






emails = zoom["Zoom id"].tolist()
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

z = z.rename(columns={'Email': 'Zoom id'})
final = z.merge(right = df4, how = "left", on = "Zoom id", suffixes=('', 'Registered'))




final_list = ['Name', 'Gender', 'College Name', 'WhatsApp No.','Zoom Name', 'Zoom id']
for final_list_index in range(File_Total):
    day_name = "Day{}".format(final_list_index)
    final_list.append(day_name)

final_list.append("Total")
final = final[final_list]


final = final.sort_values("Total", ascending = False)

final_copy = final.copy()  #make a copy of dataframe

Atleast_one_day = final.copy() #atleast one day present data 
Atleast_one_day.drop_duplicates(subset=["Zoom id"], keep='first', inplace=True)
Atleast_one_day.reset_index(inplace = True, drop = True)


for last_index in range(File_Total):
    final = final[(final["Day{}".format(last_index)] > 0)]
final.drop_duplicates(subset=["Zoom id"], keep='first', inplace=True)
final.reset_index(inplace = True, drop = True)


Atleast_one_day_list = Atleast_one_day["Zoom id"].tolist()
final_list = final["Zoom id"].tolist()


for final_list_index,final_list_email in enumerate(final_list):
    Atleast_one_day = Atleast_one_day[Atleast_one_day["Zoom id"] != '{}'.format(final_list_email)]
Atleast_one_day.reset_index(inplace = True, drop = True)    
    
Atleast_one_day = Atleast_one_day.rename(columns={'Zoom id': 'Email'})
Atleast_one_day.to_csv("Atleast_one_day_present.csv", index = False)

final = final.rename(columns={'Zoom id': 'Email'})
final.to_csv("Full_data_present_everyday.csv", index = False)





#work start for No_present.csv 


final_copy.drop_duplicates(subset=["Name"], keep='first', inplace=True) 








final_work = final_copy.merge(right = df4, how = "outer", on = "Zoom id", suffixes=('', '_Reg') )




final_work = final_work[final_work['Zoom Name'].isnull()]

final_work = final_work[['Name_Reg','Zoom id','Gender_Reg', 'College Name_Reg', 'WhatsApp No._Reg']]

z = z.rename(columns={'Zoom id': 'Email'})
final_work.to_csv("Not_present_any_day.csv", index = False)





df4_copy.to_csv("Updated_Excel _sheet.csv", index = False)














































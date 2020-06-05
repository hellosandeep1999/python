# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:58:26 2020

@author: user
"""

import pandas as pd

df1 = pd.read_csv("Day_0_participants_84422597238 (1).csv")
df2 = pd.read_csv("Day_1_participants_84422597238.csv")
df3 = pd.read_csv("Day_2_participants_84422597238.csv")
df4 = pd.read_csv("Day_3_participants_84422597238.csv")
df5 = pd.read_csv("Day_4_participants_84422597238.csv")
df6 = pd.read_csv("Day_5_participants_84422597238.csv")
df7 = pd.read_excel("Prime Season 4 - Supervised ML- INR 500 (Responses) (1).xlsx")




df1.columns = ["Name", "Email", "Time"]
df2.columns = ["Name", "Email", "Time"]
df3.columns = ["Name", "Email", "Time"]
df4.columns = ["Name", "Email", "Time"]
df5.columns = ["Name", "Email", "Time"]
df6.columns = ["Name", "Email", "Time"]


df1["Date"] = 1
df2["Date"] = 2
df3["Date"] = 3
df4["Date"] = 4
df5["Date"] = 5
df6["Date"] = 6


frames = [df1, df2, df3,df4,df5,df6]
zoom = pd.concat(frames)
#Deleting the columns with no value
zoom = zoom.dropna(how = "all")

zoom.reset_index(inplace = True, drop = True)




temp = zoom["Email"].tolist()
temp = [str(x).lower() for x in temp]
del zoom["Email"]
zoom.insert(1,"Email",temp,allow_duplicates=True)




emails = zoom["Email"].tolist()
at1 = [0] * len(emails)
at2 = [0] * len(emails)
at3 = [0] * len(emails)
at4 = [0] * len(emails)
at5 = [0] * len(emails)
at6 = [0] * len(emails)




zoom_names = zoom["Name"].tolist()
zoom_durations = zoom["Time"].tolist()
zoom_dates = zoom["Date"].tolist()




for index,name in enumerate(zoom_names): 
    for zindex, zname in enumerate(zoom_names):
        if str(name) in str(zname):
            if zoom_dates[zindex] == 1:
                at1[index] = zoom_durations[zindex]
            if zoom_dates[zindex] == 2:
                at2[index] = zoom_durations[zindex]
            if zoom_dates[zindex] == 3:
                at3[index] = zoom_durations[zindex]

            if zoom_dates[zindex] == 4:
                at4[index] = zoom_durations[zindex]
            if zoom_dates[zindex] == 5:
                at5[index] = zoom_durations[zindex]
            if zoom_dates[zindex] == 6:
                at6[index] = zoom_durations[zindex]



total = [0] * len(zoom_names)
for index,name in enumerate(zoom_names):
    total[index] = at1[index] + at2[index] + at3[index] + at4[index] + at5[index] + at6[index]




z = pd.DataFrame(list(zip(zoom_names, emails, at1,at2,at3,at4,at5,at6,total)))
z.columns = ["Zoom Name", "Email", "Day1","Day2","Day3","Day4","Day5","Day6","Total"]




z.drop_duplicates(inplace = True)
z.reset_index(inplace = True, drop = True)
#z.to_csv("Total Zoom Data.csv", index = False)











#gender, college, mobile, whatsapp, email, name











df7 = df7[["Your Name ( This will be printed on your Certificate )", \
           "Email ID (Please enter your Gmail ID)", "Your Gender", \
           "College Name", "Whatsapp No "]]




df7.columns = ["Name", "Email", "Gender", "College Name", "WhatsApp No."]




f = z.merge(right = df7, how = "left", on = "Email", suffixes=('', 'Registered') )




f = f[['Name', 'Gender', 'College Name', 'WhatsApp No.','Zoom Name', 'Email', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Total']]



f = f.sort_values("Total", ascending = False).drop_duplicates("Email")

f.reset_index(inplace = True, drop = True)
# Drop rows with any NaN in the selected columns only

f[(f['Email'] == 'nan')].index[0]

f.drop([f[(f['Email'] == 'nan')].index[0]],inplace=True)



f.to_csv("Zoom 6 days data.csv", index = False)



last = f[(f["Day1"] > 0) & (f["Day2"] > 0) & (f["Day3"] > 0) & (f["Day4"] > 0) & (f["Day5"] > 0) & (f["Day6"] > 0)]





last.to_csv(" attended everyday.csv",index = False)
































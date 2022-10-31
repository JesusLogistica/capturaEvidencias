from datetime import datetime,date

# use creds to create a client to interact with the Google Drive API
"""cope = ['https://docs.google.com/spreadsheets/u/0/']
creds = ServiceAccountCredentials.from_json_keyfile_name('logistica5-tableros-cbcc5f8d90e6.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("CopiaReporte")

# Extract and print all of the values
lis1t_of_hashes = sheet.get_all_records()"""
#print(list_of_hashes)
'''
try:
    fechaLIquidada='03/03/2021'
    fecha_cadena = fechaLIquidada
    fecha = datetime.strptime(fecha_cadena, '%d/%m/%y') 
    #fecha1=str(fecha)
    fecha1=datetime.strftime(fecha,'%d/%m/%Y')
except:
    pass

print(fecha1)
print(fecha)
'''
'''
    
def printDates(dates):  
   
    for i in range(len(dates)):   
        print(dates[i])  
       
       
if __name__ == "__main__":   
  
    dates =  ["23 Jun 2018", "2 Dec 2017", "11 Jun 2018",  
              "01 Jan 2019", "10 Jul 2016", "01 Jan 2007"]   
      
    
    dates.sort(key = lambda date: datetime.strptime(date, '%d %b %Y')) 
    
    
    printDates(dates)  '''

#Metodo para corregir el formato de las fechas ya colocadas
'''newDate=[]
    for value in df["Desde"]:
      try:
        fechaLIquidada=value
        fecha_cadena = fechaLIquidada
        fecha = datetime.strptime(fecha_cadena, '%d/%m/%y') 
        #fecha1=str(fecha)
        fecha1=datetime.strftime(fecha,'%d/%m/%Y')
        newDate.append(fecha1)
      except:
        newDate.append(value)
    df["Desde"]=newDate'''
'''import panas as pd
data = pd.DataFrame({'AdmissionDate': ['2021-01-25','2021-01-22','2021-01-20', 
                        '2021-01-18','2021-01-22','2021-01-17','2021-01-21'], 
                     'StudentID': [7,5,3,2,6,1,4], 
                     'Name': ['Ram','Shyam','Mohan','Sohan','Lucky','Abhinav','Danny'], 
                     'Stream':['CSE','ECE','Civil','Mechanical','CSE','IT','EEE'] 
                   }) 
print(data)
print(type(data.AdmissionDate[0])) 
  
data['AdmissionDate'] = pd.to_datetime(data['AdmissionDate']) 
  
print(type(data.AdmissionDate[0]))
print(type(data.AdmissionDate[0])) 
  
data['AdmissionDate'] = pd.to_datetime(data['AdmissionDate']) 
  
print(type(data.AdmissionDate[0]))
data.sort_values(by='AdmissionDate') 
print(data)'''

'''fecha_cadena = "20/10/2022"
fecha = datetime.strptime(fecha_cadena, '%d/%m/%Y')
today = datetime.now()
print (str(today.date()))

if (fecha < today):
    print("Ya se liquido")

else:
    print("No se liquido")'''
'''estatus="Recuperada - Liquidada"
if estatus=="Recuperada - Liquidada":
    today = datetime.now()
    todayPay=datetime.strptime(str(today.date()),'%Y-%m-%d')
    todayPay=datetime.strftime(today.date(),'%d/%m/%Y')

    print ("Se liquido el día: ",todayPay)
'''
'''
import pandas as pd
import numpy    as np
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        columns=['a', 'b', 'c'])

print (df2.head())

v=df2.loc[0]

print (v)
lis=[]
lis=v.iloc[1]
print (lis)
print("sd")'''
test_dict={"sis":""}
if (not test_dict):
    print("vacio")

else: 
    print("no vacio")
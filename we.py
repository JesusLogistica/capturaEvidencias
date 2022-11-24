from tkinter import *

import gspread
import pandas as pd
from pandastable import Table, TableModel
from datetime import date ,timedelta ,datetime

gc = gspread.service_account(filename='logistica5-tableros-cbcc5f8d90e6.json')
    # Abrir por titulo

sh=""
worksheet=""






class Checker():
  def checkerInt(self,strVariable):
    try:
      variableInt=int(strVariable)
      return variableInt
    except:
      print("El valor debe ser entero")
      variableInt=str(input("Ingrese la cantidad en entero: "))
      return self.checkerInt(variableInt)
  
  def checkerFloat(self,strVariable):
    try:
      variableFloat=float(strVariable)
      return variableFloat
    except:
      print("El valor debe ser flotante")

      variableFloat=str(input("Ingrese la cantidad en flotante: "))
      return self.checkerFloat(variableFloat)
  
  def checkerOrdenFecha(self,re1,re2,df,keyDF):
    newDate=[]
    # "%Y-%m-%d"  and "&d/%m/&Y"
    for value in df[keyDF]:
      
    
      try:
        value
        
        fecha_cadena = value
        fecha = datetime.strptime(fecha_cadena, re1) 
        #fecha1=str(fecha)
      
        fecha1=datetime.strftime(fecha,re2)
        newDate.append(fecha1)
      except:
        newDate.append(value)
    df[keyDF]=newDate
    return df

  def checkerOptionExists(self,listToChecker,option):
    option=self.checkerInt(option)
    if ((option <=(len(listToChecker)-1)) and (option>0)):
      
      return option
    else:
      print("No se encuentra en las opciones")

      option=str  (input("Ingrese una opción valida: "))
      return self.checkerOptionExists(listToChecker,option)
      

    

class Segmento():

  
  def printSegmento(self):
    
    segList=["Dedicado Circuito","Dedicado Zumpango","Patio SLP",
    "Incentivo"," SLP-LMM","SLP-Foráneo"]
    return segList
  def captDesde(self,dict,listPrint):
    che=Checker()
    print(listPrint[1])
    self.printSegmento()
    
    segList=["","Dedicado Circuito","Dedicado Zumpango","Patio SLP",
    "Incentivo"," SLP-LMM","SLP-Foráneo"]
    seg=str(input())
    segCheck=che.checkerOptionExists(segList,seg)
    segValu=segList[segCheck]
    return segValu


  def returnSegmento(self,newData,questionsList):
    
    newData['Segmento']=self.captDesde(newData,questionsList)

    return newData

class Desde():
  
  


  def capDesde(self,newData,questionsList):
    print(questionsList[0])
    desde =str(input("DD/MM/AAAA: "))
    
    
    return desde

  def returnDesde(self,newData,questionsList):
    
    newData['Desde']=self.capDesde(newData,questionsList)
 

    
    return newData


class Unidad():
  def __init__(self,unidad=int(0)):
    self.unidad=unidad
  def printUnidad(self):
    estatuList=["T-01","T-02","T-03","T-04",
      "T-05","T-06","T-07","T-08", "T-09","T-10","T-11","T-12",
      "T-13","T-14","T-15","T-16",
      "T-17","T-18","T-19","T-20",
      "T-21","T-22","T-23","T-24",
      "T-25","T-26","T-27","T-28",
      "T-29","T-30","T-31","T-32",
      "T-33","T-34","T-35","T-36", "T-37",
      "T-38","T-39","T-40","T-41","T-42"]
    return estatuList

  def captUnidad(self,dict,listPrint):
    print(listPrint[2])
    che=Checker()
    estatuList=["1.- T-01","7.- T-07","13.- T-13","19.- T-19",
      "2.- T-02","8.- T-08","14.- T-14","20.- T-20",
      "3.- T-03","9.- T-09","15.- T-15","21.- T-21",
      "4.- T-04","10.- T-10","16.- T-16","22.- T-22",
      "5.- T-05","11.- T-11","17.- T-17","23.- T-23",
      "6.- T-06","12.- T-12","18.- T-18","24.- T-24",
      "25.- T-25","31.- T-31","37.- T-37","26.- T-26",
      "32.- T-32","38.- T-38","27.- T-27","33.- T-33",
      "39.- T-39","28.- T-28","34.- T-34","40.- T-40", "29.- T-29",
      "35.- T-35","41.- T-41","30.- T-30","36.- T-36","42.- T-42"]

    
    self.printUnidad()
    self.unid=str(input())
    self.unidad=che.checkerOptionExists(estatuList,self.unid)
    self.unid='T-'+str(self.unid)
    
    
    return self.unid
  def returnUnidad(self,dict,listPrint):
   
    dict['Unidad']=self.captUnidad(dict,listPrint)
    
    return dict

class Responsable():
  
  def printResponsable(self):
    respList=["P. Torres","jJ- Escamilla","M. Garcia","Ma. Fernanda","Denise","M. Pierce","E. Tristan","J. Moreira"]
    return respList


  def captResponsable(self,dict,list):
    print(list[8])
    self.printResponsable()
    che=Checker()
    respList=["","P. Torres","jJ- Escamilla","M. Garcia","Ma. Fernanda","Denise","M. Pierce","E. Tristan","J. Moreira"]
    responsable=str(input())
    responsable=che.checkerOptionExists(respList,responsable)
    return responsable

  def returnResponsable(self,dict,list):
    
    dict['Responsable']=self.captResponsable(dict,list)

    
    return dict


class Cliente():
 
  def captCliente(self,dict,list):


    clien=str(input())
    return clien

  def returnCliente(self,dict,list):
    

    print(list[3])
    dict['Cliente']=self.captCliente(dict,list)
    

    
    return dict


class CP():
 
  def captCP(self,newData,questionsList):
    print(questionsList[4])

    cp=str(input())
    return cp

  def returnCP(self,dict,list):
    

    print(list[4])
    dict['Carta porte']=self.captCP(dict,list)

    return dict
    
class Consigna():
 
  def captConsigna(self,dict,list):

    print(list[5])
    consig=str(input())
    return consig

  def returnConsigna(self,dict,list):
    
    consig=self.captConsigna(dict,list)
    dict['Consigna']=consig 
    
    return dict

class Manhattan():
 
  def captManhattan(self,dato,questionsList):

    print(questionsList[6])
    manhatt=str(input())
    return manhatt

  def returnManhattan(self,dict,list):
    print(list[6])
    manhatt=self.captManhattan(dict,list)
    dict['Folio Manhattan']=manhatt 
    
    return dict



class Estatus():
  def __init__(self,esta=int(0)):
    self.esta=esta
  def printEstatus(self):
    estatuList=["Pendiente","Recuperada - En Liquidación","Recuperada - Liquidada","En Devolución","Aclaración - Faltante",
    "Aclaración - Códigos Combinados","Aclaración - Otros","Pendiente por manhattan"]
    return estatuList
  
  def captEstatus(self,dict_,list):
    fEL=fechaEntregaLiquida()
    print(list[9]) 
    self.printEstatus()
    che=Checker()

    estatuList=["","Pendiente","Recuperada - En Liquidación","Recuperada - Liquidada","En Devolución","Aclaración - Faltante",
    "Aclaración - Códigos Combinados","Aclaración - Otros","Pendiente por manhattan"]
    self.esta=str(input())
    self.esta=che.checkerOptionExists(estatuList,self.esta)
    return estatuList[self.esta],dict_




class Importe():
 
  def captImporte(self,dict,list):
    che=Checker()
    print(list[10])

    consig=che.checkerFloat(str(input()))
    return consig

  def returnImporte(self,dict,list):


    dict['Importe']=self.captImporte(dict,list)
    
    return dict


class File():
  def __init__(self, name):
     self.name=name

  def retunrData(self):
    che=Checker()
    sh = gc.open(self.name) 
    worksheet = sh.get_worksheet(0)
    list_of_lists = worksheet.get_all_values()
    df = pd.DataFrame(list_of_lists[1:], columns =list_of_lists[0])
    df.index.name="Clave"
    print(df)

    #df=che.checkerOrdenFecha("%d/%m/%y","%d/%m/%Y",df,"Hasta")

     
    #df = df.sort_values(["Desde"])
    #worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    return df


class Filter():
  def __init__(self, desde, unidad, segmento, estatus, consigna,cartaPorte,dataFrame):
    self.desde=desde
    self.unidad=unidad
    self.segmento=segmento
    self.consigna=consigna
    self.estatus=estatus
    self.cartaPorte=cartaPorte
    self.dataFrame=dataFrame


  def filterDate(self):
    if self.desde!='':
      dateFil = self.dataFrame.loc[self.dataFrame['Desde'] == self.desde]
    else: 
      dateFil=self.dataFrame
    return dateFil
  def filterUnidad(self,dataToFilter):
    if self.unidad!="Unidad":
      dateFil = dataToFilter.loc[dataToFilter['Unidad']==self.unidad ]
    else: 
      dateFil=dataToFilter
    return dateFil

  def filterSegmen(self,dataToFilter):
    if self.segmento!='Segmento': 
      dateFil = dataToFilter.loc[dataToFilter['Segmento']==self.segmento]
    else: 
      dateFil=dataToFilter
    return dateFil
  
  def filterEstatu(self,dataToFilter):
    if self.estatus!='Estatus':
      dateFil = dataToFilter.loc[dataToFilter['Estatus'] == self.estatus]
    else: 
      dateFil=dataToFilter
    return dateFil
  
  def filterConsig(self,dataToFilter):
    if self.consigna!='':  
      dateFil = dataToFilter.loc[dataToFilter['Consigna'] == self.consigna]
    else: 
      dateFil=dataToFilter
    return dateFil
  
  def filterCarta(self,dataToFilter):
    if self.cartaPorte!='':  
      dateFil = dataToFilter.loc[dataToFilter['Carta porte'] == self.cartaPorte]
    else: 
      dateFil=dataToFilter
    return dateFil
  
  
  def processFilter(self):
    newData=self.filterDate()
    newData=self.filterUnidad(newData)
    newData=self.filterSegmen(newData)
    newData=self.filterEstatu(newData)
    newData=self.filterConsig(newData)
    newData=self.filterCarta(newData)

    return newData




class Situacion():
  def __init__(self,situaci=int(0)):
    self.situaci=situaci
  def printSituacion(self):
    situaList=["","Pendiente por faltante","Pendiente por folio de devolución","Pendiente de folio de viaje",
    "Documentacion incompleta","Documentacion incompleta L5",
    "Problema de captura en sistema de cliente","Problemas con almacén","Otro","Resulto"]
    return situaList
  
  def captSituacion(self,dict,list):
    che=Checker()
    print(list[11])
    self.printSituacion()
    situaList=["","Pendiente por faltante","Pendiente por folio de devolución","Pendiente de folio de viaje",
    "Documentacion incompleta","Documentacion incompleta L5",
    "Problema de captura en sistema de cliente","Problemas con almacén","Otro","Resulto"]
    self.situaci=str(input())
    self.situaci=che.checkerOptionExists(situaList,self.situaci)
    return self.situaci

  def returnSituacion(self,dict,list):
    
    

    dict['Situación']=self.captSituacion(dict,list)
    
    return dict
   

class Seguimiento():

  def __init__(self,segui=int(0)):
    self.segui=segui
  
  def printSeguimiento(self):
    seguimiList=["Ana Rojas","Karina Ordoñez","Ivan Flores","Susana Del Rayo","Roxana Bautista"]
    return seguimiList

  def captSegui(self,dicti,list_):
    print(list_[13])
    self.printSeguimiento()
    che=Checker()
    seguimiList=["","Ana Rojas","Karina Ordoñez","Ivan Flores","Susana Del Rayo","Roxana Bautista"]
    self.segui=str(input())
    self.segui=che.checkerOptionExists(seguimiList,self.segui)

    return seguimiList[self.segui]

  def returnSeguimiento(self,dicti,list_):



    
    dicti['Seguimiento con:']=self.captSegui(dicti,list_)

    return dicti


class Herdez():

  
  def  captuHerdez(self,listHer):
    herdez=[]
    listHer=listHer[14:17]
    for i in range (len(listHer)):
      print(listHer[i])
      herdez.append(str(input("-->")))
      
    return herdez
  
  def returnHerde(self,newData,questionsList):
    herdez=self.captuHerdez(questionsList)
    newData['Que se necesita como apoyo por parte de Herdez?']=herdez[0]
    newData['Seguimiento Herdez']=herdez[1]
    newData['Comentarios por parte de Herdez']=herdez[2]

    return newData
    
              


     
  

class fechaEntregaLiquida():
  def captLiqui(self,dict_):
    form=Formula()
    try:
      estatus=dict_.iloc[12]
    except:
      estatus=dict_
    todayPay=form.payDate(estatus["Estatus"])
   
    return todayPay

  def returnLiqui(self,dict):
    
    dict['Fecha de entrega de liquidación']=self.captLiqui(dict)
    
    return dict

class Edition():
  def __init__(self,edit,listRow):
    self.edit=edit
    self.listRow=listRow
 

  def edition(self):
    
    
    fi=File("prueba")
    dato=fi.retunrData()
    #Las posiciones de listEdition [0]= estatus, [1] = importe, [2] = Carta Porte,[3] = consigna, [4] = manhattan
    listEdition=[]
    rowEdit=dato.loc[int(self.edit)]
    listEdition.append(rowEdit.iloc[0])
    listEdition.append(rowEdit.iloc[1])
    listEdition.append(rowEdit.iloc[2])
    listEdition.append(rowEdit.iloc[3])

    unidad=self.listRow[0]
    if (unidad !="Unidad"):
      listEdition.append(unidad)
    else:
      listEdition.append(rowEdit.iloc[4])

    cleinte=self.listRow[6]
    if (cleinte !=""):
      listEdition.append(cartaPorte)
    elif((cleinte =="")) :
      listEdition.append(rowEdit.iloc[5])

    cartaPorte=self.listRow[1]
    if (cartaPorte !=""):
      listEdition.append(cartaPorte)
    elif((cartaPorte =="")) :
      listEdition.append(rowEdit.iloc[6])

    

    consigna = self.listRow[2]
    if (consigna !=""):
      listEdition.append(consigna)

    else :
      listEdition.append(rowEdit.iloc[7])
    
    manhatta=self.listRow[3]
    if (manhatta !=""):  
      listEdition.append(manhatta)
    else:
      listEdition.append(rowEdit.iloc[8])
    
    listEdition.append(rowEdit.iloc[9])
    listEdition.append(rowEdit.iloc[10])
    
    estatu=self.listRow[4]
    if estatu!='Estatus':
      listEdition.append(estatu)
    else :
      listEdition.append(rowEdit.iloc[11])
    #listEdition.append(rowEdit.iloc[11])
    importe=self.listRow[5]
    if importe!="":
      listEdition.append(importe)
    
    else :
      listEdition.append(rowEdit.iloc[12])
    
    listEdition.append(rowEdit.iloc[13])
    
    
    listEdition.append(rowEdit.iloc[14])

    
    listEdition.append(rowEdit.iloc[15])
    listEdition.append(rowEdit.iloc[16])
    listEdition.append(rowEdit.iloc[17])
    listEdition.append(rowEdit.iloc[18])
    listEdition.append(rowEdit.iloc[19])
    listEdition.append(rowEdit.iloc[20])
    listEdition.append(rowEdit.iloc[21])
    listEdition.append(rowEdit.iloc[22])
    listEdition.append(rowEdit.iloc[23])
    #listEdition.append(rowEdit.iloc[24])


    dato.loc[int(self.edit)]=listEdition
    sh = gc.open("prueba")
    
    worksheet = sh.get_worksheet(0)
    
    dato = dato.fillna('')
    

  
   
    dato.reset_index(drop=True, inplace=True)

    print(dato)
   
    worksheet.update([dato.columns.values.tolist()] + dato.values.tolist())

    


      

class Menu():
  def printMenu(self):
    print("1.- Ingrese un nuevo periodo\n\r 2.- Busque un periodo\n\r3.- Edite un periodo")

  def returnMenu(self):
    che=Checker()
    self.printMenu()
    menu=["","1.- Ingrese un nuevo periodo","\t2.- Busque un periodo","3.- Edite un periodo"]
    menuOp=str(input("Ingrese la acción que dese realizar: "))
    menuOp=che.checkerOptionExists(menu,menuOp)
    return menuOp
      

    

class Converter():
  
  def converInt(self,date):
     
      fecha_cadena=datetime.strptime(date,'%d/%m/%Y') 
      fecha_cadena=datetime.strftime(fecha_cadena.date(),'%d/%m/%Y')

      return fecha_cadena


class Formula():

  def formHasta(self,dateU):
    i=Converter()
    fecha_cadena=i.converInt(dateU)
    day=fecha_cadena[0:2]
    month=fecha_cadena[3:5]
    year=fecha_cadena[6:10]
    U=date(int(year),int(month),int(day))
   

    dateHasta = U + timedelta(days=6)
    dateHasta = dateHasta.strftime('%d/%m/%Y')
    return dateHasta


  def formDiasTrans(self,dataTrans):
    i=Converter()
    datehas=i.converInt(dataTrans)
    dataTrans=datetime.strptime(datehas,'%d/%m/%Y')
    today = date.today()
    remaining_days = (today-dataTrans.date()).days
    return remaining_days
  
  def diasTrans(self):
    o=File("prueba")
    dataTrans=o.retunrData()
 # make sure indexes pair with number of rows

    for index, row in dataTrans.iterrows():
      if row ['Estatus'] !="Recuperada - Liquidada":
        row['Dias trascurridos'] = str(self.formDiasTrans(str(row['Hasta'])))
        row['Clasificacion de dias en proceso'] = str(self.ClasDiasProceso(row['Dias trascurridos']))
      if int(row ['Dias trascurridos']) <=8:
        row['Estatus de la evidencia']="En tiempo"
      else:
        row['Estatus de la evidencia']="Vencido"

    writeOdj= Writer(dataFrame=dataTrans,name="prueba")
    writeOdj.writeNewData()

  def ClasDiasProceso(self,diasTrans):
    if(int(diasTrans)>=51):
      diasProcesados="+51 días transcurridos"
      return diasProcesados
      
    elif(int(diasTrans)>=21):
      diasProcesados="De 21 a 50 días transcurridos"
      return diasProcesados
    elif(int(diasTrans)>=13):
      diasProcesados="De 13 a 20 días transcurridos"
      return diasProcesados
    elif(int(diasTrans)>=6):
      diasProcesados="De 6 a 12 días transcurridos"
      return diasProcesados
    elif(int(diasTrans)>=0):
      diasProcesados="De 0 a 5 días transcurridos"
      return diasProcesados
    
    return 0


  def periodo(self,dataHasta,dataDesde):
    periodo=dataDesde+" al "+dataHasta
  
    return periodo
  
  def payDate(self,estatus): 
    
   
    if estatus=="Recuperada - Liquidada":
      today = datetime.now()
      todayPay=datetime.strptime(str(today.date()),'%Y-%m-%d')
      todayPay=datetime.strftime(today.date(),'%d/%m/%Y')

      print ("Se liquido el día: ",todayPay)
      
    
    else:
      todayPay=""
    
    return todayPay

  def estatuEvi(self,dictEE): 
    
    
    if int(dictEE ['Dias trascurridos']) <=8:
      dictEE['Estatus de la evidencia']="En tiempo"
    else:
      dictEE['Estatus de la evidencia']="Vencido"
        
      
    
   
    return dictEE



class Capturador():


    def inputData(self):
      desd=Desde()
      form=Formula()
      unid=Unidad()
      estatu=Estatus()
      segui=Seguimiento()
      responsa=Responsable()
      situa=Situacion()
      che=Checker()
      segObj=Segmento()
      clienObj=Cliente()

      cpObj=CP()
      consigObj=Consigna()
      manhatta=Manhattan()
      impor=Importe()
      herdezObj=Herdez()

      newData={'Desde':"",'Hasta':"",'Segmento':"",	'Unidad':""	,'Cliente':"", 'Carta porte':"",	'Consigna':"",	'Folio Manhattan':"",
      'Estatus de la evidencia':"hi",	'Responsable':"", 'Estatus':"", 'Importe':"",	'Situación':"",'Fecha de entrega de liquidación':"", 
      'Seguimiento con:':"",	'Que se necesita como apoyo por parte de Herdez?':"", 'Seguimiento Herdez':	"",
      'Comentarios por parte de Herdez':"",	'seguimiento  l5':"", 'Descuento':"", 'Dias trascurridos':"", 'Clasificacion de dias en proceso':"",
      'Periodo':""}

      questionsList=["Ingrese la Fecha de inicio del periodo\n\r", "Ingrese el segmento","Ingrese la Unidad\n\r","Ingrese el cliente\n\r","Ingrese el numero de carta porte\n\r", "Ingrese la consigna\n\r", "Folio Manhanttan\n\r",
      "¿Cuál es el estatus de la evidencia?\n\r","¿Quién es el responsable?\n\r","¿Cuál es el estatus?\n\r","¿Cuál es el importe?\n\r","¿En qué situación se encuentra?\n\r", "¿Cuándo se liquida/o?\n\r",
      "¿Quién le esta dando seguimento?\n\r","¿Qué se necesita como apoyo por parte de Herdez?\n\r","Seguimiento Herdez\n\r", "Comentarios por parte de Herdez\n\r"
      ,"Seguimiento  l5\n\r", "¿De cuánto es el descuento?\n\r", "¿Clasificacián de dias en proceso?\n\r"]
      
      newData=desd.returnDesde(newData,questionsList)
     
      newData['Hasta']=str(form.formHasta(str(newData['Desde'])))
      
      newData=segObj.returnSegmento(newData,questionsList)
      
      newData=unid.returnUnidad(newData,questionsList)


      newData=clienObj.returnCliente(newData,questionsList)
      newData=cpObj.returnCP(newData,questionsList)
      newData=consigObj.returnConsigna(newData,questionsList)
      newData=manhatta.returnManhattan(newData,questionsList)
      newData=responsa.returnResponsable(newData,questionsList)
      
 
      newData=estatu.s(newData,questionsList)
      
      
      newData=impor.returnImporte(newData,questionsList)

      
      
   
      newData=situa.returnSituacion(newData,questionsList)
      newData['Fecha de entrega de liquidación']=str(input(questionsList[12]))

      newData=segui.returnSeguimiento(newData,questionsList)
      newData=herdezObj.returnHerde(newData,questionsList)
      newData['seguimiento  l5']=str(input(questionsList[17]))
      newData['Descuento']=che.checkerFloat(str(input(questionsList[18])))
      
      newData['Dias trascurridos']=str(form.formDiasTrans(str(newData['Hasta'])))
      newData['Clasificacion de dias en proceso']=str(form.ClasDiasProceso(str(newData['Dias trascurridos'])))
      newData['Periodo']=str(form.periodo(str(newData['Desde']),str(newData['Hasta'])))

   
      return newData

   
      
      



class Writer():
  def __init__(self, newDa={},dataFrame={},name=""):
     self.newDa=newDa
     self.dataFrame=dataFrame
     self.name=name
    
  def writeNewData(self):
    global worksheet
    sh = gc.open(self.name)
    
    worksheet = sh.get_worksheet(0)
    
    self.dataFrame = self.dataFrame.fillna('')
    
    if  (not self.newDa):
      pass

    else: 
      self.dataFrame=self.dataFrame.append(self.newDa, ignore_index=True)
    print(self.dataFrame)
   
    self.dataFrame.reset_index(drop=True, inplace=True)

    print(self.dataFrame)
   
    worksheet.update([self.dataFrame.columns.values.tolist()] + self.dataFrame.values.tolist())

    










class ListBoxObj():
  def __init__(self,listForList,frame_,labe_,key):

    self.listForList=listForList
    self.frame_=frame_
    self.myLabel=Label(self.frame_,text="Seleccionado:")
    self.key=key
    self.labe_=labe_
  def makeListBox(self):
    scrollbar = Scrollbar(self.frame_,orient=VERTICAL)

    
    labe= Label(self.frame_, text =self.labe_,
          font = "10") 
    labe.pack()
    self.mylist = Listbox(self.frame_, yscrollcommand = scrollbar.set, width=30, height=6)
    self.mylist.pack(side = LEFT, fill = BOTH)
    scrollbar.pack(side = LEFT, fill = BOTH)
    for line in self.listForList: 
      self.mylist.insert(END,  str(line))
    
    self.mylist.config(yscrollcommand = scrollbar.set)
    
    
    


  def select(self):
    
    self.key=self.mylist.get(ANCHOR)

    self.myLabel.config(text=self.mylist.get(ANCHOR))
    self.myLabel.pack()





class FrameJe():
  def __init__(self,root,col,row_,color_, width_,height_):  
    self.root=root
    self.col=col
    self.row_=row_
    self.color_=color_
    self.width_=width_
    self.height_=height_
    
  
  def maker(self):

    marco_principal = Frame(self.root)
    marco_principal.grid( column=self.col,  sticky=N+S+W+E)
    marco_principal.config(width=self.width_, height=self.height_)
   
    marco_principal.grid_columnconfigure(0, weight=1)
    marco_principal.config(bg=self.color_)


class SubFrame(FrameJe):
  def __init__(self, root, col, row_, color_, width_, height_):
    super().__init__(root, col, row_, color_, width_, height_)
    self.root=root
    self.col=col
    self.row_=row_
    self.color_=color_
    self.width_=width_ 
    self.height_=height_
  def makerSub(self):

    marcoSubMarco = Frame(self.root)
    marcoSubMarco.grid(row=self.row_, column=self.col)
    marcoSubMarco.config(width=self.width_, height=self.height_)  
    marcoSubMarco.config(bg=self.color_)
    return marcoSubMarco

def is_valid_date(action, char, text):
    # Solo chequear cuando se añade un carácter.
    if action != "1":
        return True
    return char in "0123456789/" and len(text) < 10

def defiDict(newData):
  form=Formula()
  liquiObj=fechaEntregaLiquida()

  
  newData['Hasta']=str(form.formHasta(str(newData['Desde'])))
  newData['Dias trascurridos']=str(form.formDiasTrans(str(newData['Hasta'])))

  newData['Clasificacion de dias en proceso']=str(form.ClasDiasProceso(str(newData['Dias trascurridos'])))
  newData['Periodo']=str(form.periodo(str(newData['Hasta']),str(newData['Desde'])))
  day=liquiObj.captLiqui(newData)
  newData['Fecha de entrega de liquidación']=day
  newData=form.estatuEvi(newData)
  start= Formula()
  start.diasTrans()

  return newData


def guardar():
 

  newData={'Desde':"",'Hasta':"",'Segmento':"",	'Unidad':""	,'Cliente':"", 'Carta porte':"",	'Consigna':"",	'Folio Manhattan':"",
      'Estatus de la evidencia':"hi",	'Responsable':"", 'Estatus':"", 'Importe':"",	'Situación':"",'Fecha de entrega de liquidación':"", 
      'Seguimiento con:':"",	'Que se necesita como apoyo por parte de Herdez?':"",
      'Comentarios por parte de Herdez':"",	'seguimiento  l5':"", 'Descuento':"", 'Dias trascurridos':"", 'Clasificacion de dias en proceso':"",
      'Periodo':""}

  form=Formula()
 

  liquiObj=fechaEntregaLiquida()
 
  newData["Desde"]=desde.get()
  newData['Unidad']=mylistUnidad.key

  newData["Cliente"]=cliente.get()
  newData["Carta porte"]=cartaPorte.get()
  newData["Folio Manhattan"]=folioManhattan.get()
  newData["Consigna"]=consigna.get()

  
  
  newData["Importe"]=importe.get()
  
  newData["Que se necesita como apoyo por parte de Herdez?"]=apoyoHer.get()

  newData["Seguimiento Herdez"]=seguHer.get()
  newData["Comentarios por parte de Herdez"]=comenHerdez.get()
  newData['seguimiento  l5']=seguimi.get()
  newData['Descuento']=descuento.get()
  newData['Situación']=str(mylistSituacion.key)
  newData['Estatus']=mylistEstatus.key
  newData['Responsable']=mylistResponsable.key
  newData['Seguimiento con:']=mylistSegiomiento.key
  newData['Segmento']=mylistSegmento.key
  
  newData=defiDict(newData)

  o=File("prueba")
  dt=o.retunrData()
 
  newData["Clave"]=(dt.shape[0])
  e=Writer(newDa=newData,dataFrame=dt,name="prueba")
  e.writeNewData()
  
class DataFrameTable():
    def __init__(self, parent=None, df=pd.DataFrame()):

        
        self.parent = parent
        fram_=Frame(parent)

        fram_.pack(fill=BOTH, expand=True)

        self.table = Table(
            fram_, dataframe=df,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)
        self.table.show()


def buscar():
  fi=File("prueba")
  dataFill=fi.retunrData()

  #"Desde que periodo quiere buscar","¿Qué unidad busca?","¿Cuál segmento?","¿Cuál es el estatus?","¿Cuál es la consigna?"
  fil=Filter(desde.get(),mylistUnidad.key,mylistSegmento.key,mylistEstatus.key,consigna.get(),cartaPorte.get(),dataFill)  
  listas=fil.processFilter()
  
  ventana_nueva1 = Toplevel()
  
  table = DataFrameTable(ventana_nueva1, listas)
  start= Formula()
  start.diasTrans()
  ventana_nueva1.mainloop()


def editarGet(): 
  data=[]
  
  
 


  clave=claveEdit.get()
  UnidadEdit=mylistUnidad.key


  CartaPorteEdit=cartaPorte.get()
  FolioManEdit=folioManhattan.get()
  consignaEdit=consigna.get()

  clienteEdit=cliente.get()
  
  importeEdit=importe.get()

  
  estatusEdit=mylistEstatus.key



  data=[UnidadEdit,CartaPorteEdit,consignaEdit,FolioManEdit,estatusEdit,importeEdit,clienteEdit]
  #defiDict(responsableEdit)
  editObj=Edition(clave ,data )
  editObj.edition()
  start= Formula()
  start.diasTrans()
  return data ,clave


root = Tk()




unidadObj=Unidad()
listUnidad=unidadObj.printUnidad()

responsableObj=Responsable()
listResponsa=responsableObj.printResponsable()

segmenObj=Segmento()
listSegmento=segmenObj.printSegmento()

estatusObj=Estatus()
listEstatus=estatusObj.printEstatus()

situacionObj=Situacion()
listSituacion=situacionObj.printSituacion()

seguimientoObj=Seguimiento()
listSeguimiento=seguimientoObj.printSeguimiento()



marco_principal1= FrameJe(root, 5,2,"white",2,3)
marco_principal1= marco_principal1.maker()
#col,row
marco_principal2= FrameJe(root,2,2,"blue",2,3)
marco_principal2= marco_principal2.maker()
marco_principal3= Frame(root)
marco_principal3.grid( row=65,column=7)
marco_principal3.config(width=2, height=3)  


marco_principal11=SubFrame(marco_principal1,8,2,"white",2,3)
marco_principal11=marco_principal11.makerSub()

marco_principal02=SubFrame(marco_principal1,8,5,"white",2,3)
marco_principal02=marco_principal02.makerSub()

marco_principal03=SubFrame(marco_principal1,8,8,"white",2,3)
marco_principal03=marco_principal03.makerSub()

marco_principal04=SubFrame(marco_principal1,12,8,"white",2,3)
marco_principal04=marco_principal04.makerSub()

marco_principal05=SubFrame(marco_principal1,12,2,"white",2,3)
marco_principal05=marco_principal05.makerSub()

marco_principal06=SubFrame(marco_principal1,12,5,"white",2,3)
marco_principal06=marco_principal06.makerSub()

marco_principal13=FrameJe(root,3,5,"white",2,3)
marco_principal13=marco_principal13.maker()

marco_principal14=SubFrame(marco_principal1,6,6,"blue",2,3)
marco_principal14=marco_principal14.makerSub()

marco_principal15=SubFrame(marco_principal1,6,7,"blue",2,3)
marco_principal15=marco_principal15.makerSub()

marco_principal16=SubFrame(marco_principal1,6,8,"blue",2,3)
marco_principal16=marco_principal16.makerSub()

desdeLabel=Label(marco_principal2, text='Desde',width=20).grid(column=0,row=1)
desde=Entry(marco_principal2,width=20,font=("Arial",12))
desde.grid(column=1,row=1)


clienteLabel=Label(marco_principal2, text='Cliente',width=20).grid(column=0,row=2)
cliente=Entry(marco_principal2,width=20,font=("Arial",12))
cliente.grid(column=1,row=2)

cartaPorteLabel=Label(marco_principal2, text='Carta porte',width=20).grid(column=0,row=3)
cartaPorte=Entry(marco_principal2,width=20,font=("Arial",12))
cartaPorte.grid(column=1,row=3)

consignaLabel=Label(marco_principal2, text='¿Cuál es la consigna?',width=20).grid(column=0,row=4)
consigna=Entry(marco_principal2,width=20,font=("Arial",12))
consigna.grid(column=1,row=4)

folioManhattanLabel=Label(marco_principal2, text='Folio manhattan',width=20).grid(column=0,row=5)
folioManhattan=Entry(marco_principal2,width=20,font=("Arial",12))
folioManhattan.grid(column=1,row=5)


validatecommand = root.register(is_valid_date)
                
importeLabel=Label(marco_principal2, text='Importe',width=20).grid(column=0,row=6)
importe=Entry(marco_principal2,validate="key",width=20,font=("Arial",12), validatecommand=(validatecommand, "%d", "%S", "%s"))
importe.grid(column=1,row=6)

seguHerLabel=Label(marco_principal2, text='Seguimiento Herdez',width=20).grid(column=0,row=7)
seguHer=Entry(marco_principal2,width=20,font=("Arial",12))
seguHer.grid(column=1,row=7)


apoyoHerLabel=Label(marco_principal2, text='Apoyo por parte de Herdez',width=20).grid(column=0,row=8)
apoyoHer=Entry(marco_principal2,width=20,font=("Arial",12))
apoyoHer.grid(column=1,row=8)


comenHerdezLabel=Label(marco_principal2, text='Comentarios por parte de Herdez',width=30).grid(column=0,row=9)
comenHerdez=Entry(marco_principal2,width=20,font=("Arial",12))
comenHerdez.grid(column=1,row=9)


descuentoLabel=Label(marco_principal2, text='Descuento',width=20).grid(column=0,row=10)
descuento=Entry(marco_principal2,width=20,font=("Arial",12))
descuento.grid(column=1,row=10)


seguimiLabel=Label(marco_principal2, text='Seguimiento L5',width=20).grid(column=0,row=11)
seguimi=Entry(marco_principal2,width=20,font=("Arial",11))
seguimi.grid(column=1,row=11)

seguimiLabel=Label(marco_principal2, text='Seguimiento L5',width=20).grid(column=0,row=11)
seguimi=Entry(marco_principal2,width=20,font=("Arial",11))
seguimi.grid(column=1,row=11)



claveLabel=Label(marco_principal2, text='Clave de edición',width=20).grid(column=0,row=13)
claveEdit=Entry(marco_principal2,width=20,font=("Arial",11))
claveEdit.grid(column=1,row=13)

my_label= Label()
my_label.grid(row=2)    

a="Elija la unidad"
mylistUnidad =ListBoxObj(listUnidad, marco_principal11,a,"Unidad")
mylistUnidad.makeListBox()


mylistResponsable =ListBoxObj(listResponsa, marco_principal02,"¿Quién es el responsable?",'Responsable')
mylistResponsable.makeListBox()

mylistEstatus =ListBoxObj(listEstatus, marco_principal03,"¿Cuál es el estado?","Estatus")
mylistEstatus.makeListBox()


mylistSituacion =ListBoxObj(listSituacion, marco_principal04,"¿Cuál es la situación?","Situación")
mylistSituacion.makeListBox()

mylistSegiomiento =ListBoxObj(listSeguimiento, marco_principal05,"Seguimiento","Seguimiento con:")
mylistSegiomiento.makeListBox()

mylistSegmento =ListBoxObj(listSegmento, marco_principal06,"Segmento","Segmento")
mylistSegmento.makeListBox()




my_buttonEs= Button(marco_principal13, text="Guardar", command=guardar)
my_buttonBus= Button(marco_principal13, text="Buscar", command=buscar)
my_buttonEdit= Button(marco_principal13, text="Editar", command=editarGet)
my_button2= Button(marco_principal11, text="Ok", command=mylistUnidad.select)
my_button3= Button(marco_principal02, text="Ok", command=mylistResponsable.select)
my_button11= Button(marco_principal06, text="Ok", command=mylistSegmento.select)
my_button4= Button(marco_principal03, text="Ok", command=mylistEstatus.select)
my_button5= Button(marco_principal04, text="Ok", command=mylistSituacion.select)
my_button6= Button(marco_principal05, text="Ok", command=mylistSegiomiento.select)

my_buttonEs.grid(column=2,row=50)
my_buttonBus.grid(column=4,row=50)
my_buttonEdit.grid(column=6,row=50)
my_button2.pack()
my_button3.pack()
my_button11.pack()
my_button4.pack()
my_button5.pack()
my_button6.pack()
root.mainloop()
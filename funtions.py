
from ast import Return
from optparse import Option
from pickle import APPEND
import gspread
import pandas as pd
from datetime import timedelta
from datetime import date 

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
  
  def checkerFecha(self,strVariable):
    try:
      variableFloat=int(strVariable)
      return variableFloat
    except:
      print("El valor debe ser flotante")

      variableFloat=str(input("Ingrese la cantidad en flotante"))
      return self.checkerFloat(variableFloat)


  def checkerOptionExists(self,listToChecker,option):
    option=self.checkerInt(option)
    if ((option <=(len(listToChecker)-1)) and (option>0)):
      
      return option
    else:
      print("No se encuentra en las opciones")

      option=str  (input("Ingrese una opción valida: "))
      return self.checkerOptionExists(listToChecker,option)
      
  def checkFilNoEMT(self, listEmty):
    for i in range (listEmty):
      pass
    

class Segmento():

  
  def printSegmento(self):
    print("1.- Dedicado Circuito\n\r2.- Dedicado Zumpango\n\r3.- Patio SLP\n\r",
    "4.- Incentivo\n\r 5.- SLP-LMM\n\r6.- SLP-Foráneo\n\r")
  
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
  
  def printUnidad(self):
    print("DD/MM/AAAA")


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
    print("1.- T-01\t7.- T-07\t13.- T-13\t19.- T-19",
      "\n\r2.- T-02\t8.- T-08\t14.- T-14\t20.- T-20",
      "\n\r3.- T-03\t9.- T-09\t15.- T-15\t21.- T-21",
      "\n\r4.- T-04\t10.- T-10\t16.- T-16\t22.- T-22",
      "\n\r5.- T-05\t11.- T-11\t17.- T-17\t23.- T-23",
      "\n\r6.- T-06\t12.- T-12\t18.- T-18\t24.- T-24",
      "\n\r----------------------------------------------",
      "\n\r25.- T-25\t31.- T-31\t37.- T-37", 
      "\n\r26.- T-26\t32.- T-32\t38.- T-38",
      "\n\r27.- T-27\t33.- T-33\t39.- T-39",
      "\n\r28.- T-28\t34.- T-34\t40.- T-40", 
      "\n\r29.- T-29\t35.- T-35\t41.- T-41",
      "\n\r30.- T-30\t36.- T-36\t42.- T-42",)

  def captUnidad(self,dict,listPrint):
    print(listPrint[2])
    che=Checker()
    
    self.printUnidad()
    self.unid=str(input())
    self.unidad=che.checkerInt(self.unid)
    self.unid='T-'+str(self.unid)
    
    
    return self.unid
  def returnUnidad(self,dict,listPrint):
   
    dict['Unidad']=self.captUnidad(dict,listPrint)
    
    return dict

class Responsable():
  
  def printResponsable(self):
    print("1.- P. Torres\n\r2.- jJ- Escamilla\n\r3.- M. Garcia\n\r","4.- Ma. Fernanda\n\r 5.- Denise\n\r6.- M. Pierce\n\r7.- E. Tristan\n\r8.- J. Moreira")

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
 
  def captliente(self,dict,list):


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
    dict['CP']=self.captCP(dict,list)

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
    print("1.- Pendiente\n\r2.- Recuperada - En Liquidación\n\r3.- Recuperada - Liquidada\n\r","4.- En Devolución\n\r 5.- Aclaración - Faltante",
    "\n\r6.- Aclaración - Códigos Combinados\n\r7.- Aclaración - Otros\n\r8.- Pendiente por manhattan")
  
  def captEstatus(self,dict,list):
    print(list[9]) 
    self.printEstatus()
    che=Checker()

    estatuList=["","Pendiente","Recuperada - En Liquidación","Recuperada - Liquidada","En Devolución","Aclaración - Faltante",
    "Aclaración - Códigos Combinados","Aclaración - Otros","Pendiente por manhattan"]
    self.esta=str(input())
    self.esta=che.checkerOptionExists(estatuList,self.esta)
    return estatuList[self.esta]


  def returnEstatus(self,dict,list):
   

    dict['Estatus']=self.captEstatus(dict,list)
    
    return dict

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
    global worksheet
    sh = gc.open(self.name) 
    worksheet = sh.get_worksheet(0)
    list_of_lists = worksheet.get_all_values()
    df = pd.DataFrame(list_of_lists[1:], columns =list_of_lists[0])
    df.index.name="Clave"
    return df


class Filter():
  def __init__(self, desde, unidad, segmento, estatus, consigna,dataFrame):
    self.desde=desde
    self.unidad=unidad
    self.segmento=segmento
    self.consigna=consigna
    self.estatus=estatus
    self.dataFrame=dataFrame


  def filterDate(self):
    if self.desde!='':
      dateFil = self.dataFrame.loc[self.dataFrame['Desde'] == self.desde]
    else: 
      dateFil=self.dataFrame
    return dateFil
  def filterUnidad(self,dataToFilter):
    if self.unidad!="":
      dateFil = dataToFilter.loc[dataToFilter['Unidad']==self.unidad ]
    else: 
      dateFil=dataToFilter
    return dateFil

  def filterSegmen(self,dataToFilter):
    if self.segmento!='': 
      dateFil = dataToFilter.loc[dataToFilter['Segmento']==self.segmento]
    else: 
      dateFil=dataToFilter
    return dateFil
  
  def filterEstatu(self,dataToFilter):
    if self.estatus!='':
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
  
  
  def processFilter(self):
    newData=self.filterDate()
    newData=self.filterUnidad(newData)
    newData=self.filterSegmen(newData)
    newData=self.filterEstatu(newData)
    newData=self.filterConsig(newData)
    print(newData)
    return newData




class Situacion():
  def __init__(self,situaci=int(0)):
    self.situaci=situaci
  def printSituacion(self):
    print("1.- Pendiente por faltante\n\r2.- Pendiente por folio de devolución\n\r3.- Pendiente de folio de viaje\n\r","4.- Documentacion incompleta\n\r 5.- Documentacion incompleta L5",
    "6.- Problema de captura en sistema de cliente\n\r7.- Problemas con almacén\n\r8.- Otro\n\r","9.- Resulto")
  
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
    print("1.- Ana Rojas\n\r2.- Karina Ordoñez\n\r3.- Ivan Flores\n\r","4.- Susana Del Rayo\n\r 5.- Roxana Bautista")
  
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
  def captEL(self,dict,list):
    print(list[12])

    entLiqui=str(input())
    return entLiqui

  def returnManhattan(self,dict,list):

    
    dict['Fecha de entrega de liquidación']=self.captEL(dict,list)
    
    return dict

class Edition():
  #def __init__(self,listToEdit):
   # self.listToEdit=listToEdit


  def printOptEdition(self,listToEdit):
    
    listEdit=listToEdit.reset_index(drop=True)
    listEdit.index = listToEdit.index + 1
    print(listToEdit)
    return listEdit
  
  def editionSelect(self):
    edi=Edition()
    che=Checker()
    captu=Capturador()
    fi=File("prueba")
    dataFill=fi.retunrData()
    listFilter=captu.capturToFilter()
    fil=Filter(listFilter[0],listFilter[1],listFilter[2],listFilter[3],listFilter[4],dataFill)  
    filList=fil.processFilter()
    re=edi.printOptEdition(filList)
    editionMenu=["¿Desea Editar alguna evidencia?", "Elija la evidencia que desea editar: "]
    
    option=str(input(editionMenu[1]))
#    option=che.checkerOptionExists(option)
    return option, dataFill

  def edition(self):
    edit,dato=self.editionSelect()
    listEdition=[]
    uniObj=Unidad()
    estaObj=Estatus()
    

    cpObj=CP()
    consigObj=Consigna()
    manhatObj=Manhattan()
    impor=Importe()

    
    
    questionsList=["Ingrese la Fecha de inicio del periodo\n\r", "Ingrese el segmento","Ingrese la Unidad\n\r","Ingrese el cliente\n\r","Ingrese el numero de carta porte\n\r", "Ingrese la consigna\n\r", "Folio Manhanttan\n\r",
      "¿Cuál es el estatus de la evidencia?\n\r","¿Quién es el responsable?\n\r","¿Cuál es el estatus?\n\r","¿Cuál es el importe?\n\r","¿En qué situación se encuentra?\n\r", "¿Cuándo se liquida/o?\n\r",
      "¿Quién le esta dando seguimento?\n\r","¿Qué se necesita como apoyo por parte de Herdez?\n\r","Seguimiento Herdez\n\r", "Comentarios por parte de Herdez\n\r"
      ,"Seguimiento  l5\n\r", "¿De cuánto es el descuento?\n\r", "¿Clasificacián de dias en proceso?\n\r"]
    
    #Las posiciones de listEdition [0]= estatus, [1] = importe, [2] = Carta Porte,[3] = consigna, [4] = manhattan
    #  
    rowEdit=dato.loc[int(edit)]
    listEdition.append(rowEdit.iloc[0])
    listEdition.append(rowEdit.iloc[1])
    listEdition.append(rowEdit.iloc[2])
 

    unidad=uniObj.captUnidad(dato,questionsList)
    if (unidad !=""):
      listEdition.append(unidad)
    listEdition.append(rowEdit.iloc[4])

    cartaPorte=cpObj.captCP(dato,questionsList)
    if (cartaPorte !=""):
      listEdition.append(cartaPorte)
    else :
      listEdition.append(rowEdit.iloc[5])

    consigna = consigObj.captConsigna(dato,questionsList)
    if (consigna !=""):
      listEdition.append(consigna)

    else :
      listEdition.append(rowEdit.iloc[6])
    
    manhatta=manhatObj.captManhattan(dato,questionsList)
    if (manhatta !=""):  
      listEdition.append(manhatta)
    else:
      listEdition.append(rowEdit.iloc[7])
    
    listEdition.append(rowEdit.iloc[8])
    listEdition.append(rowEdit.iloc[9])
    
    estatu=estaObj.captEstatus(dato,questionsList)
    if estatu!="":
      listEdition.append(estatu)
    else :
      listEdition.append(rowEdit.iloc[10])
    
    importe=impor.captImporte(dato,questionsList)
    if importe!="":
      listEdition.append(importe)
    
    else :
      listEdition.append(rowEdit.iloc[11])
    
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

 
    
    #newData={'0 Desde':"",'1Hasta':"",'2 Segmento':"",	'3 Unidad':""	,'4 Cliente':"", '5 CP':"",	'6 Consigna':"",	'7 Folio Manhattan':"",
     # '8 Estatus de la evidencia':"hi",	'9 Responsable':"", '10 Estatus':"", '11 Importe':"",	'12 Situación':"",'13 Fecha de entrega de liquidación':"", 
     # '14 Seguimiento con:':"",	'15 Que se necesita como apoyo por parte de Herdez?':"", '16 Seguimiento Herdez':	"",
      #'17 Comentarios por parte de Herdez':"",	'18 seguimiento  l5':"", '19 Descuento':"", '20 Dias trascurridos':"", '21 Clasificacion de dias en proceso':"",
      #'22 Periodo':""}
    dato.loc[int(edit)]=listEdition
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

class Select():

  def selectProces(self):
    menu=Menu()
    menuOp=menu.returnMenu()
    return menuOp
  
  def playProcess(self):
    processLog=self.selectProces()
    captu=Capturador()
    
    if processLog==1:
      o=File("prueba")
      dt=o.retunrData()
      print(dt)
      i=captu.inputData()
      e=writer(i,dt,"prueba")
      e.writeNewData()
    elif processLog==2:
      fi=File("prueba")
      dataFill=fi.retunrData()
      listFilter=captu.capturToFilter()
      fil=Filter(listFilter[0],listFilter[1],listFilter[2],listFilter[3],listFilter[4],dataFill)  
      fil.processFilter()
    
    elif processLog==3:
      editObj=Edition()

      editObj.edition()
      pass
      

    

class Converter():
  
  def converInt(self,date):
      listDate=[]
      listDate.append(int(date[0:2]))
      listDate.append(int(date[3:5]))
      listDate.append(int(date[6:10]))

      return listDate


class Formula():

  def formHasta(self,dateU):
    i=Converter()
    datehas=i.converInt(dateU)
    U=date(datehas[2],datehas[1], datehas[0])

    dateHasta = U + timedelta(days=6)
    dateHasta = dateHasta.strftime('%d/%m/%Y')
    return dateHasta


  def formDiasTrans(self,dataTrans):
    i=Converter()
    datehas=i.converInt(dataTrans)
    dataTrans=date(datehas[2],datehas[1], datehas[0])
    today = date.today()
    remaining_days = (today-dataTrans).days
    return remaining_days
    

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
    periodo=dataDesde+"AL"+dataHasta
  
    return periodo

  


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

      newData={'Desde':"",'Hasta':"",'Segmento':"",	'Unidad':""	,'Cliente':"", 'CP':"",	'Consigna':"",	'Folio Manhattan':"",
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
      
 
      newData=estatu.returnEstatus(newData,questionsList)
      
      
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

    def capturToFilter(self):
      optFilPrint=["Desde que periodo quiere buscar","¿Qué unidad busca?","¿Cuál segmento?","¿Cuál es el estatus?","¿Cuál es la consigna?"]
      optFilter=[]
      for i in range(len(optFilPrint)):
        print(optFilPrint[i])
        optFilter.append(input("-->"))
      
      return optFilter
      
      



      


class writer():
  def __init__(self, newDa,dataFrame,name):
     self.newDa=newDa
     self.dataFrame=dataFrame
     self.name=name
    
  def writeNewData(self):
    global worksheet
    sh = gc.open(self.name)
    
    worksheet = sh.get_worksheet(0)
    
    self.dataFrame = self.dataFrame.fillna('')
    

    
    self.dataFrame=self.dataFrame.append(self.newDa, ignore_index=True)
    print(self.dataFrame)
   
    self.dataFrame.reset_index(drop=True, inplace=True)

    print(self.dataFrame)
   
    worksheet.update([self.dataFrame.columns.values.tolist()] + self.dataFrame.values.tolist())

    









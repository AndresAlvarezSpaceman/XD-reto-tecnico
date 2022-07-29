#importamos las librerias
import requests, statistics
from statistics import mode

#Variables globales
ListView = []
ListTimeView = []
ListOwner = []
ContTrue = 0
ContFalse = 0

#Consumo de enlace
url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
data = requests.get(url)

#Analisis de respuesta
if data.status_code == 200:
    data = data.json() #Guardamos la respuesta en una lista
    res = True
    #Reccorrido a travez de la lista y extraccion de los datos necesarios 
    for e in data['items']:
        #Extraemos las respues de verdadero y falso
        if e['is_answered'] == True:
            ContTrue += 1
        else:
            ContFalse += 1
        #Extraemos la cantidad de vistas por respuesta 
        ListView.append(e['view_count'])
        #Extraemos los tiempos de Respuesta
        ListTimeView.append(e['last_activity_date'])
        #Extraemos el Id de los Owners
        ListOwner.append(e['owner']['user_id'])

else:
    res = False
    print("Error al acceder a la liga")         

#Metodo donde identificamos la respuesta con menor respuestas, regresamos el valor y lo imprimimos la respuesta en la consola 
def LowView():
    print("La respuesta con menor numero de vistas es la numero " + str(ListView.index(min(ListView))) + " con : " + str(min(ListView))+" views")    
    return str(ListView.index(min(ListView))),str(min(ListView))

#Metodo donde identificamos el owner en que más respuestas se repite , regresamos el valor y lo imprimimos la respuesta en la consola
def OwnRes():
    print("El owner que más se repite en las respuestas es: " + str(mode(ListOwner)))    
    return str(mode(ListOwner))

#Metodo donde identificamos la cantidad de repuestas verdaderas y falsas, regresamos el valor y lo imprimimos la respuesta en la consola
def CantRes():
    print("Se encontraron "+str(ContTrue)+" respuestas de verdadero")
    print("Se encontraron "+str(ContFalse)+" respuestas de falso") 
    return str(ContTrue),str(ContFalse)

#Metodo donde identificamos la respuesta mas nueva, regresamos el valor y lo imprimimos la respuesta en la consola
def TimeRespNew():
    print("La respuesta más nueva es la numero "+ str(ListTimeView.index(max(ListTimeView)))+" con el valor de :" + str(max(ListTimeView)))
    return str(ListTimeView.index(max(ListTimeView))), str(max(ListTimeView))

#Metodo donde identificamos la respuesta mas vieja, regresamos el valor y lo imprimimos la respuesta en la consola
def TimeRespOld():
    print("La respuesta más antigua es la numero "+ str(ListTimeView.index(min(ListTimeView)))+" con el valor de :" + str(min(ListTimeView)))
    return str(ListTimeView.index(min(ListTimeView))), str(min(ListTimeView))

#Metodo donde retornamos el resultado de la conexión
def ResLink():
    return res











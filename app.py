from flask import Flask, render_template #Importamos la libreria de Flask para montar la pagina localmente
import programacion as programacion #Importamos los metodos de la aplicacion de programación
import requests #Importamos las librerias para consumir un enlace

#Especificamos la Url de la API
url = 'https://f7y9k0cdhb.execute-api.us-west-1.amazonaws.com/default/Sql_data'

#Metodo para extraer los valores tipo JSON y alamacenarlos en listas
def LambdaApi():
    data = requests.get(url)
    if data.status_code == 200: #Si la respuesta es valida almacenamos los valores
        data = data.json()
        DatAeropuerto = str(data['items'][0]['Aeropuerto'])
        DatAerolinea = str(data['items'][0]['Aerolineas'])
        DatVuelos = str(data['items'][0]['Vuelos'])
        DatVuelosDos = str(data['items'][0]['VuelosDos'])
    return DatAeropuerto, DatAerolinea, DatVuelos, DatVuelosDos

#Creacion de un objeto de flask
app = Flask(__name__)

#Especificamos las acciones de la ruta principal
@app.route('/')
def main():
    #Verificamos que haya conexión con el enlace
    if programacion.ResLink():
        #Almacenamos los valores en listas
        menorView = programacion.LowView()
        mayorOwn = programacion.OwnRes()
        tipRes = programacion.CantRes()
        timRespNueva = programacion.TimeRespNew()
        timRespVieja = programacion.TimeRespOld()
        datLambda = LambdaApi()
        #Regresamos a la ruta principal la pagina que tiene que estar en la carpeta "templates" 
        #Especificamos las variables que se indexaran a la pagina en HTML
        return render_template('index.html', peticion="Se realizo la peticion exitosamente", 
        outMenorNum = menorView[0], outMenCan = menorView[1],
        outOwn = mayorOwn,
        outResTrue = tipRes[0], outResFals = tipRes[1],
        outNumNew = timRespNueva[0], outTimNew = timRespNueva[1],
        outNumOld = timRespVieja[0], outTimOld = timRespVieja[1],
        outAeropuerto = datLambda[0],
        outAerolinea = datLambda[1],
        outVuelos = datLambda[2],
        outVuelosDos = datLambda[3]
        )
    else:
        return "Error al realizar la peticion"

#Corremos la aplicacion, especificamos el puerto y activamos el 
#debug en la consola para la aplicacion se reinicie al hacer una modificacion a las dependencias
if __name__ == '__main__':
    app.run(port = 3000,debug = True)

from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render



class Persona(object):
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad


def saludo(request): #primera vista

    p1=Persona("César","Abadía",43)
    temasDelCurso=["Plantillas","Módelos","Vistas","Despliegue"]
    #doc_externo=open("/home/seuz716/Escritorio/DjangoProject/Proyecto1/Proyecto1/plantillas/mi_plantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template("mi_plantilla.html")
    #ctx= Context({"nombreUsuario":p1.nombre,"apellidoUser":p1.apellido,"edadUser":p1.edad, "temas":temasDelCurso})
    #cuerpo = doc_externo.render({"nombreUsuario":p1.nombre,"apellidoUser":p1.apellido,"edadUser":p1.edad, "temas":temasDelCurso})

    return render(request,"mi_plantilla.html", {"nombreUsuario":p1.nombre,"apellidoUser":p1.apellido,"edadUser":p1.edad, "temas":temasDelCurso})

def despedida(request): #primera vista
    return HttpResponse("Despedida Pagina")    

def hora(request):
    fecha_actual=datetime.datetime.now()  
    cuerpo="""<html>
        <body> <h3>Fecha y hora actuales %s </h3>
        </body> 
        </html>"""% fecha_actual 
    return HttpResponse(cuerpo) 

def fecha(request, year,edad):
    periodo = year - 2023 
    edadFutura = edad+periodo   
    cuerpo="""<html>
        <body> <h3>En el año %s tendras %s años </h3>
        </body> 
        </html>"""%(year,edadFutura) 
    return HttpResponse(cuerpo)
  
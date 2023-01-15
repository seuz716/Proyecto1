from django.http import HttpResponse
import datetime

def saludo(request): #primera vista
    cuerpo="""<html>
    <body> <h1>Severa Gurrupleta</h1>
    </body> 
    </html>""" 
    return HttpResponse(cuerpo)

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
  
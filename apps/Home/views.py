from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
import json
from datetime import datetime, timedelta

def main(request):
	return render(request, 'home.html')

def Historial(request):
	#end = datetime.now().strftime('%B %d, %Y - %H:%M:%S'); start = (datetime.now()-timedelta(weeks=4)).strftime('%B %d, %Y - %H:%M:%S')
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.filter(date__range=(str(start),str(end)) )
	#syrus_data = models.Data.objects.all().order_by('-id')[:30][::-1] #Los ultimos 30 datos
	#syrus_data = models.Data.objects.all() #Todos los datos en la base
	#print syrus_data[1].date
	return render(request, 'historial.html',{'syrus_data':syrus_data})

def Fechas(request):
	start_date = request.GET['start_date']
	print start_date
	end_date = request.GET['end_date']
	syrus_data = models.Data.objects.filter(date__range=(start_date, end_date))
	enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date for s in syrus_data]
	return JsonResponse({'puntos': str(enviar).replace("'",""), 'date': dic_fechas})

def TiempoReal(request):
	syrus_data = models.Data.objects.last()
	return render(request, 'real_time.html',{'s':syrus_data})

def Update(request):
	current_id = int(request.GET['current_id'])
	s = models.Data.objects.last()
	print s.id
	if s.id > current_id:
		enviar = "({lat: %s, lng: %s})"%(s.latitude, s.longitude)
		#return HttpResponse(enviar)
		return JsonResponse({'puntos': enviar, 'id':s.id, 'date': s.date})
	else:
		return HttpResponse("no")

def Historial_by_area(request):
	syrus_data = models.Data.objects.all()
	return render(request, 'historial_by_area.html',{'syrus_data':syrus_data})

def Area(request):
	start_lat = request.GET['start_lat']; start_lng = request.GET['start_lng']
	end_lat = request.GET['end_lat']; end_lng = request.GET['end_lng']
	syrus_data = models.Data.objects.filter(latitude__range=(start_lat, end_lat),longitude__range=(start_lng, end_lng))
	enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date for s in syrus_data]
	#return render(request, 'fecha.html', {'syrus_data': syrus_data})
	#return HttpResponse(str(enviar).replace("'",""))
	return JsonResponse({'puntos':str(enviar).replace("'",""), 'fechas': dic_fechas})
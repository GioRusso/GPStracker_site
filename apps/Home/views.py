from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
import json
from datetime import datetime, timedelta

def main(request):
	return render(request, 'home.html')

def Historial(request):
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.filter(date__range=(str(start),str(end))).order_by('date')
	return render(request, 'historial.html',{'syrus_data':syrus_data})

def Fechas(request):
	start_date = request.GET['start_date']
	end_date = request.GET['end_date']
	syrus_data = models.Data.objects.filter(date__range=(start_date, end_date)).order_by('date')
	enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date.strftime("%B %d, %Y, %I:%M%p") for s in syrus_data]
	alturas = [s.elevation for s in syrus_data]
	return JsonResponse({'puntos': str(enviar).replace("'",""), 'date': dic_fechas, 'alturas': alturas})


def Historial_Cel(request):
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.raw("SELECT * FROM android_data WHERE (date BETWEEN '%s' AND '%s') ORDER BY date;"%(start,end))
	for s in syrus_data:
		print(s.gps_id)
	return render(request, 'historial_cel.html',{'syrus_data':syrus_data})

def Fechas_Cel(request):
	start_date = request.GET['start_date']
	end_date = request.GET['end_date']
	syrus_data = models.Data.objects.raw("SELECT * FROM android_data WHERE (date BETWEEN '%s' AND '%s') ORDER BY date;"%(start_date,end_date))
	enviar = [{'lat': str(s.longitude), 'lng': str(s.latitude)} for s in syrus_data]
	dic_fechas = [s.date.strftime("%B %d, %Y, %I:%M%p") for s in syrus_data]
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
		return JsonResponse({'puntos': enviar, 'id':s.id, 'date': s.date, 'elevation': s.elevation})
	else:
		return HttpResponse("no")

def Historial_by_area(request):
	syrus_data = models.Data.objects.all()
	return render(request, 'historial_by_area.html',{'syrus_data':syrus_data})

def Area(request):
	start_lat = request.GET['start_lat']; start_lng = request.GET['start_lng']
	end_lat = request.GET['end_lat']; end_lng = request.GET['end_lng']
	start_lat= "+"+start_lat
	end_lat= "+"+end_lat
	syrus_data = models.Data.objects.filter(latitude__range=(start_lat, end_lat),longitude__range=(start_lng, end_lng)).order_by('date')
	#SELECT * FROM Home_data WHERE (latitude BETWEEN 11.0196 AND 11.0198) AND (longitude BETWEEN -74.8508 AND -74.8506); 
	#COMO FUNCIONA: syrus_data = models.Data.objects.filter(latitude__range=("+10.998","+10.999"),longitude__range=("-74.80722","-74.80730"))
	print syrus_data
	enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date.strftime("%B %d, %Y, %I:%M%p") for s in syrus_data]
	return JsonResponse({'puntos':str(enviar).replace("'",""), 'fechas': dic_fechas})

def Historial_Area(request):
	#end = datetime.now().strftime('%B %d, %Y - %H:%M:%S'); start = (datetime.now()-timedelta(weeks=4)).strftime('%B %d, %Y - %H:%M:%S')
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.filter(date__range=(str(start),str(end)) ).order_by('date')
	#syrus_data = models.Data.objects.all().order_by('-id')[:30][::-1] #Los ultimos 30 datos
	#syrus_data = models.Data.objects.all() #Todos los datos en la base
	#print syrus_data[1].date
	return render(request, 'historial_area.html',{'syrus_data':syrus_data})

def Fechas_Area(request):
	start_date = request.GET['start_date']
	print start_date
	end_date = request.GET['end_date']
	syrus_data = models.Data.objects.filter(date__range=(start_date, end_date)).order_by('date')
	enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date for s in syrus_data]
	return JsonResponse({'puntos': str(enviar).replace("'",""), 'date': dic_fechas})

def Elevacion(request):
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.filter(date__range=(str(start),str(end))).order_by('date')
	return render(request, 'elevacion.html',{'syrus_data':syrus_data})

def Elevation(request):
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=3)
	#syrus_data = models.Data.objects.filter(date__range=(str(start),str(end))).order_by('date')
	syrus_data = [{'latitude':11.002106	,'longitude':-74.831804},
{'latitude':11.002190	,'longitude':-74.830881},
{'latitude':11.001937	,'longitude':-74.830152},
{'latitude':11.001432	,'longitude':-74.829122},
{'latitude':11.000946	,'longitude':-74.828183},
{'latitude':11.000716	,'longitude':-74.827705},
{'latitude':11.000926	,'longitude':-74.827662},
{'latitude':11.001474	,'longitude':-74.827341},
{'latitude':11.001685	,'longitude':-74.827856},
{'latitude':11.001937	,'longitude':-74.828392},
{'latitude':11.002190	,'longitude':-74.828886},
{'latitude':11.002611	,'longitude':-74.829637},
{'latitude':11.002969	,'longitude':-74.830516},
{'latitude':11.003033	,'longitude':-74.831675},
{'latitude':11.002948	,'longitude':-74.832619},
{'latitude':11.003138	,'longitude':-74.833220},
{'latitude':11.003328	,'longitude':-74.833907},
{'latitude':11.003370	,'longitude':-74.834593},
{'latitude':11.003981	,'longitude':-74.834754},
{'latitude':11.003896	,'longitude':-74.834164},
{'latitude':11.003707	,'longitude':-74.833585},
{'latitude':11.003528	,'longitude':-74.832952},
{'latitude':11.003370	,'longitude':-74.832533},
{'latitude':11.003370	,'longitude':-74.831879},
{'latitude':11.003412	,'longitude':-74.831117},
{'latitude':11.003359	,'longitude':-74.830602},
{'latitude':11.003264	,'longitude':-74.830109},
{'latitude':11.003075	,'longitude':-74.829561},
{'latitude':11.003412	,'longitude':-74.829379},
{'latitude':11.003707	,'longitude':-74.829830},
{'latitude':11.003812	,'longitude':-74.830216},
{'latitude':11.003854	,'longitude':-74.830975},
{'latitude':11.003728	,'longitude':-74.831418},
{'latitude':11.003707	,'longitude':-74.831954},
{'latitude':11.003770	,'longitude':-74.832533},
{'latitude':11.003959	,'longitude':-74.833070},
{'latitude':11.004128	,'longitude':-74.833649},
{'latitude':11.004254	,'longitude':-74.834336},
{'latitude':11.004212	,'longitude':-74.834808},
{'latitude':11.004591	,'longitude':-74.834926},
{'latitude':11.004465	,'longitude':-74.834336},
{'latitude':11.004275	,'longitude':-74.833520},
{'latitude':11.004086	,'longitude':-74.833005},
{'latitude':11.004044	,'longitude':-74.832405},
{'latitude':11.004075	,'longitude':-74.831761},
{'latitude':11.003959	,'longitude':-74.831224},
{'latitude':11.004023	,'longitude':-74.830581},
{'latitude':11.003875	,'longitude':-74.830044},
{'latitude':11.003517	,'longitude':-74.829401},
{'latitude':11.003833	,'longitude':-74.829143},
{'latitude':11.004065	,'longitude':-74.829615},
{'latitude':11.004360	,'longitude':-74.830216},
{'latitude':11.004412	,'longitude':-74.830752},
{'latitude':11.004339	,'longitude':-74.831289},
{'latitude':11.004539	,'longitude':-74.831804},
{'latitude':11.004749	,'longitude':-74.832362},
{'latitude':11.004739	,'longitude':-74.833177},
{'latitude':11.004886	,'longitude':-74.833896},
{'latitude':11.004865	,'longitude':-74.834422},
{'latitude':11.004718	,'longitude':-74.835195},
{'latitude':11.005350	,'longitude':-74.835334}
]
	return render(request, 'elevation.html',{'syrus_data':syrus_data})

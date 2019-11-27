from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method =="POST":
		

		zipcode= request.POST['zipcode']
		api_request = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+ zipcode +"?apikey=0FOy9nMuRCDqM8VT1G52yRjJeOLnYsNV&metric=true ")
			#"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=0FOy9nMuRCDqM8VT1G52yRjJeOLnYsNV&q=Bangalore"
			#http://dataservice.accuweather.com/locations/v1/cities/search?apikey=0FOy9nMuRCDqM8VT1G52yRjJeOLnYsNV&q=Bangalore"
		try:
			api=json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html',{ 'api' : api })


	else:

		api_request = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/204108?apikey=0FOy9nMuRCDqM8VT1G52yRjJeOLnYsNV&metric=true")
		#"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=0FOy9nMuRCDqM8VT1G52yRjJeOLnYsNV&q=Bangalore"
		#http://dataservice.accuweather.com/locations/v1/cities/search?apikey=0FOy9nMuRCDqM8VT1G52yRjJeOLnYsNV&q=Bangalore"
		try:
			api=json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html',{ 'api' : api })

def about(request):
	return render(request, 'about.html',{})
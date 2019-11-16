from django.urls import include, path

urlpatterns = [
	path('', include('cbvtest.urls')),
	path('demo', include('cbvtest.urls')),
	]

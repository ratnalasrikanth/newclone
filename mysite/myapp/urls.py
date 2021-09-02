from django.urls import path
from . import views

urlpatterns = [
		path('',views.home,name="hello"),
		path('result/',views.ConvertCSVToJSON,name="result"),
]
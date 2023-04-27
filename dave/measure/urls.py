from django.urls import path, include

from .views import handleMeasureOperation

urlpatterns = [
    path('measures', handleMeasureOperation),
   
]
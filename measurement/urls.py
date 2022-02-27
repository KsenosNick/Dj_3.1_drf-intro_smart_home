from django.urls import path

from measurement.views import SensorsViewCreate, SensorViewUpdate, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorsViewCreate.as_view()),
    path('sensors/<pk>/', SensorViewUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]

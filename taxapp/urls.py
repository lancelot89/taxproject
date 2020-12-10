from django.urls import path
from .views import TaxModelUpdateView, resultfunc

urlpatterns = [
    path('calculator/<int:pk>', TaxModelUpdateView.as_view(), name='calculator'),
    path('result', resultfunc, name='result')
]

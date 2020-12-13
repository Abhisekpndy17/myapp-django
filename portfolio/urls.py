from django.urls import path
from portfolio.views import home, works


urlpatterns = [
    path('', home, name='home'),
    path('works/', works, name='works'),
]


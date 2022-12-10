from django.urls import path
from .views import home, detail


urlpatterns = [
    path("", home, name="name"),
    path("<slug:slug>/", detail, name="detail")
]
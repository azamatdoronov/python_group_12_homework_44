from django.urls import path
from bullscows.views import bullscows_view


urlpatterns = {
    path("", bullscows_view)
}

from django.urls import path
from bullscows.views import bullscows_view, steps_cache_view

urlpatterns = {
    path("", bullscows_view),
    path('steps_cache/', steps_cache_view),
}

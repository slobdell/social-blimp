from django.conf.urls import patterns, url

from .basic_navigation import views
from .basic_navigation import api

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^exercise/(?P<exercise_name>[-\w]+)/', views.exercise, name="exercise"),
    url(r'^muscle/(?P<muscle_name>[-\w]+)/', views.muscle, name="muscle"),
    url(r'^api/autocomplete/', api.autocomplete, name="autocomplete"),
    url(r'^api/verbose_autocomplete/', api.verbose_autocomplete, name="verbose_autocomplete"),
    url(r'^api/exercise/', api.exercise_from_name, name="exercise"),
    url(r'^api/exercises/', api.get_exercises, name="get_exercises"),
    url(r'^api/save/', api.save_exercise, name="save-exercise"),
)

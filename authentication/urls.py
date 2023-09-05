from django.urls import path
from . import views
urlpatterns = [
    path('login/<str:movie_name>/', views.login, name="login"),
    path('',views.home, name="home"),
    path('register/<str:movie_name>/',views.register,name="register"),
    path('Seats/<str:movie_name>/',views.Seats,name="Seats"),
    path('movie_detail/<int:movie_id>/',views.movie_detail,name="movie_detail"),
    path('set_session_data/', views.set_session_data, name='set_session_data'),
    path('report.html',views.report,name="report")
    ]	
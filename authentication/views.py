from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from authentication.models import Register,Movie3
import hashlib
import datetime

def home(request):
    movies = Movie3.objects.all()
    movie_data = [{'ID':movie.id, 'Movie_Name': movie.Movie_Name, 'URL': movie.URL,'Theatre_Name':movie.Theatre_Name,'Theatre_Location':movie.Theatre_Location,'Release_Date':movie.Release_Date} for movie in movies]  # Extract movie names
    return render(request, 'authentication/home.html', {'movie_data': movie_data})

# Create your views here.
def login(request,movie_name):
    if request.method == "POST":
        Email_id = request.POST['mail']
        pswrd = request.POST['pswrd']
        salt="5gz"
        pass1 = pswrd+salt
        hashed1 = hashlib.md5(pass1.encode())
        decrypt_pass = hashed1.hexdigest()
        register_user = Register.objects.filter(Email=Email_id, Password=decrypt_pass)
        if register_user:
            print(movie_name)
            return render(request,'authentication/Seats.html', {'selected_movie_name': movie_name})
        else:
            return render(request,'authentication/login.html',{'selected_movie_name': movie_name})
    return render(request,'authentication/login.html',{'selected_movie_name': movie_name})

def register(request,movie_name):
    if request.method=="POST":
        username = request.POST['username']
        mail = request.POST['mail_id']
        pswrd = request.POST['password']
        confirm = request.POST['confirm']
        if pswrd==confirm:
            salt = "5gz"
            dataBase_password = pswrd+salt
            hashed = hashlib.md5(dataBase_password.encode())
            crypted_pass = hashed.hexdigest()
            ins1 = Register(Username=username, Email = mail, Password = crypted_pass, Confirm_Password = crypted_pass)
            ins1.save()
            print("Data saved to db")
        else:
            print("Enter password properly")
    return render(request,'authentication/register.html',{'selected_movie_name': movie_name})

def Seats(request,movie_name):
    print(movie_name)
    return render(request,'authentication/Seats.html', {'selected_movie_name': movie_name})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie3, id=movie_id)
    selected_movie_name = movie.Movie_Name
    request.session['selected_movie_name'] = selected_movie_name
    return render(request, 'authentication/movie_detail.html', {'movie': movie})

def set_session_data(request):
    if request.method == "POST":
        movie_name = request.POST.get('movieName')
        total_amount = request.POST.get('totalAmount')
        total_seats = request.POST.get('selectedSeatsCount')
        request.session['movie_name'] = movie_name  # Store movie_name in the session
        request.session['total_amount'] = total_amount
        request.session['total_seats'] = total_seats
        return JsonResponse({'message': 'Session data set successfully'})

def report(request):
    movie_name = request.session.get('movie_name')
    print(movie_name)
    # Check if movie_name exists in the session
    return render(request, 'authentication/report.html', {'selected_movie_name': movie_name})

# def movie_list(request):
#     movies = Movie.objects.all()
#     movie_names = [movie.Movie_Name for movie in movies]  # Extract movie names
#     print(movie_names)
#     return render(request, 'authentication/home.html', {'movie_names': movie_names})
from django.shortcuts import render,redirect
from polls.models import Books
from django.contrib.auth.models  import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages



def main(request):
    if request.session['is_auth'] in (True, None):
        print("отработало")
        user = User.objects.get(id = request.session['user_id'])
    

    # user = User.objects.create_user('join','lenon@thebeatles.com','johnpassword')

    new = Books.objects.all()
    # new = Books(author = 'Leo Tolstoy', name = 'War and Peace', count_pages = '1300')
    # new.save()
    a = ["Вот""так""можно""получить""Данные из джанго"]
    return render(request, 'main.html', {'test':new, 'user':user})
# Create your views here.

def regUser(request):
    if request.method =='POST':
        data = request.POST
        user = User.objects.create_user(username = data['email'],password = data['password'])
        user.save
        return render(request,'main.html')

        # print(request.POST)
        # user = User.objects.create_user('join','lenon@thebeatles.com','johnpassword')
        # user.save
        # pass
    else:
        return render(request, 'reg.html')
    
def authUser(request):
    if request.method =='POST':
        data = request.POST
        user = authenticate(username = data['email'],password = data['password'])

        if user != None:
            request.session['is_auth']= True 
            request.session["user_id"]= user.id
            messages.add_message(request,messages.SUCCESS , 'Все правильно!')
            messages.add_message(request,messages.SUCCESS , request.session["user_id"])
        else:
            messages.add_message(request,messages.ERROR, 'Неверный email адрес или пароль')
            request.session['is_auth']= False    
    return render(request,'auth.html')

def successPage(request,id):
    if request.session['is_auth'] in (True,None):
        try:
            book = Books.objects.get(id=id)
            return render(request,'success.html',{"test":book, 'user': request.session['is_auth']})
        except:
                return HttpResponse("Такого товара нет")
    else:
        return HttpResponse("Вы авторизованы")




   

    
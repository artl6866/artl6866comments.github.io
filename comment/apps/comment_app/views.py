from django.shortcuts import render, HttpResponse, redirect
from.models import *
from django.contrib import messages
from datetime import datetime
import bcrypt
from ..app_one.models import *
from ..comment_app.models import *

def main(request):
    context = {
        'user_name' : User.objects.get(id=request.session['user_id']),
        'my_quote' : Quote.objects.filter(user_quote = request.session['user_id']),
        'other_quote' : Quote.objects.exclude(user_quote = request.session['user_id'])
        
    }

    return render(request, 'comment_app/index.html', context)

def processadd(request):
    if request.method == 'POST':
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/comment/processadd')
    
    if request.method == 'POST':
        add_user = User.objects.get(id=request.session['user_id'])
        quote = Quote.objects.create(author = request.POST['author'], quote = request.POST['quote'], user_quote = add_user)
        quote.user_like.add(add_user)
        return redirect('/comment')

    elif request.method == 'GET':
        return render(request, 'comment_app/index.html')

def show(request, id):
    user = User.objects.get(id=id)
    quote = Quote.objects.get(id=id)
    
    
    print(user.quote_created)

    context = {
        'user' : user
        
        
    }
    return render(request, 'comment_app/show.html', context)

def delete(request, id):
    user = User.objects.get(id=request.session['user_id'])
    quote = Quote.objects.get(id=id)
    quote.delete()
    return redirect('/comment')

def edit(request, id):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'id' : id,
        'fname' : User.objects.get(id=id).fname,
        'lname' : User.objects.get(id=id).lname,
        'email' : User.objects.get(id=id).email,
    }
    return render(request, 'comment_app/edit.html',context)

def updateuser(request, id):
    if request.method == 'POST':
        errors = User.objects.edit_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/comment/edit/' + str(id))
    
        user = User.objects.get(id=id)
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.email = request.POST['email']
        user.save()

    return redirect('/comment/edit/' + str(id))

def createlike(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        quote = Quote.objects.get(id=request.POST['quote_id'])
        user.quote_like.add(quote)
        quote.user_like.add(user)

        return redirect('/comment')

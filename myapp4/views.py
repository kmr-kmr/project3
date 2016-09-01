from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users, Books
from .forms import FormBooks, FormUsers
from django.contrib import messages

# Create your views here.

def books(request):
    """
    This is function based view to handle the request to the books url
    """
    if request.method = "POST":
        form = FormBooks(request.POST)
        if form.is_valid():
            # if form is valid save data to the database
            form.save()
            return HttpResponseRedirect()
	else:
            messages.error(request, 'Error')
    # if request method is get display the form
    return render(request, 'books.html', {'form': form})



def users(request):
    """
    This is a function based view to handle the request comming to the users url
    """
    if request.method = "POST"
        form = FormUsers(request.POST)
        if form.is_valid():
	    # if form is valid save data to the dtabase
	    form.save()
            # if method is post this is the response
	    return HttpResponseRedirect()
        else:
            messages.error(request, 'Error')
    else:
        form = FormUsers()
        # if get method this is the response
        return render(request, 'users.html', {'form': form})



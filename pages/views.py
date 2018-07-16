from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    data = {
    'text':'Very important text',
    'array' : [123,'abc',345,'cde']
    }
    return render(request, 'home.html', data)
    # return HttpResponse('<h1>Hello ' + str(request.user) + '!!!</h1><h2> We Love You :)</h2>')

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
    # return HttpResponse('<h1>Contact me ' + str(request.user) + ', please...</h1><h3>P.S. We Love You :)</h2>')

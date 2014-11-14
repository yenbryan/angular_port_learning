from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def angular(request):
    return render_to_response('angular.html')
from django.shortcuts import render
from portfolio.models import Portfolio



# Create your views here.
def project_index(request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio': portfolio
    }
    return render(request, 'project-index.htm', context)

 
def project_detail(request, pk):

    portfolio = Portfolio.objects.get(pk=pk)

    context = {

        'portfolio': portfolio

    }

    return render(request, 'project-detail.htm', context)

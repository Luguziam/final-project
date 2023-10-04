from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')

def service_views(request):
    return render(request, 'services.html')

def agent_views(request):
    return render(request,'agent.html' )

def transfer_views(request):
    return render(request,'transfer.html')

def account_views(request):
    return render(request,'account.html')

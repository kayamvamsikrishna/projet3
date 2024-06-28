from django.shortcuts import render

# Create your views here.
def kiss(request):
    return render(request,'kiss.html')

def love(request):
    return render(request,'love.html')
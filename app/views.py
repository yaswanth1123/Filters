from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'name':'Yash is the Handsome guy','count':5,'dt':dt}
    return render(request,'filters.html',d)

def userfilters(request):
    d={'name':'KONAPALLI Yaswanth Reddy'}
    return render(request,'userfilters.html',d)
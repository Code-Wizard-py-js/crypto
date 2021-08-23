
from axeapp.models import Sivan, Forest,Arctic,Mystic,Genesis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import Sivanserial,Forestserial,Arcticserial,Mysticserial,Genesisserial
from django.utils.timezone import localdate,now

# Create your views here.
#lands data views
def TimetoScrape(mode):
    idr=mode.objects.values_list('updated_at', flat=True).first()
    
    drdat=now()
    rk=drdat-idr
    idsr=rk.total_seconds()
    settime=(idsr % 3600) // 60
    return settime
    
@api_view(['GET'])
def SivnaView(request):
    task=Sivan.objects.all()
    serializer=Sivanserial(task,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def ForestView(request):
    task=Forest.objects.all()
    serializer=Forestserial(task,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def ArcticView(request):
    data=TimetoScrape(Arctic)
    print(data,'--------------------')
    task=Arctic.objects.all()
    serializer=Arcticserial(task,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def MysticView(request):
    task=Mystic.objects.all()
    serializer=Mysticserial(task,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GenesisView(request):
    task=Genesis.objects.all()
    serializer=Genesisserial(task,many=True)
    return Response(serializer.data)


# items Data views

# @api_view(['GET'])
# def SivnaView(request):
#     task=Test.objects.all()
#     serializer=testse(task,many=True)
#     return Response(serializer.data)
# @api_view(['GET'])
# def SivnaView(request):
#     task=Test.objects.all()
#     serializer=testse(task,many=True)
#     return Response(serializer.data)
# @api_view(['GET'])
# def SivnaView(request):
#     task=Test.objects.all()
#     serializer=testse(task,many=True)
#     return Response(serializer.data)
# @api_view(['GET'])
# def SivnaView(request):
#     task=Test.objects.all()
#     serializer=testse(task,many=True)
#     return Response(serializer.data)
# @api_view(['GET'])
# def SivnaView(request):
#     task=Test.objects.all()
#     serializer=testse(task,many=True)
#     return Response(serializer.data)
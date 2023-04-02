from django.http import JsonResponse
from .models import Fleet
from .serializers import FleetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def device_list(request, format=None):

    if request.method == 'GET':
        device=Fleet.objects.all()
        serializer = FleetSerializer(device, many=True)
        return JsonResponse({'fleet': serializer.data})

    if request.method == 'POST':
        serializer = FleetSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def device_detail(request, deviceid, format=None):

    try:
        device = Fleet.objects.get(deviceid=deviceid)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
            serializer = FleetSerializer(device)
            return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FleetSerializer(device, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

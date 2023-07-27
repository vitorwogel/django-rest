from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from base.models import Person
from .serializers import ItemSerializer
from .serializers import PersonSerializer   

#   ITEMS

@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItems(request):
    Item.objects.all().delete()
    return Response({"message":"All data cleared"})

#   PERSONS

@api_view(['GET'])
def getPersons(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePersons(request):
    Person.objects.all().delete()
    return Response({"message":"All data cleared"})
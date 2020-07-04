from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(request):

    urlpatterns = {
        'Lists' : '/task-list/',
        'Detail View' : '/task/<str:pk>/',
        'Create':'/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',

    }
    return Response(urlpatterns)

@api_view(['GET'])
def taskList(request):

    task = Task.objects.all()
    serializer = TaskSerializer(task , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDesc(request , pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task , many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
    serial = TaskSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['POST'])
def updateTask(request , pk):
    task = Task.objects.get(id =pk )
    serial = TaskSerializer(data=request.data , instance=task)
    if serial.is_valid():
        serial.save()
    return Response(serial.data)

@api_view(['DELETE'])
def deleteTask(request , pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task Deleted Successfully')
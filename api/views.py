from .models import Todo
from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializers

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
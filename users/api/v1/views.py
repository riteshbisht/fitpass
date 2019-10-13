from rest_framework.generics import  UpdateAPIView
from .serializers import UserActiveInactiveSerializer
from users.models import User

class UserActiveInactiveView(UpdateAPIView):
    serializer_class = UserActiveInactiveSerializer
    queryset = User.objects.all()
    permisssion_classes = []
    authentication_classes = []

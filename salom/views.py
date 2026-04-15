from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Helo
from .serializers import HeloSerializer


class HeloApiView(ListCreateAPIView):
    queryset = Helo.objects.all()
    serializer_class = HeloSerializer



class HeloDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Helo.objects.all()
    serializer_class = HeloSerializer
from rest_framework.serializers import ModelSerializer
from .models import Helo


class HeloSerializer(ModelSerializer):

    class Meta:
        model = Helo
        fields = '__all__'

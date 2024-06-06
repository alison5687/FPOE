from rest_framework import serializers
from api.models.hilo import Hilo
class HiloSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hilo
        fields = '__all__'

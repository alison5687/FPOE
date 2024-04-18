from rest_framework import serializers
from FPOE.Unidad1.Clase6.Backend.api.models.hilo import Hilo
class TecladoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hilo
        fields = '__all__'

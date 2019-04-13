from rest_framework import serializers
from .models import *

class loginSerializers(serializers.ModelSerializer):
    class Meta:
        model=Login
    fields='__all__'

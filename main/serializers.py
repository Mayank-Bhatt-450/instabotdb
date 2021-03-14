from rest_framework import serializers
from . import models
class insta_msg(serializers.ModelSerializer):
    class Meta:
        model=models.insta_msg
        fields=('msg',)

class replace_letters(serializers.ModelSerializer):
    class Meta:
        model=models.replace_letters
        fields=('word','options')

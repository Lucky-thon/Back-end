# board/serializers.py

from rest_framework import serializers
from .models import MissionSuccessPost

class MissionSuccessPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionSuccessPost
        fields = '__all__'  # 필요한 필드만 선택할 수 있습니다.

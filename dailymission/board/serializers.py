# board/serializers.py
from .models import RecruitmentPost
from .models import MissionSuccessPost
from rest_framework import serializers

class MissionSuccessPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionSuccessPost
        fields = '__all__'  # 필요한 필드만 선택할 수 있습니다.


class RecruitmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentPost
        fields = '__all__'  # 필요한 필드만 선택할 수 있습니다.
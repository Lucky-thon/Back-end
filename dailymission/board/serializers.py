# board/serializers.py
from .models import RecruitmentPost, RecruitmentComment
from .models import MissionSuccessPost
from rest_framework import serializers

class MissionSuccessPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionSuccessPost
        fields = '__all__'  # 필요한 필드만 선택할 수 있습니다.


class RecruitmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentPost
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.username  # 작성자의 username만 포함
        return representation

class RecruitmentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentComment
        fields = ['id', 'post', 'author', 'content', 'created_at']

    def create(self, validated_data):
        # 현재 사용자 설정
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
# board/serializers.py
from .models import RecruitmentPost, RecruitmentComment
from .models import MissionSuccessPost, UserProfile
from rest_framework import serializers

class MissionSuccessPostSerializer(serializers.ModelSerializer):

    has_posted_in_mission_success = serializers.SerializerMethodField()

    class Meta:
        model = MissionSuccessPost
        fields = ['id', 'title', 'content', 'image', 'created_at', 'author', 'has_posted_in_mission_success']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.username  # 작성자의 username만 포함
        return representation

    def get_has_posted_in_mission_success(self, obj):
        # 현재 요청한 사용자의 프로필에서 has_posted_in_mission_success 값 가져오기
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            return profile.has_posted_in_mission_success
        return False


class RecruitmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentPost
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.username  # 작성자의 username만 포함
        return representation

class RecruitmentCommentSerializer(serializers.ModelSerializer):
    writer = serializers.ReadOnlyField(source='writer.username')  # 작성자 username 포함

    class Meta:
        model = RecruitmentComment
        fields = '__all__'





from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Skill, Job, UserProfile


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description', 'category']


class JobSerializer(serializers.ModelSerializer):
    required_skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'required_skills', 'average_salary', 'difficulty']


class UserProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'id', 'username', 'full_name', 'age', 'city',
            'education_level', 'experience_years', 'skills',
            'interests', 'created_at'
        ]
from django.contrib import admin
from .models import Skill, Job, UserProfile


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'average_salary')
    list_filter = ('difficulty',)
    search_fields = ('title', 'description')
    filter_horizontal = ('required_skills',)  # pour choisir facilement les compétences


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'city', 'education_level', 'experience_years')
    list_filter = ('education_level', 'city')
    search_fields = ('full_name', 'user__username', 'interests')
    filter_horizontal = ('skills',)
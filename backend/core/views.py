from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Skill, Job, UserProfile
from .serializers import SkillSerializer, JobSerializer, UserProfileSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Liste et détail des compétences"""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    """Liste et détail des métiers"""
    queryset = Job.objects.all()
    serializer_class = JobSerializer


@api_view(['GET'])
def recommend_jobs(request):
    """
    Recommandation simple de métiers.
    Pour l'instant on retourne tous les métiers.
    Plus tard on améliorera avec le profil de l'utilisateur.
    """
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)
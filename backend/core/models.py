from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    """Compétence (ex: Python, Communication, Design UI...)"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('technique', 'Technique'),
            ('soft', 'Soft Skills'),
            ('langues', 'Langues'),
            ('outil', 'Outils'),
            ('autre', 'Autre'),
        ],
        default='technique'
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

    def __str__(self):
        return self.name


class Job(models.Model):
    """Métier / Profession"""
    title = models.CharField(max_length=150)
    description = models.TextField()
    required_skills = models.ManyToManyField(
        Skill,
        related_name='jobs',
        blank=True,
        help_text="Compétences nécessaires pour ce métier"
    )
    average_salary = models.CharField(
        max_length=100,
        blank=True,
        help_text="Ex: 150 000 - 300 000 FCFA"
    )
    difficulty = models.CharField(
        max_length=20,
        choices=[
            ('facile', 'Facile'),
            ('moyen', 'Moyen'),
            ('difficile', 'Difficile'),
        ],
        default='moyen'
    )

    class Meta:
        ordering = ['title']
        verbose_name = "Métier"
        verbose_name_plural = "Métiers"

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    """Profil de l'utilisateur (jeune qui cherche des métiers)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Informations de base
    full_name = models.CharField(max_length=150, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True, default="Lomé")
    
    # Niveau d'études
    education_level = models.CharField(
        max_length=50,
        choices=[
            ('college', 'Collège'),
            ('lycee', 'Lycée'),
            ('bts', 'BTS / DUT'),
            ('licence', 'Licence'),
            ('master', 'Master'),
            ('autre', 'Autre'),
        ],
        blank=True
    )
    
    # Expérience
    experience_years = models.PositiveIntegerField(default=0)
    
    # Compétences que l'utilisateur possède déjà
    skills = models.ManyToManyField(
        Skill,
        related_name='users',
        blank=True
    )
    
    # Centres d'intérêt (texte libre pour l'instant)
    interests = models.TextField(
        blank=True,
        help_text="Ex: technologie, business, santé, création..."
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profil utilisateur"
        verbose_name_plural = "Profils utilisateurs"

    def __str__(self):
        return f"Profil de {self.user.username}"
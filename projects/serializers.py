from rest_framework import serializers
from .models import Project, Brawler


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at', )
        read_only_fields = ('created_at',)


class BrawlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brawler
        fields = ('id', 'nombre', 'img', 'descripcion', 'rareza',
                 'clase', 'vel_mov', 'voz_actriz', 'super', 
                 'atq', 'salud_max', 'rango', 'tmp_recarga',)
        

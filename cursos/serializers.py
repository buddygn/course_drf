from rest_framework import serializers
from django.db.models import Avg

from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'curso',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
            'nome'
        )

    def validate_avaliacao(self, valor):
        if valor in (1, 6):
            return valor
        raise serializers.ValidationError('A avaliação precisa estar entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='avaliacao-detail',
    )

    # Primary Key Related Field
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    avaliacoes_quantidade = serializers.SerializerMethodField()
    avaliacoes_media = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'avaliacoes_quantidade',
            'avaliacoes_media',
        )

    def get_avaliacoes_media(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        return 0 if media is None else round(media * 2) / 2

    @staticmethod
    def get_avaliacoes_quantidade(obj):
        return obj.avaliacoes.all().count()

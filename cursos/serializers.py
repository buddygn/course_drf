from rest_framework import serializers

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
        )


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

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'avaliacoes_quantidade'
        )

    @staticmethod
    def get_avaliacoes_quantidade(obj):
        return obj.avaliacoes.all().count()

from django.urls import path

from cursos import views

urlpatterns = [
    path('cursos/', views.CursoApiView.as_view(), name='cursos'),
    path('avaliacoes/', views.AvaliacaoApiView.as_view(), name='avaliacoes'),
]

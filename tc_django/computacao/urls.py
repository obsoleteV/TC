from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'computacao'

urlpatterns = [
                path('', views.index, name='index'),
                path('index/', views.index, name='index'),
                path('automatos/', views.automatos, name='automatos'),
                path('novo_automato/', views.novo_automato, name='novo_automato'),
                path('edita_automato/<int:automato_id>/', views.edita_automato, name='edita_automato'),
                path('apaga_automato/<int:automato_id>/', views.apaga_automato, name='apaga_automato'),
                path('<int:automato_id>/automato/', views.automato, name='automato'),
                
                path('ExpressoesRegulares/', views.ExpressoesRegulares, name='ExpressoesRegulares'),

                path('NovaExpressao/', views.NovaExpressao, name='NovaExpressao'),
                path('EditarExpressao/<int:expressao_id>/', views.EditarExpressao, name='EditarExpressao'),
                path('ApagaExpressao/<int:expressao_id>/', views.ApagaExpressao, name='ApagaExpressao'),
                path('<int:expressao_id>/DetalhesExpressao/', views.DetalhesExpressao, name='DetalhesExpressao'),
                
                path('MaquinaTuring/', views.MaquinaTuring, name='MaquinaTuring'),
                path('NovaMaquina/', views.NovaMaquina, name='NovaMaquina'),
                path('EditarMaquina/<int:maquina_id>/', views.EditarMaquina, name='EditarMaquina'),
                path('ApagaMaquina/<int:maquina_id>/', views.ApagaMaquina, name='ApagaMaquina'),
                path('<int:maquina_id>/DetalhesMaquina/', views.DetalhesMaquina, name='DetalhesMaquina')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
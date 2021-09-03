from django.urls import path

from . import views

app_name = 'heroku'
urlpatterns = [
    path('', views.index, name='index'),
    path('categorias', views.CategoriasView.as_view(), name='categorias'),
    path('subCategorias', views.SubCategoriasView.as_view(), name='subCategorias'),
    path('categoria', views.CategoriaView.as_view(), name='categoria'),
    path('alteraCategoria', views.AlteraCategoriaView.as_view(), name='alteraCategoria'),
    path('apagaCategoria', views.ApagaCategoriaView.as_view(), name='apagaCategoria'),
    path('buscaCategoriaPorNome', views.CategoriaPorNomeView.as_view(), name='buscaCategoriaPorNome'),
    path('novaCategoria', views.insereCategoriaView.as_view(), name='novaCategoria'),
    path('subCategoria', views.SubCategoriaView.as_view(), name='subCategoria'),
    path('alteraSubCategoria', views.AlteraSubCategoriaView.as_view(), name='alteraSubCategoria'),
    path('novaSubCategoria', views.insereSubCategoriaView.as_view(), name='novaSubCategoria'),
    path('teste/<int:id>/<str:nome>', views.checaSubcat, name='teste'),
    path('apagaSubCategoria', views.ApagaSubCategoriaView.as_view(), name='apagaSubCategoria'),
    path('itens', views.ItensView.as_view(), name='itens'),
    path('alteraItem', views.AlteraItemView.as_view(), name='alteraItem'),
    path('checaExisteTitulo', views.checaExisteTitulo, name='checaExisteTitulo'),
    path('insereItem', views.InsereItemView.as_view(), name='insereItem'),
    path('apagaItem', views.ApagaItemView.as_view(), name='apagaItem'),
]
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import filters, generics
from .models import HkCategorias, HkCategoriasSerializer, HkSubcategorias, HkSubcategoriasSerializer
from .models import HkItem, HkItemSerializer

from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return HttpResponse("Alô Mundo!. Este é o index de Heroku!.")

class CategoriasView(generics.ListCreateAPIView):
    model = HkCategorias
    serializer_class = HkCategoriasSerializer

    def get_queryset(self):
        queryset =HkCategorias.objects.all().order_by('nome')
        return queryset

class SubCategoriasView(generics.ListCreateAPIView):
    model = HkSubcategorias
    serializer_class = HkSubcategoriasSerializer

    @csrf_exempt
    def get_queryset(self):
        queryset =HkSubcategorias.objects.all().order_by('nome')
        if self.request.GET.keys():
            idCategoria = self.request.GET['idCategoria']
            queryset = HkSubcategorias.objects.filter(id_categoria=idCategoria).order_by('nome')
        return queryset

class CategoriaView(generics.GenericAPIView):
    model = HkCategorias
    serializer_class = HkCategoriasSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        retorno = json.dumps(serializer.data)
        jsonData = json.loads(retorno)
        retorno = json.dumps(jsonData[0])
        return HttpResponse(retorno)
    def get_queryset(self):
        idCategoria = self.request.query_params.get('id')
        id = int(idCategoria)
        queryset = HkCategorias.objects.filter(id=id)
        return queryset

class AlteraCategoriaView(generics.GenericAPIView):
    model = HkCategorias
    serializer_class = HkCategoriasSerializer

    def get(self, request, *args, **kwargs):
        self.get_queryset()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)
    def get_queryset(self):
        idCategoria = self.request.query_params.get('id')
        nomeCategoria = self.request.query_params.get('nome')
        id = int(idCategoria)
        queryset = HkCategorias.objects.filter(id=id).update(nome = nomeCategoria)
        return queryset

class ApagaCategoriaView(generics.GenericAPIView):
    model = HkCategorias
    serializer_class = HkCategoriasSerializer

    def get(self, request, *args, **kwargs):
        if not ('id' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o id como parâmetro"}')
        idCategoria = request.query_params.get('id')
        id = int(idCategoria)
        queryset = HkSubcategorias.objects.filter(id_categoria=id)
        serializer = HkSubcategoriasSerializer(queryset, many=True)
        retorno = json.dumps(serializer.data)
        data = serializer.data
        if data != '[]':
            strJson = json.dumps(data)
            dataJson = json.loads(strJson)
            n = len(dataJson)
            if n > 0:
                msg = 'Não é possível apagar a categoria, pois existem ' + str(n) + ' subcategorias nela'
                return HttpResponse('{"retorno":"nOk","msg":"' + msg + '"}')
        self.get_queryset()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)
    def get_queryset(self):
        idCategoria = self.request.query_params.get('id')
        id = int(idCategoria)
        queryset = HkCategorias.objects.filter(id=id).delete()
        return queryset

class CategoriaPorNomeView(generics.GenericAPIView):
    model = HkCategorias
    serializer_class = HkCategoriasSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        if not ('nome' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o nome como parâmetro"}')
        retorno = json.dumps(serializer.data)
        if (retorno == '[]'):
            return HttpResponse('{"retorno":"Ok","msg":""}')
        else:
            return HttpResponse('{"retorno":"nOk","msg":"Categoria já existe"}')
        jsonData = json.loads(retorno)
        retorno = json.dumps(jsonData[0])
        return HttpResponse(retorno)
    def get_queryset(self):
        if not ('nome' in self.request.query_params):
            return HkCategorias.objects.filter(id=0)
        nomeCategoria = self.request.query_params.get('nome')
        queryset = HkCategorias.objects.filter(nome=nomeCategoria)
        return queryset

class insereCategoriaView(generics.GenericAPIView):
    model = HkCategorias
    serializer_class = HkCategoriasSerializer

    def get(self, request, *args, **kwargs):
        if not ('nome' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o nome como parâmetro"}')
        nome = request.query_params.get('nome')
        categoria = HkCategorias(nome=nome)
        categoria.save()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)

class SubCategoriaView(generics.GenericAPIView):
    model = HkSubcategorias
    serializer_class = HkSubcategoriasSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        retorno = json.dumps(serializer.data)
        jsonData = json.loads(retorno)
        retorno = json.dumps(jsonData[0])
        return HttpResponse(retorno)
    def get_queryset(self):
        idSubCategoria = self.request.query_params.get('id')
        id = int(idSubCategoria)
        queryset = HkSubcategorias.objects.filter(id=id)
        return queryset

class SubCategoriaView(generics.GenericAPIView):
    model = HkSubcategorias
    serializer_class = HkSubcategoriasSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        retorno = json.dumps(serializer.data)
        jsonData = json.loads(retorno)
        retorno = json.dumps(jsonData[0])
        return HttpResponse(retorno)
    def get_queryset(self):
        idSubCategoria = self.request.query_params.get('id')
        id = int(idSubCategoria)
        queryset = HkSubcategorias.objects.filter(id=id)
        return queryset

class AlteraSubCategoriaView(generics.GenericAPIView):
    model = HkSubcategorias
    serializer_class = HkSubcategoriasSerializer

    def get(self, request, *args, **kwargs):
        self.get_queryset()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)
    def get_queryset(self):
        idSubCategoria = self.request.query_params.get('id')
        nomeSubCategoria = self.request.query_params.get('nome')
        id = int(idSubCategoria)
        queryset = HkSubcategorias.objects.filter(id=id).update(nome = nomeSubCategoria)
        return queryset

class SubCategoriaPorNomeView(generics.GenericAPIView):
    model = HkSubcategorias
    serializer_class = HkSubcategoriasSerializer
    localId = 0
    _localNome = 'inicial'

    @property
    def localNome(self):
        if self._localNome:
           return self._localNome
        return 'Nada'

    @localNome.setter
    def localNome(self, value):
        self._localNome = value

    def setLK(self,parm):
        self.localNome = parm

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        passado = self.localNome

        if not ('nome' in request.query_params):
            if (passado == 'inicial'):
                return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o nome como parâmetro"}')
        retorno = json.dumps(serializer.data)
        if (retorno == '[]'):
            return HttpResponse('{"retorno":"Ok","msg":""}')
        else:
            return HttpResponse('{"retorno":"nOk","msg":"Sub-ategoria já existe"}')
        jsonData = json.loads(retorno)
        retorno = json.dumps(jsonData[0])
        return HttpResponse(retorno)
    def get_queryset(self):
        strData = json.dumps(self.request.query_params)
        jsData = json.loads(strData)
        nomeSubCategoria = jsData['nome']
        queryset = HkSubcategorias.objects.filter(nome=nomeSubCategoria)
        return queryset

class insereSubCategoriaView(generics.GenericAPIView):
    model = HkSubcategorias
    serializer_class = HkSubcategoriasSerializer

    def get(self, request, *args, **kwargs):
        if not ('nome' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o nome como parâmetro"}')
        if not ('id' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o id da categoria"}')
        nome = request.query_params.get('nome')
        strId = request.query_params.get('id')
        id = int(strId)
        retorno = checaSubcat(request, nome, id)
        data = json.loads(retorno.content)
        resultado = data['retorno']
        if resultado != 'Ok':
            msg = json.dumps(data)
            return HttpResponse(msg)
        subcategoria = HkSubcategorias(id_categoria=id, nome=nome)
        subcategoria.save()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)

def checaSubcat(request, nome, id):
    model = HkSubcategorias
    serializer_class = HkSubcategoriasSerializer
    queryset = HkSubcategorias.objects.filter(nome=nome, id_categoria=id)
    serializer = HkSubcategoriasSerializer(queryset, many=True)
    retorno = json.dumps(serializer.data)
    data = serializer.data
    if data == '[]':
        return HttpResponse('{"retorno":"Ok","msg":""}')
    strJson = json.dumps(data)
    dataJson = json.loads(strJson)
    n = len(dataJson)
    if n == 0:
        return HttpResponse('{"retorno":"Ok","msg":""}')
    strJson = dataJson[0]
    return HttpResponse('{"retorno":"nOk","msg":"Sub categoria já existe"}')

class ApagaSubCategoriaView(generics.GenericAPIView):
    model = HkSubcategorias
    serializer_class = HkSubcategoriasSerializer

    def get(self, request, *args, **kwargs):
        if not ('id' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o id da sub-categoria"}')
        idSubCategoria = request.query_params.get('id')
        id = int(idSubCategoria)
        queryset = HkItem.objects.filter(id_subcategoria=id)
        serializer = HkItemSerializer(queryset, many=True)
        retorno = json.dumps(serializer.data)
        data = serializer.data
        print('data:')
        print (data)
        if data != '[]':
            strJson = json.dumps(data)
            dataJson = json.loads(strJson)
            n = len(dataJson)
            if n > 0:
                msg = 'Não é possível apagar a sub-categoria, pois existem ' + str(n) + ' itens nela'
                return HttpResponse('{"retorno":"nOk","msg":"' + msg + '"}')
        self.get_queryset()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)
    def get_queryset(self):
        idSubCategoria = self.request.query_params.get('id')
        id = int(idSubCategoria)
        queryset = HkSubcategorias.objects.filter(id=id).delete()
        return queryset

class ItensView(generics.ListCreateAPIView):
    model = HkItem
    serializer_class = HkItemSerializer

    def get_queryset(self):
        queryset =HkItem.objects.all().order_by('titulo')
        return queryset

class AlteraItemView(generics.GenericAPIView):
    model = HkItem
    serializer_class = HkItemSerializer

    def get(self, request, *args, **kwargs):
        if not ('id' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o id da sub-categoria"}')
        self.get_queryset()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)
    
    def get_queryset(self):
        idItem = self.request.query_params.get('id')
        titulo = self.request.query_params.get('titulo')
        texto = self.request.query_params.get('texto')
        codCat = self.request.query_params.get('codCat')
        codSub = self.request.query_params.get('codSub')
        id = int(idItem)
        queryset = HkItem.objects.filter(id=id).update(titulo = titulo, texto = texto, id_categoria = codCat, id_subcategoria = codSub)
        return queryset

def checaExisteTitulo(request):
    model = HkItem
    serializer_class = HkItemSerializer

    if not ('titulo' in request.GET):
        return HttpResponse('{"retorno":"nOk","msg":"Informe o título"}')
    titulo = request.GET['titulo']
    queryset = HkItem.objects.filter(titulo=titulo)
    serializer = HkItemSerializer(queryset, many=True)
    data = serializer.data
    if data == '[]':
        return HttpResponse('{"retorno":"Ok","msg":""}')
    strJson = json.dumps(data)
    dataJson = json.loads(strJson)
    n = len(dataJson)
    if n == 0:
        return HttpResponse('{"retorno":"Ok","msg":""}')
    return HttpResponse('{"retorno":"nOk","msg":"Já existe este título"}')

class InsereItemView(generics.GenericAPIView):
    model = HkItem
    serializer_class = HkItemSerializer

    def get(self, request, *args, **kwargs):
        if not ('titulo' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve informar o título como parâmetro"}')
        if not ('idCategoria' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"idCategoria não informado"}')
        if not ('idSubCategoria' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"idSubCategoria não informado"}')
        texto = ''
        if 'texto' in request.query_params:
            texto = request.query_params.get('texto')
        titulo = request.query_params.get('titulo')
        idCategoria = request.query_params.get('idCategoria')
        idSubCategoria = request.query_params.get('idSubCategoria')
        retorno = checaExisteTitulo(request)
        data = json.loads(retorno.content)
        resultado = data['retorno']
        if resultado != 'Ok':
            msg = json.dumps(data)
            return HttpResponse(msg)
        idCat = int(idCategoria)
        idSub = int(idSubCategoria)
        item = HkItem(id_categoria=idCat, id_subcategoria=idSub, titulo=titulo, texto=texto)
        item.save()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)

class ApagaItemView(generics.GenericAPIView):
    model = HkItem
    serializer_class = HkItemSerializer

    def get(self, request, *args, **kwargs):
        if not ('id' in request.query_params):
            return HttpResponse('{"retorno":"nOk","msg":"Você deve passar o id do ítem"}')
        self.get_queryset()
        data = '{"retorno":"Ok"}'
        return HttpResponse(data)
    def get_queryset(self):
        idItem = self.request.query_params.get('id')
        id = int(idItem)
        queryset = HkItem.objects.filter(id=id).delete()
        return queryset
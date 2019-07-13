from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import BbForm

from .models import Bb

from .models import Rubric

from .serializers import RubricSerializer

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}  
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

@api_view(['GET'])
def api_rubrics(request):
    if request.method == 'GET':
        rubrics = Rubric.objects.all()
        serializer = RubricSerializer(rubrics, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_rubric_detail(request, pk):
    if request.method == 'GET':
        rubric = Rubric.objects.get(pk=pk)
        serializer = RubricSerializer(rubric)
        return Response(serializer.data)
    

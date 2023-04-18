from django.views.generic.base import TemplateView
from core.models import GPUSpecs
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.utils import translation
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data['data'] = GPUSpecs.objects.order_by('-performance')
        context_data['other_data'] = list(context_data['data'].values('id', 'performance'))
        context_data['obj'] = GPUSpecs.objects.get(performance=100)
        return context_data


class CompareView(TemplateView):
    template_name = 'compare.html'

    def get_context_data(self, **kwargs):
        lang = self.request.LANGUAGE_CODE
        context_data = super(CompareView, self).get_context_data(**kwargs)
        context_data['data'] = GPUSpecs.objects.order_by('-performance')
        # context_data['data'] = GPUSpecs.objects.order_by('-performance').values('name', 'performance', 'price', 'year')
        q = Q()
        for d in [kwargs.get('c_val_1', ''), kwargs.get('c_val_2', '')]:
            q |= Q(name__icontains=d.replace('-', ' '))
        objs = GPUSpecs.objects.filter(q)
        for idx, obj in enumerate(objs):
            context_data[f'obj_{idx}'] = obj
            context_data[f'obj_{idx}_benchmark_performance'] = obj.benchmark_performance(lang)
        return context_data


class DetailView(TemplateView):
    template_name = 'info.html'

    def get_context_data(self, **kwargs):
        lang = self.request.LANGUAGE_CODE
        context_data = super(DetailView, self).get_context_data(**kwargs)
        context_data['data'] = GPUSpecs.objects.order_by('-performance')
        context_data['obj'] = GPUSpecs.objects.filter(name__iexact=kwargs.get('selected', '').replace('-', ' ').lower()).first()
        context_data[f'benchmark_performance'] = context_data['obj'].benchmark_performance(lang)
        return context_data
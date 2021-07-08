from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from chemistry.forms import SolventForm, ReagentForm, ReactionForm
from chemistry.models import Producer, Reagent, Reaction, Solvent


class IndexView(View):
    def get(self, request):
        message = request.GET.get('message', '')
        return render(request, 'base.html', {'message': message})


class AddSolvent(LoginRequiredMixin, View):
    def get(self, request):
        form = SolventForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = SolventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Solvent added')


class AddReagent(LoginRequiredMixin, View):
    def get(self, request):
        form = ReagentForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = ReagentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Reagent added')


class AddReaction(LoginRequiredMixin, View):
    def get(self, request):
        form = ReactionForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = ReactionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Reaction added')


class ProducerList(View):
    def get(self, request):
        producers = Producer.objects.all()
        return render(request, 'producer_list.html', {'producers': producers})


class ListReagentView(ListView):
    model = Reagent
    fields = ['reagent_name', 'producer', 'physical_state', 'comment']
    template_name = 'list_view.html'


class ListReactionView(ListView):
    model = Reaction
    fields = ['reaction_number', 'user', 'description', 'comment']
    template_name = 'list_view.html'


class ListSolventView(ListView):
    model = Solvent
    fields = ['solvent_name', 'producer', 'comment']
    template_name = 'list_view.html'


class UpdateSolventView(UpdateView):
    model = Solvent
    fields = '__all__'
    template_name = 'form.html'


class UpdateReactionView(UpdateView):
    model = Reaction
    fields = '__all__'
    template_name = 'form.html'


class UpdateReagentView(UpdateView):
    model = Reagent
    fields = '__all__'
    template_name = 'form.html'


class ProducerDelete(DeleteView):
    model = Producer
    success_url = '/producer_list'


class ReagentDelete(DeleteView):
    model = Reagent
    success_url = '/reagent_list'


class SolventDelete(DeleteView):
    model = Solvent
    success_url = '/solvent_list'


class ReactionDelete(DeleteView):
    model = Reaction
    success_url = '/reaction_list'



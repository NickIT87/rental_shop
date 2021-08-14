from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Apartment, ApartmentGallery


# Create your views here.
_TRANSLITERATE = {
    'sale' : 'продажа',
    'rental' : 'аренда',
    'exchange' : 'обмен'
}


class HomePageView(TemplateView):
    template_name = "agency/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home"
        return context


class ApartmentsView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Квартиры."
        return context

    def get_queryset(self):
        return Apartment.objects.all()


class ApartmentsProposalTypeView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = "Квартиры, {}.".format(_TRANSLITERATE[self.kwargs['proposal_type']])
        except:
            raise Http404
        return context

    def get_queryset(self):
        return Apartment.objects.filter(proposal_type=self.kwargs['proposal_type'])


class ApartmentsProposalTypeByRoomsNumber(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 3
    #allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if self.kwargs['rooms_count'] > 0 and self.kwargs['rooms_count'] <= 3:
                context['title'] = "Квартиры, {}, комнат: {}.".format(
                    _TRANSLITERATE[self.kwargs['proposal_type']],
                    self.kwargs['rooms_count']
                )
            else:
                context['title'] = "Квартиры, {}, комнат: 4+".format(_TRANSLITERATE[self.kwargs['proposal_type']])
        except:
            raise Http404
        return context

    def get_queryset(self):
        if self.kwargs['rooms_count'] > 0 and self.kwargs['rooms_count'] <= 3:
            return Apartment.objects.filter(proposal_type=self.kwargs['proposal_type'], number_of_rooms=self.kwargs['rooms_count'])
        elif self.kwargs['rooms_count'] == 4:
            return Apartment.objects.filter(proposal_type=self.kwargs['proposal_type'], number_of_rooms__gt=3)
        else:
            raise Http404


class ApartmentView(DetailView):
    model = Apartment
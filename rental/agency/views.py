from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.db.models import Q

from .models import Apartment, House, Settlement, CommercialStructure, Garage, LandPlot, Advertising


# Create your views here.
_TRANSLITERATE = {
    'sale' : 'продажа',
    'rental' : 'аренда',
    'exchange' : 'обмен'
}


# MAIN PAGE VIEW
class HomePageView(TemplateView):
    template_name = "agency/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home"
        return context


# APARTMENTS VIEWS
class ApartmentsView(ListView):
    model = Apartment
    template_name = "agency/apartments.html"
    context_object_name = 'flats'
    paginate_by = 6

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
    paginate_by = 6

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
    paginate_by = 6
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


# HOUSES VIEWS
class HousesView(ListView):
    model = House
    template_name = 'agency/houses.html'
    context_object_name = 'houses'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Дома."
        return context

    def get_queryset(self):
        return House.objects.all()


class HousesProposalTypeView(ListView):
    model = House
    template_name = 'agency/houses.html'
    context_object_name = 'houses'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = "Дома, {}.".format(_TRANSLITERATE[self.kwargs['proposal_type']])
        except:
            raise Http404
        return context

    def get_queryset(self):
        return House.objects.filter(proposal_type=self.kwargs['proposal_type'])


class HousesProposalTypeBySettlementView(ListView):
    model = House
    template_name = 'agency/houses.html'
    context_object_name = 'houses'
    paginate_by = 6
    #allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = "Дома, {}, {}.".format(
                _TRANSLITERATE[self.kwargs['proposal_type']],
                Settlement.objects.get(pk=self.kwargs['settlement_id'])
            )
        except:
            raise Http404
        return context

    def get_queryset(self):
        return House.objects.filter(
            proposal_type=self.kwargs['proposal_type'],
            settlement_id=self.kwargs['settlement_id'],
        ).select_related('settlement')


class HouseView(DetailView):
    model = House


# COMMERCIAL STRUCTURES VIEWS
class CommercialStructsView(ListView):
    model = CommercialStructure
    template_name = 'agency/commercialStructures.html'
    context_object_name = 'commstructs'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Коммерческая недвижимость"
        return context

    def get_queryset(self):
        return CommercialStructure.objects.all()


class CommStructsPropTypeView(ListView):
    model = CommercialStructure
    template_name = 'agency/commercialStructures.html'
    context_object_name = 'commstructs'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = "Коммерческая недвижимость, {}.".format(_TRANSLITERATE[self.kwargs['proposal_type']])
        except:
            raise Http404
        return context

    def get_queryset(self):
        return CommercialStructure.objects.filter(proposal_type=self.kwargs['proposal_type'])


class CommercialStructureView(DetailView):
    model = CommercialStructure


# GARAGES VIEWS
class GaragesView(ListView):
    model = Garage
    template_name = 'agency/garages.html'
    context_object_name = 'garages'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Гаражи"
        return context

    def get_queryset(self):
        return Garage.objects.all()


class GaragesPropTypeView(ListView):
    model = Garage
    template_name = 'agency/garages.html'
    context_object_name = 'garages'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = "Гаражи, {}.".format(_TRANSLITERATE[self.kwargs['proposal_type']])
        except:
            raise Http404
        return context

    def get_queryset(self):
        return Garage.objects.filter(proposal_type=self.kwargs['proposal_type'])


class GarageView(DetailView):
    model = Garage


# LANDPLOTS VIEWS
class LandPlotsView(ListView):
    model = LandPlot
    template_name = 'agency/landplots.html'
    context_object_name = 'landplots'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Земельные участки"
        return context

    def get_queryset(self):
        return LandPlot.objects.all()


class LandPlotsPropTypeView(ListView):
    model = LandPlot
    template_name = 'agency/landplots.html'
    context_object_name = 'landplots'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['title'] = "Участки, {}.".format(_TRANSLITERATE[self.kwargs['proposal_type']])
        except:
            raise Http404
        return context

    def get_queryset(self):
        return LandPlot.objects.filter(proposal_type=self.kwargs['proposal_type'])


class LandPlotView(DetailView):
    model = LandPlot


class FindFormView(TemplateView):
    template_name = 'agency/searchForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Поиск объекта"
        context['settlements'] = Settlement.objects.all()
        context['promos'] = Advertising.objects.all()
        if len(context['promos']) > 1:
            context['option'] = 'true'
        else:
            context['option'] = 'false'
        return context


class Search(ListView):
    template_name = 'agency/searchResult.html'
    context_object_name = 'found_obj'

    def get_queryset(self):
        if self.request.GET.get('s') == None or self.request.GET.get('select_obj_type') == None:
            raise Http404
        # request variables
        obj_type = self.request.GET.get('select_obj_type')
        prop_type = self.request.GET.get('select_proposal_type')
        flat_cnt = int(self.request.GET.get('select_flat_room_count'))
        stlmnt = self.request.GET.get('select_settlement')
        p1 = self.request.GET.get('p1')
        p2 = self.request.GET.get('p2')
        s = self.request.GET.get('s')
        # Apartments search logic
        if obj_type == 'Apartment':
            if flat_cnt > 0 and len(s) > 0:
                if flat_cnt == 4:
                    return Apartment.objects.filter(proposal_type=prop_type, price__range=(p1, p2),
                                                    number_of_rooms__gt=3, address__icontains=s)
                else:
                    return Apartment.objects.filter(proposal_type=prop_type, price__range=(p1, p2),
                                                    number_of_rooms=flat_cnt, address__icontains0=s)
            elif flat_cnt == 0 and len(s) > 0:
                return Apartment.objects.filter(proposal_type=prop_type, price__range=(p1, p2), address__icontains=s)
            elif flat_cnt > 0 and len(s) == 0:
                if flat_cnt == 4:
                    return Apartment.objects.filter(proposal_type=prop_type, price__range=(p1, p2),
                                                    number_of_rooms__gt=3)
                else:
                    return Apartment.objects.filter(proposal_type=prop_type, price__range=(p1, p2),
                                                    number_of_rooms=flat_cnt)
            else:
                return Apartment.objects.filter(proposal_type=prop_type, price__range=(p1, p2))
        elif obj_type == 'House':
            if len(s) > 0:
                return House.objects.filter(proposal_type=prop_type, price__range=(p1, p2),
                                            address__icontains=s, settlement__title__contains=stlmnt
                )
            else:
                return House.objects.filter(proposal_type=prop_type, price__range=(p1, p2),
                                            settlement__title__contains=stlmnt
                )
        else:
            # default return never execute
            return False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['s'] = f"{self.request.GET.get('s')}"
        context['title'] = "search"
        return context
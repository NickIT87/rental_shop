from django import template
from django.core.cache import cache

from agency.models import Garage


register = template.Library()


@register.inclusion_tag('agency/garagesSidebarTmpl.html')
def count_garages():
    garagesBySale = len(Garage.objects.filter(proposal_type='sale'))
    garagesByExchange = len(Garage.objects.filter(proposal_type='exchange'))
    garagesByRental = len(Garage.objects.filter(proposal_type='rental'))

    return {
        "garagesBySale": garagesBySale,
        "garagesByExchange": garagesByExchange,
        "garagesByRental": garagesByRental,
    }
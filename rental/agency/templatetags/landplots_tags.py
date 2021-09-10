from django import template
from django.core.cache import cache

from agency.models import LandPlot


register = template.Library()


@register.inclusion_tag('agency/landsSidebarTmpl.html')
def count_lands():
    landsBySale = len(LandPlot.objects.filter(proposal_type='sale'))
    landsByExchange = len(LandPlot.objects.filter(proposal_type='exchange'))
    landsByRental = len(LandPlot.objects.filter(proposal_type='rental'))

    return {
        "landsBySale": landsBySale,
        "landsByExchange": landsByExchange,
        "landsByRental": landsByRental,
    }
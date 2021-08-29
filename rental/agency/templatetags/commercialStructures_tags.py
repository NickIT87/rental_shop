from django import template
from django.core.cache import cache

from agency.models import CommercialStructure


register = template.Library()


@register.inclusion_tag('agency/commStructSidebarTmpl.html')
def count_structures():
    structsBySale = len(CommercialStructure.objects.filter(proposal_type='sale'))
    structsByExchange = len(CommercialStructure.objects.filter(proposal_type='exchange'))
    structsByRental = len(CommercialStructure.objects.filter(proposal_type='rental'))

    return {
        "structsBySale": structsBySale,
        "structsByExchange": structsByExchange,
        "structsByRental": structsByRental,
    }
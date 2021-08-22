from django import template
from django.db.models import Count, F
from django.core.cache import cache

from agency.models import Settlement


register = template.Library()


@register.inclusion_tag('agency/list_settlements.html')
def show_settlements():

    settlementsBySale = Settlement.objects.filter(house__proposal_type__contains='sale').annotate(
        cnt=Count('house')).filter(cnt__gt=0)
    settlementsByRental = Settlement.objects.filter(house__proposal_type__contains='rental').annotate(
        cnt=Count('house')).filter(cnt__gt=0)
    settlementsByExchange = Settlement.objects.filter(house__proposal_type__contains='exchange').annotate(
        cnt=Count('house')).filter(cnt__gt=0)

    #settlements = Settlement.objects.annotate(cnt=Count('house')).filter(cnt__gt=0)
    # categories = cache.get('categories')
    # if not categories:
    #     categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    #     cache.set('categories', categories, 30)

    return {
        "settlementsSale":settlementsBySale,
        "settlementsRental": settlementsByRental,
        "settlementsExchange": settlementsByExchange,
    }
from django.urls import path

from .views import *


urlpatterns = [
    # main page
    path('', HomePageView.as_view(), name='home'),
    # apartments
    path('apartments/', ApartmentsView.as_view(), name='apartments'),
    path('apartments/<str:proposal_type>/', ApartmentsProposalTypeView.as_view(), name='apartmentsProposalType'),
    path('apartments/<str:proposal_type>/<int:rooms_count>/', ApartmentsProposalTypeByRoomsNumber.as_view(),
         name='apartmentsProposalTypeByRoomsNumber'),
    path('apartment/<int:pk>/', ApartmentView.as_view(), name='apartment'),
    # houses
    path('houses/', HousesView.as_view(), name='houses'),
    path('houses/<str:proposal_type>/', HousesProposalTypeView.as_view(), name='housesProposalType'),
    path('houses/<str:proposal_type>/<int:settlement_id>', HousesProposalTypeBySettlementView.as_view(),
         name='housesProposalTypeBySettlement'),
    path('house/<int:pk>/', HouseView.as_view(), name='house'),
]
from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('apartments/', ApartmentsView.as_view(), name='apartments'),
    path('apartments/<str:proposal_type>/', ApartmentsProposalTypeView.as_view(), name='apartmentsProposalType'),
    path('apartments/<str:proposal_type>/<int:rooms_count>/', ApartmentsProposalTypeByRoomsNumber.as_view(),
         name='apartmentsProposalTypeByRoomsNumber'),
    path('apartment/<int:pk>/', ApartmentView.as_view(), name='apartment'),
    path('houses/', HousesView.as_view(), name='houses'),
]
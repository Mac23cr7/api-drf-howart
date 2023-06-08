from django.urls import path 
#from apps.apiSolicitud.views import SchoolApiView
from apps.apiSolicitud.views import school_api_view, school_api_detail, request_api_view, request_api_detail

urlpatterns = [
    #path('school/', SchoolApiView.as_view(), name = 'school_api')

    path('school/', school_api_view, name = 'school_api'),
    path('school/<int:pk>', school_api_detail, name = 'school_api_detail'),

    #
    path('request/', request_api_view, name = 'request_api'),
    path('request/<int:pk>', request_api_detail, name = 'request_api_detail')
]
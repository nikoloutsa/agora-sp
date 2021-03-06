from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'^service_details_option/edit/?$', views.edit_service_details_option),
    url(r'^service_details_option/add/?$', views.insert_service_details_option),
    url(r'^service_option/edit/?$', views.edit_service_option),
    url(r'^service_option/add/?$', views.insert_service_option),
    url(r'^parameter/edit/?$', views.edit_parameter),
    url(r'^parameter/add/?$', views.insert_parameter),
    url(r'^SLA_paramters/edit/?$', views.edit_SLA_parameter),
    url(r'^SLA_paramters/add/?$', views.insert_SLA_parameter),
    url(r'^SLAs/edit/?$', views.edit_SLA),
    url(r'^SLAs/add/?$', views.insert_SLA),
    url(r'^service_options/all/?$', views.get_service_options_all),
    url(r'^parameter/all/?$', views.get_parameter_all),
    url(r'^sla/all/?$', views.get_sla_all),
    url(r'^service_options/(?P<serv_opt_uuid>[0-9a-zA-Z\-]+)/?$', views.get_service_options_single),
    url(r'^service_options_sla/(?P<serv_opt_uuid>[0-9a-zA-Z\-]+)/?$', views.get_service_options_with_sla),
    url(r'^sla/(?P<sla_uuid>[0-9a-zA-Z\-]+)/?$', views.get_sla),
    url(r'^parameter/(?P<param_uuid>[0-9a-zA-Z\-]+)/?$', views.get_parameter),
    url(r'^sla_parameter/(?P<sla_param_uuid>[0-9a-zA-Z\-]+)/?$', views.get_sla_parameter),
    url(r'^service_details_options/(?P<serv_det_option_uuid>[0-9a-zA-Z\-]+)/?$', views.get_service_details_options),
    url(r'^options_for_service_details/(?P<version>[0-9a-zA-Z\-]+)/?$', views.get_options_for_service_details),
    url(r'^parameters_for_sla/(?P<sla>[0-9a-zA-Z\-]+)/?$', views.get_parameters_for_sla)
]
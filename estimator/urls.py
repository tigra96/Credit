from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.estimator_list, name='estimator_list'),
	url(r'^result/$', views.estimate_result, name='estimate_result'),
	url(r'^sorry/$', views.estimate_bad_result, name='estimate_bad_result'),
	url(r'^enter/$', views.post_new, name='post_new'),
	url(r'^credit_history/$', views.estimate_credit_history, name='credit_history'),
	url(r'^model_info/$', views.estimate_model_info, name='model_info'),
	url(r'^bad_answer/$', views.estimate_bad_answer, name='estimate_bad_answer'),
	url(r'^login/$', views.estimate_login, name='login'),
	url(r'^administrator/$', views.estimate_admin, name='estimate_admin'),
]
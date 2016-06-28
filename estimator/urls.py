from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.estimator_list, name='estimator_list'),
	url(r'^result/$', views.estimate_result, name='estimate_result'),
	url(r'^sorry/$', views.estimate_bad_result, name='estimate_bad_result'),
	url(r'^enter/$', views.post_new, name='post_new'),
]
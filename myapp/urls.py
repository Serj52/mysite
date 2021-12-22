from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'home/$', views.home, name='home'),
    url(r'\w{1,}/search.html', views.search, name='search'),
    url(r'contacts/$', views.contacts, name='cotacts'),
    url(r'home/fest.html/$', views.fest, name='fest'),
    url(r'home/fest.html/base_film.html/$', views.film, name='film'),


]
from django.conf import settings
from django.conf.urls import url
from django.urls import path, include

from welcome import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^health$', views.health),
    path('grocery/', include('welcome.urls'))
]  # point the root urls.py -> the welcome urls.py module
# include() allows referencing of other url config files (urls.py)

# path(route, view, name)
#  - route: a URL pattern, searches from TOP -> BOTTOM;
#  - view: the view called when Django finds a matching pattern, sends a HttpRequest object as argument
#  - name: allows you to unambiguously name the URL to refer to it from within templates
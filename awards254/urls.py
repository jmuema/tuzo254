from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^register',views.register, name='register'),
    url(r'^feed',views.feed, name='feed'),
    url(r'^review/(\d+)', views.review, name = 'review'),
    url(r'^profile/(\d+)',views.profile, name='profile'),
    url(r'^post/', views.post, name='post'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
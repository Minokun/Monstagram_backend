from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^resource_list/', views.ResourceList.as_view()),
    url(r'^user_detail/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
    url(r'^user_list/',views.User.as_view()),
    url(r'^comment_list/',views.CommentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from BBlog.models import  Post
from django.conf.urls.i18n import urlpatterns
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                           template_name="BBlog/BBlog.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
                                                         template_name = 'BBlog/post.html'))]

from django.views.generic import ListView
from models import *


class ListNews(ListView):
    model = News
    template_name_suffix = "_list_all"

    def get_context_data(self, **kwargs):
        data = super(ListNews, self).get_context_data(**kwargs)
        data['header_news'] = News.objects.all()[5:9]
        data['news_list'] = News.objects.all()[:5]
        return data

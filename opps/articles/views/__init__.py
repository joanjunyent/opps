#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404

from haystack.views import SearchView

from opps.articles.models import Post, Album
from opps.articles.views.generic import OppsDetail, OppsList


class PostList(OppsList):
    obj = Post
    type = "channels"


class PostDetail(OppsDetail):
    obj = Post
    type = 'articles'


class AlbumList(OppsList):
    obj = Album
    type = "channels/album"


class AlbumDetail(OppsDetail):
    obj = Album
    type = 'articles/album'


class Search(SearchView):
    def get_results(self):
        return self.form.search().order_by('-date_available')

    def build_page(self):
        paginator = Paginator(self.results, self.results_per_page)
        try:
            paginator.page(int(self.request.GET.get('page', 1)))
        except InvalidPage:
            raise Http404("No such page!")

        return (None, self.results)
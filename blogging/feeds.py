from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class LatestEntriesFeed(Feed):
    title = "Posts"
    link = "/posts/"
    description = "rss feed for latest posts"

    def items(self):
        return Post.objects.all().order_by('published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if Post has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse('post-detail', args=[item.pk])
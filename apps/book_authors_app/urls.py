from django.conf.urls import url
from . import views
                    
urlpatterns = [
    # books
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^books/(?P<book_id>\d+)$', views.books),
    url(r'^add_author_to_book$', views.add_author_to_book),
    # authors
    url(r'^authors$', views.authors),
    url(r'^add_author$', views.add_author),
    url(r'^author_page/(?P<author_id>\d+)$', views.author_page),
    url(r'^add_book_to_author$', views.add_book_to_author)
]
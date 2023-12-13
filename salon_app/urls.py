from django.contrib import admin
from django.urls import path , include

from .router import router


from .views import      EventoListView   \
                    ,   EventoDetailView \
                    ,   EventoCreateView \
                    ,   EventoUpdateView \
                    ,   EventoDeleteView \
                  

app_name = "salon_app"

urlpatterns = [
    # Evento URLs

    path("evento/", EventoListView.as_view(), name='evento_all'),
    path("create/", EventoCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", EventoDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", EventoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", EventoDeleteView.as_view(), name="delete"),
]

urlpatterns += router.urls
from django.urls import path

from . import views

app_name= "polls"            #especificar o nome do app para que que o django saiba que é esse app
urlpatterns  = [             #para ser executado se houver uma views de mesmo nome
    path("", views.IndexView.as_view(), name = "index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name= "results"),
    path("<int:question_id>/vote/", views.vote, name= "vote")
]

''' o 2° e 3° mudaram pq as views detail() e results() vão ser  alteradas'''
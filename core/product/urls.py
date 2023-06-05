from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("list/", views.list_view, name="list"),
    path("create/", views.create_view, name="create"),
    path("detail/<id>/", views.detail_view, name="detail"),
    path("update/<id>/", views.update_blog_view, name="update"),

]

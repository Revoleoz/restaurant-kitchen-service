from django.urls import path

from kitchen.views import (
    index,
    DishTypesListView,
    DishTypesCreateView,
    DishTypesUpdateView,
    DishTypesDeleteView,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishDetailView,
    CookListView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    CookDetailView,
    toggle_assign_to_dish,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypesListView.as_view(), name="dish-type-list"),
    path(
        "dish-types/create/",
        DishTypesCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypesUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypesDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"),
    path("dish/<int:pk>/",
         DishDetailView.as_view(),
         name="dish-detail"),
    path("cook/",
         CookListView.as_view(),
         name="cook-list"),
    path(
        "cook/create/",
        CookCreateView.as_view(),
        name="cook-create"),
    path("cook/<int:pk>/update/",
         CookUpdateView.as_view(),
         name="cook-update"),
    path("cook/<int:pk>/delete/",
         CookDeleteView.as_view(),
         name="cook-delete"),
    path("cook/<int:pk>/",
         CookDetailView.as_view(),
         name="cook-detail"),
    path(
        "dish/<int:pk>/assignment/",
        toggle_assign_to_dish,
        name="dish-toggle-assignment"),
]

app_name = "kitchen"

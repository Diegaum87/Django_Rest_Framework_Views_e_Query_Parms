from django.urls import path
# import o views
from .views import PersonView, PersonDetailView

# precisa manter o nome urlpattners
# crie o endpoint e passe a view no final
urlpatterns = [
    path("persons/", PersonView.as_view()),
    path("persons/<int:person_id>", PersonDetailView.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('app/notes', views.NoteList.as_view(), name='notes_list'), # api/contacts will be routed to the ContactList view for handling
    path('app/notes/<int:pk>', views.NoteDetail.as_view(), name='note_detail'), # api/contacts will be routed to the ContactDetail view for handling
]

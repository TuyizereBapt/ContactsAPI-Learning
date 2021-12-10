from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions


class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Filtering out contacts for other users
    # And keeping contacts only for the currently logged in user
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    # Filtering out contacts for other users
    # And keeping contacts only for the currently logged in user
    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)



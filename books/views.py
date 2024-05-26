# books/views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

from .models import Book
from .serializers import BookSerializer


# custom class to check if user is superuser
class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class IsIndy(BasePermission):
    """Custom class to check if user is Indy."""
    def has_object_permission(self, request, view, obj):
        # If book is not restricted, anyone can see 
        if not obj.restricted:
            return True
        # if book is restricted, check if user is Indy, if it is Indy has access
        return request.user.username == "indy"


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
    #permission_classes = [IsSuperUser]  # runs the custom class IsSuperUser to check if user is superuser
    #permission_classes = [IsIndy | IsSuperUser]   # runs the custom classes IsIndy and IsSuperUser to check if either is true

    def get_queryset(self):
        return Book.objects.all()
      
        # substitute the code below to filter restricted books
        #if self.request.user.is_staff:
        #    return Book.objects.all()

        #return Book.objects.filter(restricted=False)


@login_required
def library(request):
    output = f"""
        <html>
            <body>
                <h2>Library</h2>
                <p>{request.user.username}</p>
                <a href="/books/books/">Books API</a>
                <br/>
                <a href="/accounts/logout/">Logout</a>
            </body>
        </html>
    """
    return HttpResponse(output)

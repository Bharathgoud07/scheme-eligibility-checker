from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from eligibility.models import Scheme
from documents.models import Document


def home(request):
    # Get dynamic counts from database
    schemes_count = Scheme.objects.count()
    documents_count = Document.objects.count()

    return render(request, 'home.html', {
        'schemes_count': schemes_count if schemes_count > 0 else 8,
        'documents_count': documents_count if documents_count > 0 else 12,
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('profile/', include('profiles.urls')),
    path('documents/', include('documents.urls')),
    path('eligibility/', include('eligibility.urls')),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path, include
from django.contrib import admin

# docker build -t cs2ranking .
# docker run -dp 127.0.0.1:8000:8000 cs2ranking

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),
    path('cs2ranking/', include('CS2Ranking.urls')),
]

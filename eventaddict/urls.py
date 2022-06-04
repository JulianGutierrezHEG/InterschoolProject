from django.contrib import admin
from django.urls import path,include
from .routers import router
from django.views.generic import TemplateView
from core.views import frontpage, signup
from django.contrib.auth import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('places/', TemplateView.as_view(template_name='places.html'),name='places'),
    path('events/', TemplateView.as_view(template_name='events.html'),name='events'),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', include('core.urls')),
    path('eventsDasboard/', include('core.urls')),
]

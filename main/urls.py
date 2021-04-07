from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #Blogs
    path('blog/', include('blog.urls')),

    #Store
    path('store/', include('store.urls')),

    #Basket
    path('basket/', include('basket.urls')),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

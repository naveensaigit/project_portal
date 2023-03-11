from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('users.urls')),
    # path('signup/', users_views.signup, name='signup'),
    path('login/', users_views.Login.as_view(), name='login'),
    path('logout/', users_views.Logout, name='logout'),
    path('', include('home.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG == False:
    handler404 = "home.views.errorPage404"
    handler500 = "home.views.errorPage500"

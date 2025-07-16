from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_pannel'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('signup/', SignupView, name='signup'),
    path('', HomeView, name='Home'),
    path('book_table/', BookTableView, name='Book_Table'),
    path('menu/', MenuView, name='Menu'),
    path('about/', AboutView, name='About'),
    path('feedback/', FeedbackView, name='Feedback_Form'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('get-cart-items/', get_cart_items, name='get_cart_items'),
    path('menu/', MenuView, name='menu_list'),
    path('menu/category/<int:category_id>/', MenuView, name='menu_list_by_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

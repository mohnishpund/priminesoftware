from django.urls import path
from . import views
from .views import HomeView, AddBookingView, UpdateBookingView, DeleteBookingView

urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),

    
    path('booking-list/',views.ShowAll, name='booking-list'),
    path('booking-detail/<int:pk>/',views.ViewBooking, name='booking-detail'),
    path('booking-create/',views.CreateBooking, name='booking-create'),
    path('booking-update/<int:pk>/',views.UpdateBooking, name='booking-update'),
    path('booking-delete/<int:pk>/',views.DeleteBooking, name='booking-delete'),
    
    #path('', views.home, name="home"),

    path('', HomeView.as_view(), name="home"),
    path('create_booking', AddBookingView.as_view(), name='create_booking'),
    path('update_booking/<int:pk>', UpdateBookingView.as_view(), name='update_booking'),
    path('delete_booking/<int:pk>', DeleteBookingView.as_view(), name='delete_booking'),
]
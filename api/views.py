from django.shortcuts import render,  get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse_lazy


from .serializers import BookingSerializer, DataSerializer
from .models import Booking
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.


"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }
    return Response(api_urls);
"""

@api_view(['GET'])
def ShowAll(request):
    booking = Booking.objects.all()
    serializer = BookingSerializer(booking, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def ViewBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    serializer = BookingSerializer(booking, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def CreateBooking(request):
    serializer = BookingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdateBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    serializer = BookingSerializer(instance=booking, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def DeleteBooking(request, pk):
    booking = BookingSerializer.objects.get(id=pk)
    booking.delete()

    return Response("Item Deleted Successfully..!")

#@api_view(['GET'])
#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
    model = Booking
    #form_class = DataSerializer
    template_name = 'home.html'


class AddBookingView(CreateView):
    model = Booking
    form_class = DataSerializer
    template_name = 'create_booking.html'
    success_url = reverse_lazy('home')
   

class UpdateBookingView(UpdateView):
    model = Booking
    form_class = DataSerializer
    template_name = 'update_booking.html'
    success_url = reverse_lazy('home')

class DeleteBookingView(DeleteView):
    model = Booking
    template_name ='delete_booking.html'
    success_url = reverse_lazy('home')
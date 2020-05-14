from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('contact.html', views.contact, name='contact'),
	path('about-us.html', views.about, name='about'),
	path('causes.html', views.causes, name='causes'),
	path('donate.html', views.donate, name='donate'),
	path('payment.html', views.payment, name='payment'),
	path('charge/', views.charge, name='charge'),
	path('change/', views.change, name='change'),
	path('paypal_payment/', views.payment_checkout, name='payment_checkout'),
	path('checkout/<int:arg>', views.checkout, name='checkout'),

	path('success/<str:args>/', views.successMsg, name='success'),
]
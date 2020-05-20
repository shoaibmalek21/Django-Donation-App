from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.core.mail import send_mail

from . models import *
import stripe
import json

stripe.api_key = 'sk_test_7GWBNRzTyUfispytEqqxy1To002MtJXuco'

def index(request):
	return render(request, 'index.html')

def contact(request):
	if request.method == "POST":
		message_name = request.POST['name']	
		message_email = request.POST['email']	
		message_subject = request.POST['subject']	
		message = request.POST['message']	

		send_mail(
				message_name,
				message,
				message_email,
				['shoaib@gmail.com'],
			)
		# contact_data = Contact()
		return render(request, 'contact.html', {'message_name':message_name,'message_email':message_email,'message_subject':message_subject,'message':message})
	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about-us.html')

def causes(request):
	return render(request, 'causes.html')

def donate(request):
	return render(request, 'base/donate.html')

# def payment_info(request):
# 	if request.method == 'POST':
# 		amount = int(request.POST['amount'])
# 	return redirect(reverse('payment', args=[amount]))

def payment(request):
	return render(request, 'base/payment.html')


def payment_checkout(request):
	return render(request, 'base/payment_checkout.html')

def charge(request):
	if request.method == 'POST':

		print('Data', request.POST)
		amount = int(request.POST['amount'])


		customer = stripe.Customer.create(
			email = request.POST['email'],
			name = request.POST['nickname'],
			address= {
			      'line1': '510 Townsend St',
			      'postal_code': '98140',
			      'city': 'San Francisco',
			      'state': 'CA',
			      'country': 'US',
			    },
			source = request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description='Donation'
			)

	return redirect(reverse('success', args=[amount]))

def change(request):
	if request.method == 'POST':

		print('Data', request.POST)
		amount = int(request.POST['amount'])
		print(amount)

	return redirect(reverse('checkout', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount': amount})

def checkout(request, arg):
	amount = arg
	return render(request, 'base/checkout.html',{'amount': amount})

def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:',body)
	return JsonResponse('Payment Complete',safe=False)
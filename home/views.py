from django.shortcuts import redirect, render
from sunil.models import *
from owner.models import *
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def payment_verify(request):
    if request.method == 'POST':
        order_id = request.POST.get('razorpay_order_id')
        payment_id = request.POST.get('razorpay_payment_id')
        signature = request.POST.get('razorpay_signature')
        
        payment = Auto_Shope_payment.objects.all().last()
        if client.utility.verify_payment_signature({
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }):
            payment.razorpay_payment_id = payment_id
            payment.razorpay_signature = signature
            payment.is_paid = True
            payment.save()
        else:
            payment.is_paid = False
            payment.save()

        return redirect('/office/softwar_charges/')

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def terms_and_conditions(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        context={
            'e':e,
            'bill':Farmer_bill.objects.filter(id=31).first(),
            'all_users':office_employee.objects.filter(shope_id=e.shope.id)

        }
        return render(request, 'home/terms_and_conditions.html', context)
    else:
        return redirect('login')

def login(request):
    if request.session.has_key('office_mobile'):
        return redirect('office_home')
    else:
        if request.method == "POST":
            number=request.POST ['number']
            pin=request.POST ['pin']
            o= office_employee.objects.filter(mobile=number,pin=pin,status=1, shope__status=1) 
            if o:
                request.session['office_mobile'] = request.POST["number"]
                return redirect('office_home')
            else:
                return redirect('/login/')
            
    return render(request, 'home/login.html')

def owner_logout(request):
    del request.session['owner_mobile']
    return redirect('/sunil/sunil_home/')

def office_logout(request):
    if request.session.has_key('office_mobile'):
        del request.session['office_mobile']
    return redirect('/')
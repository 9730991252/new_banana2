from django.shortcuts import redirect, render
from sunil.models import *
from owner.models import *
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ssl
import smtplib
from email.message import EmailMessage
import datetime
from django.contrib import messages 


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

def send_email(subject, body, email_sender, email_password, email_receiver):
    email_sender = email_sender
    email_password = email_password
    email_receiver = email_receiver
    
    subject = subject
    body = body
    
    # Compose email
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)

# Create your views here.
def index(request):
    if 'sine_up'in request.POST:
        shop_name = request.POST.get('shop_name')
        owner_name = request.POST.get('owner_name')
        owner_mobile = request.POST.get('owner_mobile')
        address = request.POST.get('address')
        description = request.POST.get('description')
        contact_details = request.POST.get('contact_details')
        body = f"""New Account Successfully Registered Successfully on { datetime.datetime.now() } 
        \n Shop Name = {shop_name}
        \n Owner Name = {owner_name}
        \n Owner Mobile = {owner_mobile}
        \n Address = {address}
        \n Description = {description}
        \n Contact Details = {contact_details}
        """
        
        if Shope.objects.filter(mobile=owner_mobile).exists():
            messages.error(request, 'This Shop is Already Registered.')
            return redirect('/')
        Shope.objects.create(
            shope_name=shop_name,
            owner_name=owner_name,
            mobile=owner_mobile,
            address=address,
            description=description,
            contact_details=contact_details,
            pin=0,
            edit_pin=1234,
            status=0,
        )
        office_employee.objects.create(
            shope = Shope.objects.filter(mobile=owner_mobile).last(),
            name = owner_name,
            mobile = owner_mobile,
            pin = 1234,
        )
        messages.success(request, 'Your Shop Registered Successfully. Our Team Contact You Soon From +91 9730 99 1252.')  
        send_email('New Registration On New Banana ', body, 'prasannadigital101@gmail.com', 'jmcjgjxfcpembcne', 'sunilkale101@gmail.com')
        return redirect('/')
        
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
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        if e:
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
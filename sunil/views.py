from django.shortcuts import redirect, render
from . models import *
from owner. models import *
from datetime import *
import month
# Create your views here.
def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["number"])
        b =int(request.POST["pin"])
        if a== 9730991252 and b== 876790143:
            request.session['sunil_mobile'] = a
            return redirect('sunil_home')
        else:
            return redirect('sunil_login')
    return render(request, 'sunil/sunil_login.html')


def sunil_home(request):
    if request.session.has_key('sunil_mobile'):
        if 'profile'in request.POST:
            id = request.POST.get('id')
            o = Shope.objects.filter(id=id).first()
            request.session['owner_mobile'] = o.mobile
            return redirect('/owner/owner_home/')

            
        if 'Add_shope'in request.POST:
            shope_name = request.POST.get('shope_name')
            owner_name = request.POST.get('owner_name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            edit_pin = request.POST.get('edit_pin')
            if Shope.objects.filter(mobile=mobile).exists():
                pass
            else:
                Shope(
                    shope_name=shope_name,
                    owner_name=owner_name,
                    mobile=mobile,
                    pin=pin,
                    edit_pin=edit_pin,
                ).save()    
            return redirect('sunil_home')
        if 'Edit_shope'in request.POST:
            id = request.POST.get('id')
            shope_name = request.POST.get('shope_name')
            owner_name = request.POST.get('owner_name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            edit_pin = request.POST.get('edit_pin')
            Shope(
                id=id,
                shope_name=shope_name,
                owner_name=owner_name,
                mobile=mobile,
                pin=pin,
               edit_pin=edit_pin,
            ).save()
            return redirect('sunil_home')
        if 'active'in request.POST:
            id = request.POST.get('id')
            c = Shope.objects.filter(id=id).first()
            c.status = 0
            c.save()
            return redirect('sunil_home')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            c = Shope.objects.filter(id=id).first()
            c.status = 1
            c.save()
            return redirect('sunil_home')
        if 'login'in request.POST:
            id = request.POST.get('id')
            e = office_employee.objects.filter(shope_id=id).first()
            if e:
                request.session['office_mobile'] = e.mobile
                return redirect('office_home')
            return redirect('sunil_home')
        shope = []
        # today_date = date(2025,6,1)
        for s in Shope.objects.all():
            today_date = date.today()
            status = ''
            if today_date < date(today_date.year, today_date.month, 6):
                status = 'show_worning'
            elif Shope_payment.objects.filter(shope_id=s.id, from_date__year=today_date.year, from_date__month=today_date.month-1).exists():
                status = 'paid'
            asp = Auto_Shope_payment.objects.filter(shope_id=s.id, added_date__year=today_date.year, month=month.Month(date.today().year, date.today().month - 1)).last()
            if asp:
                if asp.is_paid == True:
                    status = 'paid'
            if status == 'show_worning' or status == '' and today_date > date(today_date.year, today_date.month, 5):
                status = 'Not Paid'
            shope.append({
                        'id':s.id,
                        'shope_name':s.shope_name,
                        'owner_name':s.owner_name,
                        'mobile':s.mobile,
                        'pin':s.pin,
                        'edit_pin':s.edit_pin,
                        'status':s.status,
                        'is_paid':status
                          })
        
        context={
            'shope':shope
        }
        return render(request, 'sunil/sunil_home.html', context)
    else:
        return redirect('sunil_login')

def shope_detail(request, id):
    if request.session.has_key('sunil_mobile'):
        if 'Add_payment'in request.POST:
            amount = request.POST.get('amount')
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')
            payment_type = request.POST.get('payment_type')
            Shope_payment(
                shope_id=id,
                amount=amount,
                from_date=from_date,
                to_date=to_date,
                payment_type=payment_type,
            ).save()
            return redirect('shope_detail', id=id)
        context={
            'shope':Shope.objects.filter(id=id).first(),
            'payment':Shope_payment.objects.filter(shope_id=id).order_by('-id'),
        }
        return render(request, 'sunil/shope_detail.html', context)
    
def payment_detail(request):
    if request.session.has_key('sunil_mobile'):
        context={
            'payment':Shope_payment.objects.filter().order_by('-id')[0:100],
        }
        return render(request, 'sunil/payment_detail.html', context)
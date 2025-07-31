1
2
# Create your tests here.
## 8208492615
### 7709775093
6
7
8
9
10@register.simple_tag()
def check_shop_payment(shope_id):
    today_date = date.today()
    status = ''
    if today_date < date(today_date.year, today_date.month, 6):
        status = 'show_worning'
    elif Shope_payment.objects.filter(shope_id=shope_id, from_date__year=today_date.year, from_date__month=today_date.month-1).exists():
        status = 'paid'
    asp = Auto_Shope_payment.objects.filter(shope_id=shope_id, added_date__year=today_date.year, month=month.Month(date.today().year, date.today().month - 1)).last()
    if asp:
        if asp.is_paid == True:
            status = 'paid'
    if status == 'show_worning' or status == '' and today_date > date(today_date.year, today_date.month, 5):
        status = 'disable'
    return {'status':status, 'last_month':date(today_date.year, today_date.month-1, today_date.day)}
 
11
12
13
14
15
16
17
18
19
20
21  
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46

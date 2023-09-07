from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentDetailsForm, FeesForm
from .models import StudentDetails, Fees
from datetime import datetime

# Homepage ==============

def HomePage(request):
    return render(request,'index.html')

# Profiles ===================

def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user = authenticate(request,username=username, password = password)
        if user is not None:
            login(request,user)
            return redirect('HomePage')
        else:
            messages.error(request,"Username or Password Incorrect")
            return redirect("SignIn")
    return render(request,'login.html')

def SignOut(request):
    logout(request)
    return redirect('SignIn')

# student dats and calculations ============================

def Students(request):
    form = StudentDetailsForm()
    # form1  = FeesForm()
    
    if request.method == "POST":
        # return HttpResponse("all is fine")
        form = StudentDetailsForm(request.POST)
        # form1  = FeesForm(request.POST)
        
        if form.is_valid():
            data = form.save()
            data.save()
            
            messages.success(request,"Student Data Saved Success Please Add Admisiion fee")
            return redirect('Admissionfeeenter')
        else:
            messages.error(request,'Data Is Not Saved')
    
    context = {"form":form,"students":StudentDetails.objects.all()}
    return render(request,'students.html',context)

def Admissionfeeenter(request):
    form  = FeesForm()
    if request.method == "POST":
        form = FeesForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.save()
            messages.success(request,"Fee Saved Success")
            return redirect('Students')
        else:
            messages.error(request,'Data Is Not Saved')
            return redirect('Admissionfeeenter')
    
    context = {
        "form":form
    }
    return render(request,"admissionfeeenter.html",context)

def StudentSingleView(request,pk):
    student = StudentDetails.objects.get(id = pk)
    if request.method == "POST":
        name = request.POST['fname']
        dob = request.POST['dob']
        print(name,dob)
    context = {"student":student}
    return render(request,"studentsngleview.html",context)

def DeleteStudent(request,pk):
    StudentDetails.objects.get(id = pk).delete()
    messages.error(request,"Data Deleted Successfully")
    return redirect("Students")
    

def Expenses(request):
    return render(request,'expenses.html')


# Fee Calculations====================================

def FeesData(request):
    fees = Fees.objects.all()
    month_num = datetime.now().month
    month = datetime.now().strftime('%B')
    total_fee = 0
    student_num = 0
    for i in fees:
        month_fee = i.date.month
        if month_fee == month_num:
            total_fee += i.Fee_amount
            student_num += 1 
            
    pending_students = StudentDetails.objects.all().count() - student_num
            
    form = FeesForm()
    if request.method == "POST":
        form = FeesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Fee Added")
            return redirect('FeesData')
        else:
            messages.error(request,"Something Wrong")
            return redirect("FeesData")
        # return HttpResponse("form good")
    context = {"form":form,"fees":fees,"total_fee":total_fee,"pending_students":pending_students,"student_num":student_num,"month":month}
    return render(request,'fees.html',context)

def FeeGivenDetails(request):
    fees = Fees.objects.all().order_by("-date")
    context = {"Fee":fees}
    return render(request,'collectedfees.html',context)

def UpcomingPayments(request):
    
    from datetime import datetime, timedelta
    from django.utils import timezone

    # Calculate the start date (7 days ago from the current date)
    start_date = timezone.now()
    end_date = start_date + timedelta(days=7)

    # Query the database to filter rows within the last 7 days (ignoring month and year)
    results = StudentDetails.objects.filter(Date_of_Joining__day__gte=start_date.day,Date_of_Joining__day__lte=end_date.day)
    
    current_month = timezone.now().month
    current_year = timezone.now().year

    # Query to find persons with payments in the current month and year
    feepayedstudents = Fees.objects.filter(date__month=current_month,date__year=current_year).distinct()
    upcommimgfeestudents = []
    print(feepayedstudents)
    for val in results:
        flag = 0
        for fee in feepayedstudents:
            if fee.student == val:
                flag = 1
            else:
                continue
        if flag == 0:
            upcommimgfeestudents.append(val)
        else:
            continue
                       
    context = {"upcomming":upcommimgfeestudents}
    return render(request,"upcommingpayments.html",context)

def PendinFees(request):
    from datetime import datetime, timedelta
    from django.utils import timezone
    current_month = timezone.now().month
    current_year = timezone.now().year
    pendingstudents = []
    
    students = StudentDetails.objects.all()
    for i in students:
        
        feepayedstudents = Fees.objects.filter(date__month=current_month,date__year=current_year,student = i)
        
        if feepayedstudents is not None:
            continue
        else:
            pendingstudents.append(i)
         
    print(pendingstudents)
    
    return render(request,"pendingfees.html")
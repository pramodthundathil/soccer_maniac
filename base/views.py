from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentDetailsForm, FeesForm, ExpenseForm, IncomeForm
from .models import StudentDetails, Fees, Expense, Income, EmailAddress
from datetime import datetime
from datetime import datetime, timedelta
from django.utils import timezone
# Homepage ==============

def HomePage(request):
    current_month = timezone.now().month
    current_year = timezone.now().year
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
    
    expense = Expense.objects.filter(Date__month = current_month, Date__year = current_year) 
    total_expense = 0
    for i in expense:
        total_expense += i.Amount 
        
    income = Income.objects.filter(Date__month = current_month, Date__year = current_year) 
    total_income = 0
    for j in expense:
        total_income += j.Amount
        
        
           
    context = {"fees":fees,"total_fee":total_fee,"pending_students":pending_students,"student_num":student_num,"month":month,"students":StudentDetails.objects.all().count(),"total_expense":total_expense,"total_income":total_income}

    return render(request,'index.html',context)

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

# def PendinFees(request):
#     from datetime import datetime, timedelta
#     from django.utils import timezone
#     current_month = timezone.now().month
#     current_year = timezone.now().year
    
    # pendingstudents = Fees.objects.exclude(date__month =current_month,date__year=current_year)

    # students_val = []
    # students = StudentDetails.objects.all()
    # for i in students:
        
    #     feepayedstudents = Fees.objects.filter(date__month =current_month,date__year=current_year,student = i)
        # pendingstudents.append(feepayedstudents)
        # print(feepayedstudents,"========================================")
        
        # if feepayedstudents is not None:
        #     continue
        # else:
        #     pendingstudents.append(i)
    for i in pendingstudents:
        students_val.append(i.student)
        
        
    from django.db.models import F, Count, Q
    from django.db.models.functions import ExtractMonth

# Get the current month
# current_month = 9  # Replace with the current month number (e.g., 9 for September)

# Query the database
    # results = Fees.objects.filter(~Q(date__month=current_month,date__year=current_year),  # Exclude records in the current month
    # student__in=Fees.objects.values('student').annotate(foreign_key_count=Count('student')).filter(student=1)  # Filter for foreign key elements with a count of 1
    # )

    # print(results,"========================")   
    # pending_students = list(set(students_val))
    # from django.db.models import F, Count
    # duplicates = pendingstudents.values('student').annotate(count=Count('student')).filter(count__gt=1)
    # Get a list of related_field values that are duplicates
    # duplicate_related_field_values = [item['student'] for item in duplicates]

    # Exclude objects with duplicate related_field values
    # filtered_queryset = pendingstudents.exclude(student__in=duplicate_related_field_values)
    # queryset = pendingstudents.order_by('student', 'id').distinct('student')
    # print(filtered_queryset)
    # context = {
    #     "pendingstudents":pending_students
    # }
    # return render(request,"pendingfees.html",context)

def PendinFees(request):
    
    current_month = timezone.now().month
    current_year = timezone.now().year
    current_day = timezone.now().day
    pendingstudents = Fees.objects.exclude(date__month =current_month,date__year=current_year)
    feepaiedstudents = Fees.objects.filter(date__month =current_month,date__year=current_year)
    
    studentsfeepending = []
    studentsfeepaid = []
    final_fee_pending = []
    for i in pendingstudents:
        studentsfeepending.append(i.student)
    for j in feepaiedstudents:
        studentsfeepaid.append(j)
        
    students = StudentDetails.objects.all()
    
    pending_on_month = list(set(students).difference(set(studentsfeepending)))
    print(pending_on_month)
    print(students[0].Date_of_Joining.day)
    final_fee_pending.extend(pending_on_month)
    
    for item in studentsfeepending:
        try:
            feepend = Fees.objects.get(date__day__lte = item.Date_of_Joining.day, student = item)
            final_fee_pending.append(feepend.student)
        except:
            continue
        
    print(final_fee_pending)
    
    for stu in final_fee_pending:
        if stu.Date_of_Joining.day > current_day:
            final_fee_pending.remove(stu)
    fees = Fees.objects.all()
    email = EmailAddress.objects.all()
    emails = []
    for i in email:
        emails.append(i.email)
    mail_subject = 'Pending Fee Deatails.'
    message = render_to_string('emailbody.html', {"pendingstudents":final_fee_pending})
    email = EmailMessage(mail_subject, message, to=emails)
    email.send(fail_silently=True)
    
    context = {
        "pendingstudents":final_fee_pending
    }
    return render(request,"pendingfees.html",context)

from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string



                

def FeeSigleView(request,pk):
    
    student = StudentDetails.objects.get(id = pk)
    
    fees = Fees.objects.filter(student = student).order_by("-date")
    
    context = {"student":student,"fees":fees}
    return render(request,"fee_studentsingleview.html",context)

def DeleteFee(request,pk):
    student = Fees.objects.get(id = pk).student
    Fees.objects.get(id = pk).delete()
    messages.error(request,"Fee Data Deleted")
    return redirect("FeeSigleView", student.id)



def Expenses(request):
    current_month = timezone.now().month
    current_year = timezone.now().year
    current_day = timezone.now().day
    
    expense = Expense.objects.filter(Date__month = current_month, Date__year = current_year)
    expense_today = Expense.objects.filter(Date__month = current_month, Date__year = current_year, Date__day = current_day)
    income = Income.objects.filter(Date__month = current_month, Date__year = current_year)
    income_today = Income.objects.filter(Date__month = current_month, Date__year = current_year,Date__day = current_day)
    
    month = datetime.now().strftime('%B')
    month_total = 0
    day_total = 0
    month_income = 0
    day_income = 0
    credit = 0
    
    
    for i in expense:
        month_total +=  i.Amount
        
    for j in expense_today:
        day_total += j.Amount
        
    
    for k in income:
        month_income += k.Amount
        if k.Mode_Of_Payment == "Credit":
            credit += k.Amount
    
    for h in income_today:
        day_income += h.Amount
        

        
        
    form1 = IncomeForm()
    form = ExpenseForm()
    
    context = {
        "form1":form1,"form":form,"expanse":expense,"income":income,"month":month, "month_total":month_total, "day_total":day_total,"day_income":day_income,"month_income":month_income, "credit":credit,
    }
    return render(request,'expenses.html',context)

def IncomeAdd(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Income values added")
            return redirect("Expenses")
        else:
            messages.success(request,"Operation failed")
            return redirect("Expenses")
        
def ExpenseAdd(request):
    expense = Expense.objects.all()
    income = Income.objects.all()
    month = datetime.now().strftime('%B')
    
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Expense values added")
            return redirect("Expenses")
        else:
            messages.success(request,"Operation failed")
            return redirect("Expenses")
        
def ExpenseTotalView(request):
    current_month = timezone.now().month
    current_year = timezone.now().year
    current_day = timezone.now().day
    
    expense = Expense.objects.all().order_by("-Date")
    expense_today = Expense.objects.filter(Date__day = current_day,Date__month = current_month,Date__year = current_year)
    expense_month = Expense.objects.filter(Date__month = current_month,Date__year = current_year)

    context = {
        "expense":expense,
        "expense_today":expense_today,
        "expense_month":expense_month
    }
    return render(request,"expense_singleview.html",context)

def DeleteExpense(request,pk):
    Expense.objects.get(id = pk).delete()
    messages.error(request,"Expense Data Deleted")
    return redirect("ExpenseTotalView")

def IncomeTotalView(request):
    current_month = timezone.now().month
    current_year = timezone.now().year
    current_day = timezone.now().day
    income = Income.objects.all()
    income_today = Income.objects.filter(Date__day = current_day,Date__month = current_month,Date__year = current_year)
    income_month = Income.objects.filter(Date__month = current_month,Date__year = current_year)
    income_credit = Income.objects.filter(Mode_Of_Payment = "Credit") 
    
    
    
    
    context = {
        "income":income,"income_today":income_today,
        "income_month":income_month,
        "credit": income_credit
    }
    return render(request,"income_single_view.html",context)

def DeleteIncome(request,pk):
    Income.objects.get(id=pk).delete()
    messages.info(request,"Income Data deleted")
    return redirect("IncomeTotalView")

def CreditChange(request,pk):
    income = Income.objects.get(id = pk)
    income.Mode_Of_Payment = "Credit-Received"
    income.save()
    return redirect("IncomeTotalView")


# report Generation Functions-------------------------------------

from django.http import HttpResponse
import csv


def GenerateStudentReport(request):
    student = StudentDetails.objects.all()
    date = timezone.now().month
    date_year = timezone.now().year
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=studentreport{}-{}.csv'.format(date,date_year)
    writer = csv.writer(response)
    writer.writerow(['FullName',"Date_of_Joining","Date_of_Birth",'Address','Phone_Number','Email',"Parents_Mobile_Number",'Blood_Group','Class_Studing',"School","School_Timeing",])
    for i in student:
        writer.writerow([i.FullName,i.Date_of_Joining,i.Date_of_Birth,i.Address,i.Phone_Number,i.Email,i.Parents_Mobile_Number,i.Blood_Group,i.Class_Studing,i.School,i.School_Timeing])

    return response

def FeeReportDate(request):
    if request.method =="POST":
        s_date = request.POST["datestart"]
        e_date = request.POST["dateend"]
    
    
        date = timezone.now().month
        date_year = timezone.now().year
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename=Feereport_sorted{}-{}.csv'.format(date,date_year)
        
        fees = Fees.objects.filter(date__gte = s_date, date__lte = e_date)
        
        writer = csv.writer(response)
        writer.writerow(['student',"Fee_amount","date",'payment mode','reason'])
        for i in fees:
            writer.writerow([i.student.FullName,i.Fee_amount,i.mode,i.reason])

    return response

def FeeReportMonth(request):
    date = timezone.now().month
    date_year = timezone.now().year
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=Feereport_month{}-{}.csv'.format(date,date_year)
    
    fees = Fees.objects.filter(date__month = date, date__year = date_year).order_by("-date")
    
    writer = csv.writer(response)
    writer.writerow(['student',"Fee_amount","date",'payment mode','reason'])
    for i in fees:
        writer.writerow([i.student.FullName,i.Fee_amount,i.date,i.mode,i.reason])

    return response

def FeeReport(request):
    date = timezone.now().month
    date_year = timezone.now().year
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=Feereport{}-{}.csv'.format(date,date_year)
    
    fees = Fees.objects.all().order_by("-date")
    
    writer = csv.writer(response)
    writer.writerow(['student',"Fee_amount","date",'payment mode','reason'])
    for i in fees:
        writer.writerow([i.student.FullName,i.Fee_amount,i.date,i.mode,i.reason])

    return response
    
def ExpenseReport(request):
    
    date = timezone.now().month
    date_year = timezone.now().year
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=Expense{}-{}.csv'.format(date,date_year)
    
    expense = Expense.objects.all().order_by("-Date")
    
    writer = csv.writer(response)
    writer.writerow(['Date',"Amount","Reason"])
    for i in expense:
        writer.writerow([i.Date,i.Amount,i.Reason])

    return response

def ExpenseReportByDate(request):
    if request.method == "POST":
        s_date = request.POST["datestart"]
        e_date = request.POST["dateend"]
        date = timezone.now().month
        date_year = timezone.now().year
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename=Expense_by_date{}-{}.csv'.format(date,date_year)
        
        expense = Expense.objects.filter(Date__gte = s_date,Date__lte = e_date).order_by("-Date")
        
        writer = csv.writer(response)
        writer.writerow(['Date',"Amount","Reason"])
        for i in expense:
            writer.writerow([i.Date,i.Amount,i.Reason])

        return response
    
def IncomeReport(request):
    
    date = timezone.now().month
    date_year = timezone.now().year
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=Expense{}-{}.csv'.format(date,date_year)
    
    income = Income.objects.all().order_by("-Date")
    
    writer = csv.writer(response)
    writer.writerow(['Date',"Amount","Reason","Mode_Of_Payment",])
    for i in income:
        writer.writerow([i.Date,i.Amount,i.Reason,i.Mode_Of_Payment])

    return response

def IncomeReportByDate(request):
    if request.method == "POST":
        s_date = request.POST["datestart"]
        e_date = request.POST["dateend"]
        date = timezone.now().month
        date_year = timezone.now().year
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename=Expense_by_date{}-{}.csv'.format(date,date_year)
        income = Income.objects.filter(Date__gte = s_date,Date__lte = e_date).order_by("-Date")
    
        writer = csv.writer(response)
        writer.writerow(['Date',"Amount","Reason","Mode_Of_Payment",])
        for i in income:
            writer.writerow([i.Date,i.Amount,i.Reason,i.Mode_Of_Payment])

        return response
    
    
    
def AddEmail(request):
    if request.method == "POST":
        email = request.POST["email"]
        data = EmailAddress.objects.create(email = email)
        data.save()
        messages.info(request,"Email Saved")
    return redirect("HomePage")
    
    
    
    
    
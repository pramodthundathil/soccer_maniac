from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from celery import shared_task
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from .models import Fees, StudentDetails, EmailAddress
from datetime import timezone


@shared_task
def FeeEmail(request):
    mail_subject = 'Activate your E-Cart account.'
    message = render_to_string('emailbody.html', {})

    email = EmailMessage(mail_subject, message, to=['gopinath.pramod@gmail.com'])
    email.send(fail_silently=True)
    
class Command(BaseCommand):
    help = 'Send a scheduled email'

    def handle(self, *args, **options):
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
        email = EmailAddress.objects.all()
        emails = []   
        
        context = {
            "pendingstudents":final_fee_pending
        }
        mail_subject = 'Activate your E-Cart account.'
        message = render_to_string('emailbody.html', context)

        email = EmailMessage(mail_subject, message, to=email)
        email.send(fail_silently=True)
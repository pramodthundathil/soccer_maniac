from django.db import models

class StudentDetails(models.Model):
    
    FullName = models.CharField(max_length=255)
    Date_of_Birth = models.DateField(auto_now_add=False)
    Address = models.TextField()
    Phone_Number = models.CharField(max_length=15)
    Email = models.EmailField()
    Parents_Mobile_Number = models.CharField(max_length=15)
    blood = (("A+","A+"),("A-","A-"),("B+","B+"),("B-","B-"),("O+","O+"),("O-","O-"),("AB+","AB+"),("AB-","AB-")) 
    Blood_Group = models.CharField(max_length=20, choices=blood)
    ID_Proof_Submitted = models.BooleanField(default=True)
    ids = (("Aadhaar","Aadhaar"),("Driving License","Driving License"),("Voter Id","Voter Id"),("PanCard","Pancard"),("School Id","Scool Id"),("Other","Other"),("Not Submitted","Not Submitted"))
    Type_Of_Id_Proof = models.CharField(max_length=20,choices=ids)
    
    Class_Studing = models.CharField(max_length=255)
    School = models.CharField(max_length=255)
    School_Timeing = models.CharField(max_length=255) 

    Date_of_Joining = models.DateField(auto_now_add=False)
    Date_of_Leaving = models.DateField(auto_now_add=False,null=True,blank=True)
    Course_Duration_In_Months = models.IntegerField(blank=True, null=True)
    
    Total_Fee = models.FloatField(null=True, blank=True)
    Discount = models.IntegerField(null=True, blank=True)
    Fee_Installments = models.FloatField(null=True, blank=True)
    
    Live_Status = models.BooleanField(default=True)
    
    # Date_of_Birth.widget.atter.update({"type":"date"})
    
    def __str__(self):
        return self.FullName
    
class Fees(models.Model):
    student = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    Fee_amount = models.FloatField()
    date = models.DateField(auto_now_add=False)
    mo = (("Cash","Cash"),("Bank","Bank"),("UPI","UPI"))
    mode = models.CharField(max_length=25,choices=mo)
    opt = (("Admission Fee","Admission Fee"),("Monthly Fee","Monthly Fee"),("Other","Other"))
    reason = models.CharField(max_length=30,choices=opt,null=True, blank=True)
    
    def __str__(self):
        return self.student.FullName
    
class Income(models.Model):
    
    Date = models.DateField(auto_now_add=False)
    Amount = models.FloatField()
    Reason = models.CharField(max_length=1000)
    option = (("Credit","Credit"),("Cash","Cash"),("Bank","Bank"),("UPI","UPI"))
    Mode_Of_Payment = models.CharField(choices=option,max_length=255)
    Cash_received = models.BooleanField(default=True)

class Expense(models.Model):
    
    Date = models.DateField(auto_now_add=False)
    Amount = models.FloatField()
    Reason = models.CharField(max_length=1000)

    
    
    
    
    

from django.forms import ModelForm, TextInput
from .models import StudentDetails, Fees
from datetime import datetime

date =  str(datetime.now()).split(" ")[0]


class StudentDetailsForm(ModelForm):
    
    
    class Meta:
        model = StudentDetails
        fields = ["FullName","Date_of_Birth","Address","Phone_Number","Email","Parents_Mobile_Number","Blood_Group","ID_Proof_Submitted","Type_Of_Id_Proof","Class_Studing","School","School_Timeing","Date_of_Joining"]
        # fields = "__all__"
    
        widgets = {
            "Date_of_Birth": TextInput(attrs={"type":"date", "max":date}),
            "Phone_Number": TextInput(attrs={"type":"number"}),
            "Email": TextInput(attrs={"type":"email"}),
            "Parents_Mobile_Number": TextInput(attrs={"type":"number"}),
            "Date_of_Joining": TextInput(attrs={"type":"date","max":date}),
            "Date_of_Leaving": TextInput(attrs={"type":"date"}),
            "Course_Duration_In_Months":TextInput(attrs={"max":12})
        }
        
class FeesForm(ModelForm):
    class Meta:
        model = Fees
        fields = "__all__"
        
        widgets = {
            "date":TextInput(attrs={"max":date,"type":"date"})
        }    

        

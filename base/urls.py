from django.urls import path 
from .import views 

urlpatterns = [
    path("HomePage",views.HomePage,name="HomePage"),
    path("",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("Students",views.Students,name="Students"),
    path("Expenses",views.Expenses,name="Expenses"),
    path("FeesData",views.FeesData,name="FeesData"), 
    path("StudentSingleView/<int:pk>",views.StudentSingleView,name="StudentSingleView"), 
    path("DeleteStudent/<int:pk>",views.DeleteStudent,name="DeleteStudent") ,
    path("FeeGivenDetails",views.FeeGivenDetails,name="FeeGivenDetails"),
    path("Admissionfeeenter",views.Admissionfeeenter,name="Admissionfeeenter"),
    path("UpcomingPayments",views.UpcomingPayments,name="UpcomingPayments"),
    path("PendinFees",views.PendinFees,name="PendinFees"), 
     
] 
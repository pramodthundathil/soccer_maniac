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
    path("FeeSigleView/<int:pk>",views.FeeSigleView,name="FeeSigleView"), 
    path("DeleteFee/<int:pk>",views.DeleteFee,name="DeleteFee"), 
    path("IncomeAdd",views.IncomeAdd,name="IncomeAdd"), 
    path("ExpenseAdd",views.ExpenseAdd,name="ExpenseAdd"),
    path("ExpenseTotalView",views.ExpenseTotalView,name="ExpenseTotalView"),
    path("DeleteExpense/<int:pk>",views.DeleteExpense,name="DeleteExpense"), 
    path("IncomeTotalView",views.IncomeTotalView,name="IncomeTotalView"), 
    path("DeleteIncome/<int:pk>",views.DeleteIncome,name="DeleteIncome"), 
    path("CreditChange/<int:pk>",views.CreditChange,name="CreditChange"), 
    path("GenerateStudentReport",views.GenerateStudentReport,name="GenerateStudentReport"), 
    path("FeeReportDate",views.FeeReportDate,name="FeeReportDate"),
    path("FeeReportMonth",views.FeeReportMonth,name="FeeReportMonth"), 
    path("FeeReport",views.FeeReport,name="FeeReport"), 
    path("ExpenseReport",views.ExpenseReport,name="ExpenseReport"), 
    path("ExpenseReportByDate",views.ExpenseReportByDate,name="ExpenseReportByDate"), 
    path("IncomeReport",views.IncomeReport,name="IncomeReport"), 
    path("IncomeReportByDate",views.IncomeReportByDate,name="IncomeReportByDate"),
    path("AddEmail",views.AddEmail,name="AddEmail"), 
     
              
] 
from django.urls import path
from OrganApp.admin_views import index,ViewBloodDonorList,ViewOrganDonorList,ViewpledgeformList,View_all_users,Add_Blood_Bank,RemoveUsers,Checkup,View_all_blood_bank,RemoveBank,editbank

urlpatterns = [
    path('', index.as_view()),
    path('ViewBloodDonorList',ViewBloodDonorList.as_view()),
    path('ViewOrganDonorList',ViewOrganDonorList.as_view()),
    path('ViewpledgeformList',ViewpledgeformList.as_view()),
    path('View_all_users',View_all_users.as_view()),
    path('Add_Blood_Bank',Add_Blood_Bank.as_view()),
    path('RemoveUsers', RemoveUsers.as_view()),
    path('checkuplists',Checkup.as_view()),
    path('viewbloodbank',View_all_blood_bank.as_view()),
    path('removebank',RemoveBank.as_view()),
    path('editbank',editbank.as_view()),
    # path('Rejectuser',Rejectuser.as_view()),
    # path('Feedback_view',fbview.as_view()),
    # path('Assign_pharmacy',Assign_pharmacy.as_view()),
    # path('Category_Add',Category_Add.as_view())


]

def urls():
    return urlpatterns, 'admin','admin'
from django.urls import path
from OrganApp.bank_views import index,addblood,UpdateBloodStock,ViewBloodStock,ProfileView
urlpatterns = [
    path('', index.as_view()),
    path('addblood',addblood.as_view()),
    path('UpdateBloodStock',UpdateBloodStock.as_view()),
    path('ViewBloodStock',ViewBloodStock.as_view()),
    path('ProfileView',ProfileView.as_view()),
    # path('View_all_users',View_all_users.as_view()),
    # path('rejectshop',RejectShop.as_view()),
    # path('confirmorder', ConfirmOrder.as_view()),
    # #path('approve',ApproveView.as_view()),
    # path('Reject',Reject.as_view()),
    # path('Manage_users',Manage_users.as_view()),
    # path('ApproveUser',ApproveUser.as_view()),
    # path('Rejectuser',Rejectuser.as_view()),
    # path('Feedback_view',fbview.as_view()),
    # path('Assign_pharmacy',Assign_pharmacy.as_view()),
    # path('Category_Add',Category_Add.as_view())


]

def urls():
    return urlpatterns, 'bloodbank','bloodbank'
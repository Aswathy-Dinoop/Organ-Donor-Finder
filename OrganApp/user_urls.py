from django.urls import path
from django.contrib import messages
from OrganApp import user_views
from OrganApp.user_views import index, MyBloodDonateDetails, blood_donation_form, organ_donation_form, \
    OrganDonorAfterDeath, ProfileView, MyOrganDonateDetails, BloodDonationEdit, BloodDonationDelete, \
    ViewAllBloodDonorList, ViewAllOrganDonorList, UpdateProfile,ViewAllBloodbankDetails,ViewCheckup

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('blood_donation_form',blood_donation_form.as_view()),
    path('organ_donation_form',organ_donation_form.as_view(),name='organ_donation_form'),
    path('OrganDonorAfterDeath',OrganDonorAfterDeath.as_view()),
    path('ProfileView',ProfileView.as_view()),
    path('UpdateProfile',UpdateProfile.as_view()),
    path('MyBloodDonateDetails',user_views.MyBloodDonateDetails,name='MyBloodDonateDetails'),
    path('MyOrganDonateDetails',user_views.MyOrganDonateDetails,name='MyOrganDonateDetails'),
    path('BloodDonationEdit',BloodDonationEdit.as_view()),
    path('BloodDonationDelete',BloodDonationDelete.as_view()),
    # path('blooddonatview',user_views.blooddonatview,name='blooddonate'),
    path('ViewAllBloodDonorList',ViewAllBloodDonorList.as_view()),
    path('ViewAllOrganDonorList',ViewAllOrganDonorList.as_view()),

    path('ViewAllBloodbankDetails', ViewAllBloodbankDetails.as_view()),
    path('ViewCheckup',ViewCheckup.as_view())



]

def urls():
    return urlpatterns, 'user','user'
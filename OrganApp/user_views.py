from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from OrganApp.models import Blood_Donation,Registration,Organ_Donation,Pledge_Form,BloodStocks,BloodBank
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from datetime import datetime
class index(TemplateView):
    template_name='user/index.html'
class blood_donation_form(TemplateView):
    template_name='user/blood_donation_form.html'
    def get_context_data(self, **kwargs):
        context = super(blood_donation_form, self).get_context_data(**kwargs) 
        abc=Registration.objects.get(user_id=self.request.user.id)
        context['pro'] = abc  
        return context
    def post(self, request, *args, **kwargs):
        public=Registration.objects.get(user_id=self.request.user.id)
        bloodgroup = request.POST['bloodgroup']
        healthissue = request.POST['health']

        dateofdonation = request.POST['date']
        dateofdonation=datetime.strptime(dateofdonation, '%Y-%m-%d').date()
        today_date = datetime.today().date()
        number_of_dates = (today_date - dateofdonation).days
        count=abs(number_of_dates)
        print("xfcghj",count)
        if count==0:
            reg = Blood_Donation()
            re = Registration.objects.get(id=public.id)
            re.last_donate_date = dateofdonation
            re.save()
            reg.public_id = public.id
            reg.bloodgroup = bloodgroup
            reg.dateofdonation = dateofdonation
            reg.healthissue = healthissue
            reg.save()
            return render(request, 'user/index.html', {'message': "successfully added"})

        elif count<90:
            return render(request, 'user/blood_donation_form.html', {'message': "less than 90 days"})
        else:

            reg = Blood_Donation()
            re = Registration.objects.get(id=public.id)
            re.last_donate_date=dateofdonation
            re.save()
            reg.public_id=public.id
            reg.bloodgroup=bloodgroup
            reg.dateofdonation = dateofdonation
            reg.healthissue=healthissue  
            reg.save()
            return render(request, 'user/index.html', {'message': "successfully added"})

class organ_donation_form(TemplateView):
    template_name='user/organ_donation_form.html'

    def post(self, request, *args, **kwargs):
        public=Registration.objects.get(user_id=self.request.user.id)
        # WillingToDonate = request.POST['willingtodonate']
        PreviousOrganDonate = request.POST['organdonateprevious']
        LastOrganDonationDate = request.POST['lastdonationdate']
        CheckupDate = request.POST['checkupddate']
        Organ = request.POST['organ']
        healthissue = request.POST['healthissue']
        if Organ_Donation.objects.filter(public_id=public.id):
            return render(request, 'user/organ_donation_form.html', {'message': "Already added" })
        else:
            reg = Organ_Donation()# call the model
            reg.public_id=public.id
        # reg.WillingToDonate=WillingToDonate
            reg.PreviousOrganDonate=PreviousOrganDonate
            reg.LastOrganDonationDate=LastOrganDonationDate 
            reg.CheckupDate=CheckupDate
            reg.Organ = Organ
            reg.healthissue=healthissue
            reg.checkupstatus="Checkup Requested"
            
            reg.save()
        # messages.success(request, "Successfully added")  # Add success message
        # return redirect('user:index')
            return render(request, 'user/index.html', {'message': "successfully added" })
class OrganDonorAfterDeath(TemplateView):
    template_name='user/Organdonsubmitafterdeath.html'
    def post(self, request, *args, **kwargs):
        fullName = request.POST['fullName']
        email = request.POST['email']
        phone = request.POST['phone']
        bloodgroup = request.POST['bloodgroup']
        medicalConditions = request.POST['medicalConditions']
        organPreferences = request.POST['organPreferences']

        reg = Pledge_Form()
        reg.bloodgroup=bloodgroup
        reg.fullName=fullName
        reg.phone=phone 
        reg.email=email
        reg.medicalConditions = medicalConditions
        reg.organPreferences=organPreferences
            
        reg.save()
        return render(request, 'user/index.html', {'message': "successfully filled the form"})
class ProfileView(TemplateView):
    template_name='user/profile.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        # id1 = self.request.user.id
        obj = User.objects.get(pk=self.request.user.id)
        pro = Registration.objects.get(user_id=obj.id)
        context['profile'] = pro
        return context
class UpdateProfile(TemplateView):
    template_name = 'user/upd_profile.html'
    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        abc=Registration.objects.get(user_id=self.request.user.id)
        context['profile'] = abc
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']
        phone = request.POST['phone']
        address = request.POST['address']
        age = request.POST['age']
        district = request.POST['district']

        reg = Registration.objects.get(id=id3)  # call the model
        reg.phone = phone
        reg.address = address
        reg.age=age
        reg.district=district
        reg.save()

def MyBloodDonateDetails(request):
    abc=Registration.objects.get(user_id=request.user.id)
    bdd = Blood_Donation.objects.filter(public_id=abc.id)
    context={
        'bdd':bdd
    }
    return render(request,'user/myblooddetails.html',context)
    
    name = request.user.first_name
    messages.warning(request, f"Sorry {name} You have not donated before." )
    return render(request, 'user/message.html')
class BloodDonationEdit(TemplateView):
    template_name = "user/blooddonationedit.html"        
    def get_context_data(self, **kwargs):
        context = super(BloodDonationEdit, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro =  Blood_Donation.objects.get(id=id3)
        context['upd'] = pro
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']
        dateofdonation = request.POST['date']
        healthissue = request.POST['health']
    
        reg = Blood_Donation.objects.get(id=id3)# call the model
        reg.dateofdonation = dateofdonation
        reg.healthissue = healthissue
        reg.save()
        return render(request, 'user/index.html',{'message':"Successfully Profile Edited"})
class BloodDonationDelete(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Blood_Donation.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Deleted"})

def MyOrganDonateDetails(request):
    try:
        abc=Registration.objects.get(user_id=request.user.id)
        pro = Organ_Donation.objects.get(public_id=abc.id)
        context={
            'profile':pro
        }
        return render(request,'user/myorgandetails.html',context)
    except:
        
        name = request.user.first_name
        messages.warning(request, f"Sorry {name} You have not donated before." )
        return render(request, 'user/message.html')
        # return render(request,'user/index.html')
    
        

class ViewAllBloodDonorList(TemplateView):
    template_name='user/viewallblooddonor.html'
    def get_context_data(self, **kwargs):
        view_blood_donor = Blood_Donation.objects.all()
        context = {
            'view_blood_donor':view_blood_donor
        }
     
        bd = Blood_Donation.objects.all()
        context['bd'] = bd
        return context
    
    def post(self, request, *args, **kwargs):
        
        search = self.request.POST['search']
        view_blood_donor = Blood_Donation.objects.filter(bloodgroup__icontains=search)
        
        return render(request,'user/viewallblooddonor.html',{'view_blood_donor':view_blood_donor})
class ViewAllOrganDonorList(TemplateView):
    template_name='user/viewallorgandonation.html'
    def get_context_data(self, **kwargs):
        view_organ_donor = Organ_Donation.objects.all()
        context = {
            'view_organ_donor':view_organ_donor
        }
        bd = Organ_Donation.objects.all()
        context['bd'] = bd
        return context
    
    def post(self, request, *args, **kwargs):
        
        search = self.request.POST['search']
        view_organ_donor = Organ_Donation.objects.filter(Organ__icontains=search)
        
        return render(request,'user/viewallorgandonation.html',{'view_organ_donor':view_organ_donor})

class ViewAllBloodbankDetails(TemplateView):
    template_name='user/viewbloodbankdetails.html'
    def get_context_data(self, **kwargs):
        view_bb = BloodStocks.objects.all()
        context = {
            'view_bb':view_bb
        }
        # bd = Organ_Donation.objects.all()
        # context['bd'] = bd
        return context 
    def post(self, request, *args, **kwargs):
        
        search = self.request.POST['search']
        view_bb = BloodStocks.objects.filter(user_id__location__icontains=search)
        
        return render(request,'user/viewbloodbankdetails.html',{'view_bb':view_bb})
class ViewCheckup(TemplateView):
    template_name="user/viewcheckup.html"
    def get_context_data(self, **kwargs):
        context = super(ViewCheckup, self).get_context_data(**kwargs) 
        abc=Registration.objects.get(user_id=self.request.user.id)
        pro = Organ_Donation.objects.filter(public_id=abc.id,status='Hospital Assigned')
        context['checkup'] = pro  
        return context
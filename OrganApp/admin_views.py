from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from OrganApp.models import UserType,Blood_Donation,Organ_Donation,Pledge_Form,Registration,BloodBank
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='Admin/index.html'

class ViewBloodDonorList(TemplateView):
    template_name='admin/viewBlooddonor.html'
    def get_context_data(self, **kwargs):
        view_blood_donor = Blood_Donation.objects.all()
        context = {
            'view_blood_donor':view_blood_donor
        }
        return context

class ViewOrganDonorList(TemplateView):
    template_name='admin/viewOrgandonor.html'
    def get_context_data(self, **kwargs):
        view_organ_donor = Organ_Donation.objects.all()
        context = {
            'view_organ_donor':view_organ_donor
        }
        return context
class ViewpledgeformList(TemplateView):
    template_name='admin/viewPledgeformlists.html'
    def get_context_data(self, **kwargs):
        view_lists = Pledge_Form.objects.all()
        context = {
            'view_lists':view_lists
        }
        return context

class View_all_users(TemplateView):
    template_name='admin/viewallusers.html'
    def get_context_data(self, **kwargs):
        view_user = Registration.objects.all()
        context = {
            'view_user':view_user
        }
        return context

class RemoveUsers(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Registration.objects.get(id=id).delete()
        return redirect('/admin')
        
class Add_Blood_Bank(TemplateView):
    template_name='admin/add_blood_bank.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']
        password = request.POST['phone']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'admin/index.html' , {'message': "Already added the Username or Email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()

           
            
            reg = BloodBank()
            reg.user = user
            reg.name=name
            reg.phone=phone 
            reg.email=email
            reg.location = location
            reg.password=password
            
                
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "bloodbank"
            usertype.save()
            return render(request, 'admin/index.html', {'message': "Blood Bank Added Successfully"})

class Checkup(TemplateView):
    template_name='admin/view_checkup.html'
   
    def get_context_data(self, **kwargs):
        view_checkup = Organ_Donation.objects.filter(checkupstatus='Checkup Requested')
        context = {
            'view_checkup':view_checkup
        }
        return context
    def post(self, request, *args, **kwargs):
        id=request.POST['id']
        id2=request.POST['id2']
        var=Organ_Donation.objects.get(id=id2)
        hospitalname=request.POST['hospitalname']
        # abc=Problems.objects.get(id=id2)
        var.status='Hospital Assigned'
        var.hospitalname=hospitalname
        var.save()
        return render(request, 'admin/base.html',{'message':"Hospital Assigned"})
    
class View_all_blood_bank(TemplateView):
    template_name='admin/viewbloodbanklist.html'
    def get_context_data(self, **kwargs):
        view_bb = BloodBank.objects.all()
        context = {
            'view_bb':view_bb
        }
        return context


class RemoveBank(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        BloodBank.objects.get(id=id).delete()
        return redirect('/admin')

class editbank(TemplateView):
    template_name='admin/editbank.html'
    def get_context_data(self, **kwargs):
        context = super(editbank, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro =  BloodBank.objects.get(id=id3)
        context['upd'] = pro
        return context
    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']
        name = request.POST['name']
        phone = request.POST['phone']
        location = request.POST['location']
        reg = BloodBank.objects.get(id=id3)# call the model
        reg.name = name
        reg.phone = phone
        reg.location = location
        reg.save()
        return render(request, 'admin/editbank.html',{'message':"Successfully Bank details Updated"})


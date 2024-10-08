from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from OrganApp.models import BloodBank,BloodStocks
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='bloodbank/index.html'
class addblood(TemplateView):
    template_name='bloodbank/addblood.html'
    
    def post(self, request, *args, **kwargs):
        
        xyz=BloodBank.objects.get(user_id=self.request.user.id)
        bloodgroup = request.POST['bloodgroup']
        stock = request.POST['stock']

        reg = BloodStocks()
        
        reg.user_id=xyz.id
        reg.bloodgroup=bloodgroup
        reg.availability=stock
        
            
        reg.save()
        return render(request, 'bloodbank/index.html', {'message': "successfully added"})
class ViewBloodStock(TemplateView):
    template_name='bloodbank/view_bloodstocks.html'
    def get_context_data(self, **kwargs):
        view_stock = BloodStocks.objects.all()
        context = {
            'view_stock':view_stock
        }
        return context
class UpdateBloodStock(TemplateView):
    template_name = "bloodbank/updatestock.html"        
    def get_context_data(self, **kwargs):
        context = super(UpdateBloodStock, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro =  BloodStocks.objects.get(id=id3)
        context['upd'] = pro
        return context
    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']
        stock = request.POST['stock']
        reg = BloodStocks.objects.get(id=id3)# call the model
        reg.availability=stock
        reg.save()  
        return render(request, 'bloodbank/index.html', {'message': "successfully updated"})
class ProfileView(TemplateView):
    template_name='bloodbank/profile.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        # id1 = self.request.user.id
        obj = User.objects.get(pk=self.request.user.id)
        pro = BloodBank.objects.get(user_id=obj.id)
        context['profile'] = pro
        return context

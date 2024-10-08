from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate
from OrganApp.models import UserType,Registration
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.core.mail import EmailMessage

# Create your views here.

class index(TemplateView):
    template_name='index.html'
# class about(TemplateView):
#     template_name='about.html'
# class contact(TemplateView):
#     template_name='contact.html'

class loginview(TemplateView):
    template_name='login.html'
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            if user.is_active == True:
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "bloodbank":
                    return redirect('/bloodbank')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})
        else:
            return render(request, 'index.html', {'message': "Invalid Username or Password"})

class signup(TemplateView):
    template_name='register.html'
    def post(self, request, *args, **kwargs):
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        bloodgroup = request.POST['bloodgroup']
        dob = datetime.strptime(request.POST['dob'], '%Y-%m-%d')
        age = calculate_age(dob)
        district = request.POST['district']
        gender = request.POST['gender']
        password = request.POST['password']
        if not email.endswith('.com'):
            return render(request, 'register.html', {'message': "Invalid email"})
        else:         

            if age < 18:
                return render(request, 'register.html', {'message': "You must be at least 18 years old to register."})

        
            if User.objects.filter(email=email):
                print('pass')
                return render(request, 'register.html' , {'message': "already added the username or email"})
                
            else:
                
                user = User.objects.create_user(username=email, password=password, first_name=fname, email=email,
                                                is_staff=False, is_active=False)
                user.save()

                reg = Registration()# call the model
                reg.user = user

                reg.fname=fname
                reg.lname=lname
                reg.email=email
                reg.phone = phone
                reg.address=address
                reg.district=district
                reg.bloodgroup=bloodgroup
                reg.dob=dob
                reg.gender=gender
                reg.age=age
                reg.password = password
                
                reg.save()
                usertype = UserType()
                usertype.user = user
                usertype.type = "user"
                usertype.save()

                current_site = get_current_site(request)
                mail_subject = 'Activate your account'
                message = render_to_string('activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = email
                email = EmailMessage(mail_subject, message, to=[to_email])
                
                try:
                    email.send()
                except Exception as e:
            # If email sending fails, render an error message
                    return render(request, 'register.html', {'message': f"Error sending activation email: {str(e)}"})

                return render(request, 'verify_email.html', {'email': to_email})

def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'index.html')  # Render a success message after activation
    else:
        return HttpResponse('Activation link is invalid or expired.') 

def update_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        try:
            # Retrieve the user object
            user = User.objects.get(email=email)

            # Set the new password
            user.set_password(new_password)

            # Save the changes
            user.save()
            return render(request, 'password_updated.html')
        except User.DoesNotExist:
            return render(request, 'user_not_found.html')

    return render(request, 'update_password_form.html')
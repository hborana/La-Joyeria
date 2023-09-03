from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dealer_Registration, Jewellery_Info,Category_Info

# Create your views here.
def Vender_Register(request):
    if request.POST:
        obj = Dealer_Registration()
        obj.d_name = request.POST['d_name']
        obj.d_gender = request.POST['d_gender']
        obj.d_email = request.POST['d_email']
        obj.d_dob = request.POST['d_dob']
        obj.d_contact = request.POST['d_contact']
        obj.d_address = request.POST['d_address']
        obj.d_aadharno = request.POST['d_aadharno']
        obj.d_shopName = request.POST['d_shopName']
        obj.d_shopEmail = request.POST['d_shopEmail']
        obj.d_shopAddress = request.POST['d_shopAddress']
        obj.d_shopContact = request.POST['d_shopContact']
        obj.d_country = request.POST['d_country']
        obj.d_state = request.POST['d_state']
        obj.d_city = request.POST['d_city']
        obj.d_pincode = request.POST['d_pincode']
        obj.save()
        return redirect('venderlogin')
    return render(request,'venders/vregi.html')

def Vender_Login(request):
    if request.POST:
        try:
            valid = Dealer_Registration.objects.get(d_email=request.POST['d_email'])
            if valid.d_aadharno == request.POST['d_aadharno']:
                request.session['vender'] = valid.d_aadharno
                return redirect('venderHome')
            else:
                print("enter Valid AAdhar No.")
        except:
            print("Enter Valid Email Id")
    return render(request,'venders/vlogin.html')

def VenderHomePage(request):
    if 'vender' in request.session.keys():
        dr = Dealer_Registration.objects.get(d_aadharno = request.session['vender'])
        ji = Jewellery_Info.objects.filter(Dealers = dr)
        return render(request,'venders/vdashboard.html',{'vdata':dr,'jewel':ji})
    else:
        return redirect('venderlogin')

def Add_New_Jewellery(request):
    if 'vender' in request.session.keys():
        dr = Dealer_Registration.objects.get(d_aadharno = request.session['vender'])
        ci = Category_Info.objects.all()
        if request.POST:
            obj = Jewellery_Info()
            obj.Dealers = dr
            obj.category_name = Category_Info.objects.get(id=request.POST['category_name'])
            obj.j_name = request.POST['j_name']
            obj.j_type = request.POST['j_type']
            obj.j_code = request.POST['j_code']
            obj.j_description = request.POST['j_description']
            obj.j_price = request.POST['j_price']
            obj.j_picture = request.FILES.get('j_picture')
            obj.save()
            return redirect('venderHome')
        return render(request,'venders/ADD_jewellery.html',{'vdata':dr,'catin':ci})
    else:
        return redirect('venderlogin')

def Update_Jewellery(request,id):
    if 'vender' in request.session.keys():
        dr = Dealer_Registration.objects.get(d_aadharno = request.session['vender'])
        ci = Category_Info.objects.all()
        obj = Jewellery_Info.objects.get(id=id)
        if request.POST:
            obj.Dealers = dr
            obj.category_name = Category_Info.objects.get(id=request.POST['category_name'])
            obj.j_name = request.POST['j_name']
            obj.j_type = request.POST['j_type']
            obj.j_code = request.POST['j_code']
            obj.j_description = request.POST['j_description']
            obj.j_price = request.POST['j_price']
            profile = request.FILES.get('j_picture')
            
            if profile == None:
                profile = obj.j_picture
                
            obj.j_picture = profile
            
            obj.save()
            return redirect('venderHome')
        return render(request,'venders/ADD_jewellery.html',{'data':obj,'vdata':dr,'catin':ci})
    else:
        return redirect('venderlogin')
    
def Delete_Jewellery(request,id):
    if 'vender' in request.session.keys():
        obj = Jewellery_Info.objects.get(id=id)
        obj.delete()
        return redirect('venderHome')
    else:
        return redirect('venderlogin')
    
    
def VenderLogout(request):
    if 'vender' in request.session.keys():
        del request.session['vender']
        return redirect('venderlogin')
    else:
        return redirect('venderlogin')
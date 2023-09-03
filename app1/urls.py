from django.urls import path

from . import views as v

urlpatterns = [
    path('',v.Vender_Register),
    path("Dealer_Login/",v.Vender_Login,name='venderlogin'),
    path("Dealer_DashBoard/",v.VenderHomePage,name='venderHome'),
    path('venderlogout/',v.VenderLogout,name='venderlogout'),
    path('Add_New_Jewellery/',v.Add_New_Jewellery,name='AddNewJewellery'),
    path('Update_Jewellery/<int:id>',v.Update_Jewellery,name='Update_Jewellery'),
    path('Delete_Jewellery/<int:id>',v.Delete_Jewellery,name='Delete_Jewellery'),
]

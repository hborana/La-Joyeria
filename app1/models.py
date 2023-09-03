from django.db import models

# Create your models here.
class Customer_Info(models.Model):
    c_name = models.CharField(max_length=200,default="")
    c_contact = models.CharField(max_length=200,default="")
    c_address = models.TextField(default="")
    c_email = models.EmailField(max_length=200,default="")
    c_country = models.CharField(max_length=100,default="")
    c_state = models.CharField(max_length=100,default="")
    c_city = models.CharField(max_length=100,default="")
    c_pincode = models.CharField(max_length=100,default="")
    c_dob = models.DateField(auto_now=False, blank=True, null=True)
    c_password = models.EmailField(max_length=200,default="")
    
    def __str__(self):
        return self.c_name

class Admin_Info(models.Model):
    Admin_name = models.CharField(max_length=200,default="")
    Admin_contact = models.CharField(max_length=200,default="")    
    Admin_email = models.EmailField(max_length=200,default="")
    Admin_password = models.EmailField(max_length=200,default="")

    def __str__(self):
        return self.Admin_name

class Dealer_Registration(models.Model):
    d_name = models.CharField(max_length=200,default="")
    d_gender = models.CharField(max_length=200,default="")
    d_email = models.EmailField(max_length=200,default="")
    d_dob = models.DateField(auto_now=False, blank=True, null=True)
    d_contact = models.CharField(max_length=200,default="")
    d_address = models.TextField(default="")
    d_aadharno = models.CharField(max_length=100,default="")
    d_shopName = models.CharField(max_length=200,default="")
    d_shopEmail = models.EmailField(max_length=200,default="")
    d_shopAddress = models.TextField(default="")
    d_shopContact = models.CharField(max_length=200,default="")
    d_country = models.CharField(max_length=100,default="")
    d_state = models.CharField(max_length=100,default="")
    d_city = models.CharField(max_length=100,default="")
    d_pincode = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.d_name
    

class Category_Info(models.Model):
    category_name = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.category_name

class Jewellery_Info(models.Model):
    Dealers = models.ForeignKey('Dealer_Registration', on_delete=models.CASCADE,blank=True, null=True)
    category_name = models.ForeignKey('Category_Info', on_delete=models.CASCADE,blank=True, null=True)
    j_name = models.CharField(max_length=200,default="")
    j_type = models.CharField(max_length=200,default="")
    j_code = models.CharField(max_length=200,default="")
    j_description = models.TextField(default="")
    j_price = models.CharField(max_length=200,default="")
    j_picture = models.ImageField(upload_to="Images/", max_length=300,default="")
    
    def __str__(self):
        return self.j_name  

class Order_Info(models.Model):
    Customer_Info = models.ForeignKey('Customer_Info', on_delete=models.CASCADE,blank=True, null=True)
    Jewellery_Info = models.ForeignKey('Jewellery_Info', on_delete=models.CASCADE,blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    netPrice = models.CharField(max_length=200,default="")
    date_Time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.BooleanField(default=False)
    shippingDetails = models.CharField(max_length=200,default="")
    order_No = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.Jewellery_Info.j_name
    
class Cart_Info(models.Model):
    Jewellery_Info = models.ForeignKey('Jewellery_Info', on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self):
        return self.Jewellery_Info.j_name
    
class Payment_Info(models.Model):
    Customer_Info = models.ForeignKey('Customer_Info', on_delete=models.CASCADE,blank=True, null=True)
    Jewellery_Info = models.ForeignKey('Jewellery_Info', on_delete=models.CASCADE,blank=True, null=True)
    Dealers = models.ForeignKey('Dealer_Registration', on_delete=models.CASCADE,blank=True, null=True)
    payment_type = models.CharField(max_length=200,default="")
    pay_cardNo = models.CharField(max_length=200,default="")
    pay_amount = models.CharField(max_length=200,default="")
    pay_totalAmount = models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.payment_type

class Invoice(models.Model):
    Customer_info = models.ForeignKey('Customer_Info', on_delete=models.CASCADE,blank=True, null=True)
    Dealers = models.ForeignKey('Dealer_Registration', on_delete=models.CASCADE,blank=True, null=True)
    Jewellery_info = models.ForeignKey('Jewellery_Info', on_delete=models.CASCADE,blank=True, null=True)
    Payment_info = models.ForeignKey('Payment_Info', on_delete=models.CASCADE,blank=True, null=True)
    
class Wishlist(models.Model):
    Jewellery_Info = models.ForeignKey('Jewellery_Info', on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self):
        return self.Jewellery_Info.j_name

class Feedback(models.Model):
    Jewellery_Info = models.ForeignKey('Jewellery_Info', on_delete=models.CASCADE,blank=True, null=True)
    Customer_info = models.ForeignKey('Customer_Info', on_delete=models.CASCADE,blank=True, null=True)
    Rate = models.PositiveIntegerField(default=0)
    comments = models.TextField(default="")
    
    
    
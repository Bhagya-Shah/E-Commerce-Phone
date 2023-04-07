from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
# Create your models here.
#overwrite django ka inbuild vala model

from django.contrib.auth.models import User
from base.models import BaseModel
from base.emails import send_account_activation_email
from products.models import Product,ColorVariant,SizeVariant


class Profile(BaseModel):
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True, blank=True)
    profile_image=models.ImageField(upload_to="profile")

    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid=False,cart__user=self.user).count()


class Cart(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='carts')
    is_paid=models.BooleanField(default=False)


class CartItems(BaseModel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    color_variant=models.ForeignKey(ColorVariant,on_delete=models.SET_NULL,null=True,blank=True)
    size_variant=models.ForeignKey(SizeVariant,on_delete=models.SET_NULL,null=True,blank=True)

@receiver(post_save , sender = User)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)





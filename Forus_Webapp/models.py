from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

class register(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)
	
class register1(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)
	
class empreg1(models.Model):
	name=models.CharField(max_length=60)
	email=models.CharField(max_length=60)
	password=models.CharField(max_length=60)
	rpassword=models.CharField(max_length=60)
	dob=models.CharField(max_length=60)
	gender=models.CharField(max_length=60)
	phno=models.CharField(max_length=60)


class stock_bin1(models.Model):
	bin_card=models.CharField(max_length=60,default=0)
	ERP_NO=models.CharField(max_length=60,default=0)
	MP_NO=models.CharField(max_length=60,default=0)
	str=models.CharField(max_length=60,default=0)
	devr1=models.CharField(max_length=60,default=0)
	rkr=models.CharField(max_length=60,default=0)
	shelf=models.CharField(max_length=60,default=0)
	binr=models.CharField(max_length=60,default=0)
	item=models.CharField(max_length=60,default=0)
	date=models.CharField(max_length=60,default=0)
	pb=models.CharField(max_length=60,default=0)
	desc=models.CharField(max_length=60,default=0)
	no_received=models.CharField(max_length=60,default=0)
	no_issue=models.CharField(max_length=60,default=0)
	sb=models.CharField(max_length=60,default=0)
	rdno=models.CharField(max_length=60,default=0)
	remarks=models.CharField(max_length=60,default='remark')



class stock(models.Model):
	bin_card=models.IntegerField(default=1)
	ERP_NO=models.CharField(max_length=60)
	MP_NO=models.CharField(max_length=60,default=0)
	str=models.CharField(max_length=60)
	devr1=models.CharField(max_length=60)
	rkr=models.CharField(max_length=60)
	shelf=models.CharField(max_length=60,default=0)
	binr=models.CharField(max_length=60)
	item=models.CharField(max_length=60,default=0)
	date=models.CharField(max_length=60)
	pb=models.CharField(max_length=60,default=0)
	desc=models.CharField(max_length=60)
	no_received=models.CharField(max_length=60,default=0)
	no_issue=models.CharField(max_length=60,default=0)
	sb=models.CharField(max_length=60,default=0)
	rdno=models.CharField(max_length=60,default=0)
	remarks=models.CharField(max_length=60,default='remark')
	

class store_room(models.Model):
	str=models.CharField(max_length=60)
	rkr=models.CharField(max_length=60)
	devr1=models.CharField(max_length=60)
	shelf=models.CharField(max_length=60,default='shelf1')
	binr=models.CharField(max_length=60)




class additem(models.Model):
	name=models.CharField(max_length=60)
	total=models.CharField(max_length=60)
	pd=models.CharField(max_length=60,default=1)
	Rece=models.CharField(max_length=60,default=1)
	Iss=models.CharField(max_length=60,default=1)
	cd=models.CharField(max_length=60,default=1)
	db=models.CharField(max_length=60,default=1)
	rm1=models.CharField(max_length=60,default=1)

class deviceitem(models.Model):
	device_id=models.CharField(max_length=60,default=1)
	name=models.CharField(max_length=60)
	Previous_Date=models.CharField(max_length=60,default=1)
	Previous_Balance=models.CharField(max_length=60,default=1)
	Received=models.CharField(max_length=60,default=1)
	Issued=models.CharField(max_length=60,default=1)
	Current_Date=models.CharField(max_length=60,default=1)
	Device_Balance=models.CharField(max_length=60,default=1)
	Remarks=models.CharField(max_length=60,default=1)

	

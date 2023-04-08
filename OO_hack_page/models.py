import django.contrib.auth.backends
from django.contrib.postgres.fields import DateRangeField
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import datetime

types = [
    ('LV', 'Жилое помещение'),
    ('NL', 'Нежилое помещение'),
    ('AP', 'Квартира'),
    ('EH', 'Доходный дом'),
    ('MH', 'Общежитие'),
    ('HO', 'Отель'),
    ('GH', 'Дом престарелых'),
    ('ST', 'Склад'),
    ('SR', 'Стрит-ретейл'),
    ('OF', 'Офис'),
    ('SM', 'Супермаркет'),
    ('TC', 'Торговый центр'),
    ('OR', 'Другое')
]

status = [
    ('EX', 'Введено в экспаутацию'),
    ('NC', 'Незавершенное строительство'),
    ('NR', 'Требует реконструкции'),
    ('NE', 'Не в ведено в эксплаутацию'),
    ('DE', 'Назначено под снос'),
    ('NA', 'Статус не определен'),
]

TF = [
    ('FL','Нет'),
    ('TR','Да'),
]

metro = [
    ('m','M^2'),
    ('g','Gect'),
]

wall = [
    ('bet','Beton'),
    ('Woo','Wood'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", default='None')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)


class Owner(models.Model):
    name = models.CharField()


class REstate(models.Model):
    object_state = models.CharField()
    object_dist = models.CharField()
    object_adress = models.CharField()
    object_type = models.CharField(choices=types, default='OR')
    object_status = models.CharField(choices=status, default='NA')
    object_square = models.DecimalField(max_digits=9, decimal_places=2)
    object_owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    object_client = models.CharField()
    object_photo = ArrayField(models.CharField(blank= True),blank= True)
    object_video = ArrayField(models.CharField(blank= True),blank= True)
    object_inRec = models.CharField(choices=TF,default= 'FL')
    object_LetterADO = models.IntegerField(blank= True)
    object_LetterDate = models.DateField(blank= True)
    object_HandCorr = models.CharField(choices=TF,default= 'FL')
    object_HandCorrCom = models.CharField(blank=True)
    object_Chekers = models.CharField()
    object_viewing = models.CharField()
    object_addition = models.CharField(blank= True)
    object_objectCount = models.IntegerField(default= 1)
    object_demont = models.CharField(choices= TF,default='FL')
    object_demontConf = models.DateField(blank= True)
    object_demontWorker = models.CharField(blank= True)
    object_Comment = models.CharField(blank= True)
    object_religion = models.CharField(choices= TF,default='FL')
    object_OKN = models.CharField(choices= TF,default='FL')
    object_metro = models.CharField(choices= metro,default='m')
    object_sqareBTI = models.DecimalField(max_digits=9, decimal_places=2,blank=True)
    object_sqareSelfBuild = models.DecimalField(max_digits=9, decimal_places=2)
    object_negativC = models.IntegerField(default=0)
    object_yearST = models.DateField()
    object_yearSP = models.DateField()
    object_sqareSpot = models.DecimalField(max_digits=9, decimal_places=2,blank=True)
    object_hight = models.DecimalField(max_digits=9, decimal_places=2,blank=True)
    object_WallMat = models.CharField(choices= wall,default='bet')
    object_conts = models.CharField()



class Workgroup(models.Model):
    group_name = models.CharField()
    group_spec = models.CharField()
    group_head = models.CharField()
    group_type = models.CharField()
    group_OIV = models.CharField()

class Workgroup_time(models.Model):
    workgroup = models.CharField(primary_key=Workgroup)
    object_ES = models.ForeignKey('REstate', on_delete=models.CASCADE)
    task = models.CharField()
    date_start = models.DateField()
    date_end = models.DateField()

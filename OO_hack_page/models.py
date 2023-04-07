from django.db import models

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
    ('OR','Другое')
]
status = [
    ('EX', 'Введено в экспаутацию'),
    ('NC', 'Незавершенное строительство'),
    ('NR', 'Требует реконструкции'),
    ('NE', 'Не в ведено в эксплаутацию'),
    ('DE', 'Назначено под снос'),
    ('NA', 'Статус не определен'),
]
class Owner(models.Model):
    name = models.CharField()

class REstate(models.Model):
    object_state = models.CharField()
    object_dist = models.CharField()
    object_adress = models.CharField()
    object_type = models.CharField(choices=types,default= 'OR')
    object_status = models.CharField(choices=status,default= 'NA')
    object_square = models.DecimalField(max_digits=9,decimal_places=2)
    object_owner = models.ForeignKey('Owner',on_delete= models.CASCADE)
    object_client = models.CharField()
    object_photo = models.CharField()
    object_video = models.CharField()

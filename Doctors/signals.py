# from django.db.models.signals import post_save
# from django.contrib.auth.models import User, Group
# from .models import Doctor

# def customer_profile(sender, instance, created, **kwargs):
#     if created:    
#         group = Group.objects.get(name='doctor')
# 		instance.groups.add(group)
#         Doctor.objects.create(
# 			user=instance,
# 			name=instance.username,
# 			)
#         print('Profile created')

# post_save.connect(customer_profile, sender=User)
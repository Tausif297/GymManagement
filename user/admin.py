from django.contrib import admin
from .models import Contact, Plans, Member
# Register your models here.
class PlansAdmin(admin.ModelAdmin):
    list_display=['id','plan_name','plan_price','plan_desc','plan_slogan']

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','number','message']

class MemberAdmin(admin.ModelAdmin):
    list_display=['id','username','contact_1','contact_2','email','plans']   

admin.site.register(Plans,PlansAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Member,MemberAdmin)
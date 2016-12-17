from django.contrib import admin

# Register your models here.
from models import Articles, Action, Room, Image, Serv_Image, Reviews, Service, Room_ind, Date
from image_cropping import ImageCroppingMixin

admin.site.register(Articles)
admin.site.register(Room_ind)
admin.site.register(Date)

class InlineImage(admin.TabularInline):
    model = Image

class InlineServImage(admin.TabularInline):
    model = Serv_Image

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
	pass

class CelebrityAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [InlineImage]
    pass

class CelebrityServAdmin(ImageCroppingMixin, admin.ModelAdmin):
    inlines = [InlineServImage]
    pass

admin.site.register(Action, MyModelAdmin)
admin.site.register(Reviews, MyModelAdmin)
admin.site.register(Room, CelebrityAdmin)
admin.site.register(Service, CelebrityServAdmin)
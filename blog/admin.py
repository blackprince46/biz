from django.contrib import admin
from blog.models import (
            UserType, Company, Category, SubCategory, Blog, BloggerLogin, BlogSeo
            )

# Register your models here.


class UserTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserType, UserTypeAdmin)


class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Company, CompanyAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(SubCategory, SubCategoryAdmin)


class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)


class BlogLoginAdmin(admin.ModelAdmin):
    pass

admin.site.register(BloggerLogin, BlogLoginAdmin)


class BlogSeoAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogSeo, BlogSeoAdmin)








from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from django.utils.html import escape
from django.core.urlresolvers import reverse
from .models import Contact, User
from .forms import UserCreationAdminForm


# class LogEntryAdmin(admin.ModelAdmin):

#     date_hierarchy = 'action_time'

#     readonly_fields = LogEntry._meta.get_all_field_names()

#     list_filter = [
#         'user',
#         'content_type',
#         'action_flag'
#     ]

#     search_fields = [
#         'object_repr',
#         'change_message'
#     ]

#     list_display = [
#         'action_time',
#         'user',
#         'content_type',
#         'object_link',
#         'action_flag',
#         'change_message',
#     ]

#     def has_add_permission(self, request):
#         return False

#     def has_change_permission(self, request, obj=None):
#         return request.user.is_superuser and request.method != 'POST'

#     def has_delete_permission(self, request, obj=None):
#         return False

#     def object_link(self, obj):
#         if obj.action_flag == DELETION:
#             link = escape(obj.object_repr)
#         else:
#             ct = obj.content_type
#             link = u'<a href="%s">%s</a>' % (
#                 reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
#                 escape(obj.object_repr),
#             )
#         return link
#     object_link.allow_tags = True
#     object_link.admin_order_field = 'object_repr'
#     object_link.short_description = u'object'

#     def queryset(self, request):
#         return super(LogEntryAdmin, self).queryset(request).prefetch_related('content_type')


class UserCustomAdmin(UserAdmin):
    """
    User CMS. We need to change the add form because we use out custom User model.
    """
    add_form = UserCreationAdminForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Lainnya'), {'fields': ('role', 'gender', 'facebook', 'twitter', 'about_me')}),
    )


class ContactAdmin(admin.ModelAdmin):
    model = Contact

    list_display = ['name', 'address', 'telephone', 'email', 'message']

    search_fields = ['name', 'email', 'message']

admin.site.register(User, UserCustomAdmin)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(LogEntry, LogEntryAdmin)
admin.site.unregister(Site)

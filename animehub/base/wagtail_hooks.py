from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import Expert, ExpertReview, Contact

'''
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see http://kave.github.io/general/2015/12/06/wagtail-streamfield-icons.html

This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at http://fontawesome.io/icons/.
'''


class ExpertModelAdmin(ModelAdmin):
    model = Expert
    # menu_label = 'People'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-users'  # change as required
    list_display = ('first_name', 'last_name', 'job_title', 'thumb_image')


class ExpertReviewModelAdmin(ModelAdmin):
    model = ExpertReview


class ContactsModelAdmin(ModelAdmin):
    model = Contact
    menu_icon = 'fa-map-marker'
    list_display = ('title', 'formatted_address', 'work_time', 'phone', 'site_link')


class SophienWandAdminGroup(ModelAdminGroup):
    menu_label = 'Sophien Wald'
    menu_icon = 'fa-suitcase'  # change as required
    menu_order = 300  # will put in 4th place (000 being 1st, 100 2nd)
    items = (ExpertModelAdmin, ExpertReviewModelAdmin, ContactsModelAdmin)


modeladmin_register(SophienWandAdminGroup)

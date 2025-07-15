from django.contrib import admin
from .models import (
    Profile, Education, Certification, SkillCategory, Skill, 
    Experience, ProjectCategory, Project, Award, 
    ContactMessage, BackgroundImage
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'years_experience')
    search_fields = ('name', 'title', 'email')
    list_filter = ('years_experience',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'title', 'short_bio', 'long_bio')
        }),
        ('Contact Info', {
            'fields': ('email', 'phone', 'address', 'resume')
        }),
        ('Social Media', {
            'fields': ('linkedin', 'github', 'twitter', 'kaggle', 'medium','orcid')
        }),
        ('Images & Others', {
            'fields': ('years_experience', 'profile_image', 'about_image', 'current_project', 'project_description')
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'field_of_study', 'institution', 'start_year', 'end_year' )
    search_fields = ('degree', 'field_of_study', 'institution')
    list_filter = ('start_year', 'end_year')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuing_organization', 'issue_date',  )
    search_fields = ('name', 'issuing_organization', 'credential_id')
    list_filter = ('issue_date',  )

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'color_scheme')
    list_editable = ('icon_class', 'color_scheme')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.site_header = "Portfolio Admin"

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'currently_working',  )
    search_fields = ('position', 'company')
    list_filter = ('currently_working', 'start_date')

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'completion_date', 'is_featured')
    search_fields = ('title', 'short_description')
    list_filter = ('category', 'is_featured', 'completion_date')
    filter_horizontal = ('technologies',)
    readonly_fields = ('display_technologies',)
    
    def display_technologies(self, obj):
        return ", ".join([tech.name for tech in obj.technologies.all()])
    display_technologies.short_description = 'Technologies'

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'issue_date',  )
    search_fields = ('title', 'issuing_organization')
    list_filter = ('issue_date',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_editable = ('is_read',)

@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('name',)
    list_filter = ('is_active',)
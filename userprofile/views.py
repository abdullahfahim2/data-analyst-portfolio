from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import ContactForm

def index(request):
    # Get all data needed for the single page
    profile = Profile.objects.first()
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').order_by('id')
    experiences = Experience.objects.all()
    project_categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    featured_projects = projects.filter(is_featured=True)
    awards = Award.objects.all()
    background_images = BackgroundImage.objects.filter(is_active=True).order_by('order')
    
    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!Thank You!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form.')
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'educations': educations,
        'certifications': certifications,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'project_categories': project_categories,
        'projects': projects,
        'featured_projects': featured_projects,
        'awards': awards,
        'background_images': background_images,
        'form': form,
    }
    
    return render(request, 'profile/index.html', context)

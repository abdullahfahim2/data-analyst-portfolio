from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100,blank=True, null=True)
    short_bio = models.TextField(blank=True, null=True)
    long_bio = RichTextField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    years_experience = models.PositiveIntegerField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/',blank=True, null=True)
    about_image = models.ImageField(upload_to='about/',blank=True, null=True)
    current_project = models.CharField(max_length=100,blank=True, null=True)
    project_description = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/',blank=True, null=True)
    
    # Social links
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    kaggle = models.URLField(blank=True, null=True)
    medium = models.URLField(blank=True, null=True)
    orcid = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=100,blank=True, null=True)
    field_of_study = models.CharField(max_length=100,blank=True, null=True)
    institution = models.CharField(max_length=200,blank=True, null=True)
    start_year = models.PositiveIntegerField(blank=True, null=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.institution}"

class Certification(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    issuing_organization = models.CharField(max_length=200,blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class SkillCategory(models.Model):
    ICON_CHOICES = [
        ('fas fa-chart-pie', 'Chart Pie'),
        ('fas fa-robot', 'Robot'),
        ('fas fa-database', 'Database'),
        ('fas fa-cloud', 'Cloud'),
        ('fas fa-code', 'Code'),
        ('fas fa-chart-bar', 'Chart Bar'),
        ('fas fa-brain', 'AI'),
        ('fas fa-server', 'Server'),
        ('fas fa-network-wired', 'Network'),
        ('fas fa-laptop-code', 'Development'),
    ]

    COLOR_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('purple', 'Purple'),
        ('orange', 'Orange'),
        ('red', 'Red'),
        ('yellow', 'Yellow'),
    ]
    name = models.CharField(max_length=100)
    icon_class = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        default='fas fa-code'
    )
    color_scheme = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default='blue'
    )
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
        
    def __str__(self):
        return f"{self.name}"

class Experience(models.Model):
    position = models.CharField(max_length=100,blank=True, null=True)
    company = models.CharField(max_length=100,blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(default=False)
    description = RichTextField()
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class ProjectCategory(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('DA', 'Data Analysis'),
        ('ML', 'Machine Learning'),
        ('WEB', 'Web Development'),
    ]
    name = models.CharField(max_length=5,choices=PROJECT_TYPE_CHOICES, default='DA')
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True)
    short_description = models.TextField(blank=True, null=True)
    detailed_description = RichTextField()
    featured_image = models.ImageField(upload_to='projects/',blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    # Technologies used (many-to-many with Skill model)
    technologies = models.ManyToManyField(Skill)
    
    def __str__(self):
        return self.title

class Award(models.Model):
    ICON_CHOICES = [
        ('fas fa-trophy', 'Trophy'),
        ('fas fa-award', 'Award'),
        ('fas fa-medal', 'Medal'),
        ('fas fa-certificate', 'Certificate'),
        ('fas fa-star', 'Star'),
    ]
    
    COLOR_CHOICES = [
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('purple', 'Purple'),
        ('red', 'Red'),
    ]
    
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon_class = models.CharField(
        max_length=20,
        choices=ICON_CHOICES,
        default='fas fa-award'
    )
    color = models.CharField(
        max_length=10,
        choices=COLOR_CHOICES,
        default='blue'
    )
    
    def __str__(self):
        return self.title
    
    def get_icon_color(self):
        return self.color

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class BackgroundImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='backgrounds/')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name    


# Step 1: Extend the User Model with a UserProfile
# Create a UserProfile model that includes a role field with predefined roles. This model should be linked to Django’s built-in User model with a one-to-one relationship.

# Fields Required:
# user: OneToOneField linked to Django’s User.
# role: CharField with choices for ‘Admin’, ‘Librarian’, and ‘Member’.
# Automatic Creation: Use Django signals to automatically create a UserProfile when a new user is registered.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Step 2: Create a Signal to Automatically Create UserProfile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Step 2: Set Up Role-Based Views
# Create three separate views to manage content access based on user roles:

# Views to Implement:

# An ‘Admin’ view that only users with the ‘Admin’ role can access, the name of the file should be admin_view
# A ‘Librarian’ view accessible only to users identified as ‘Librarians’. The file should be named librarian_view
# A ‘Member’ view for users with the ‘Member’ role, the name of the file should be member_view
# Access Control:

# Utilize the @user_passes_test decorator to check the user’s role before granting access to each view.
from django.contrib.auth.decorators import user_passes_test
def is_admin(user):
    return user.is_authenticated and user.profile.role == 'Admin'
def is_librarian(user):
    return user.is_authenticated and user.profile.role == 'Librarian'
def is_member(user):
    return user.is_authenticated and user.profile.role == 'Member'  
@user_passes_test(is_admin)
def admin_view(request):
    # Admin-specific logic here
    pass
@user_passes_test(is_librarian)
def librarian_view(request):
    # Librarian-specific logic here
    pass    
@user_passes_test(is_member)
def member_view(request):
    # Member-specific logic here
    pass




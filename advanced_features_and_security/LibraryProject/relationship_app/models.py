from django.db import models

# Step 1: Extend the Book Model with Custom Permissions
# Add custom permissions to the Book model to specify who can add, edit, or delete the entries.

# Model Changes Required:
# Inside the Book model, define a nested Meta class.
# Within this Meta class, specify a permissions tuple that includes permissions like can_add_book, can_change_book, and can_delete_book.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')


    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]


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




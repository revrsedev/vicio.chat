from django.db import models
from django.utils import timezone

class HomeCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='home_category_images/')
    link = models.CharField(max_length=200)  # Now just a relative path
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class RecommendedChatRoom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='recommended_chat_rooms/')
    link = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='chatrooms/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='subcategories/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class ChatRoomLatam(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='chatroomslatam/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class SubCategoryLatam(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='subcategorieslatam/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class ChatRoomOcio(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='chatroomsocio/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class SubCategoryOcio(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='subcategoriesocio/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class SubCategoryParaguay(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='subcategoriesparaguay/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class SubCategoryArgentina(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='subcategoriesargentina/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class SubCategoryDev(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='subcategoriesdev/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

class ChatRoomDev(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='chatroomdev/')
    url = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)  # Add this line
    #popularity = models.IntegerField(default=0)  # New field to track popularity

    def __str__(self):
        return self.name

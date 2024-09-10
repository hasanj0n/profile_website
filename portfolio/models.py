from django.db import models

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to="picture/")
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to="picture/")
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career
    
# PROFILE
class Profile(models.Model):
    about = models.ForeignKey(About,
                              on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)
    


# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)



# PORTFOLIO SECTION

class Portfolio(models.Model):
    project_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="portfolio/")
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Portfolio {self.id}'

    
# CONTACT SECTION

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name  # This will display the name in the admin panel





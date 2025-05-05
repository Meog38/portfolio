from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']

class Profile(models.Model):
    name = models.CharField(max_length=200, default="Maria Eduarda Oliveira Galdino")
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    use_default_photo = models.BooleanField(default=True, help_text="Use a imagem padrão em vez de fazer upload")
    bio = models.TextField(default="Prazer, eu me chamo Maria Eduarda, curso ciencia da computacao no insper e tenho entusiasmo por programação e desejo crescer profissionalmente no setor de tecnologia.")
    email = models.EmailField(default="meog38@gmail.com")
    phone = models.CharField(max_length=20, default="28999049728")
    github = models.URLField(default="https://github.com/Meog38")
    linkedin = models.URLField(default="https://www.linkedin.com/in/meog38/")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Profile"
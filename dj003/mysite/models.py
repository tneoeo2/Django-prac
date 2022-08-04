from django.db import models

# Create your models here.
  
 
# class Member(models.Model):
#     id = models.CharField(db_column='ID', max_length=16, primary_key=True)  # Field name made lowercase.
#     pw = models.CharField(db_column='PW', max_length=20)  # Field name made lowercase.
#     date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.
#     permit = models.PositiveIntegerField(db_column='PERMIT', blank=True, null=True)  # Field name made lowercase.
 
  
# class Post(models.Model):
#     number = models.AutoField(db_column='NUMBER', primary_key=True)  # Field name made lowercase.
#     title = models.CharField(db_column='TITLE', max_length=150)  # Field name made lowercase.
#     content = models.TextField(db_column='CONTENT')  # Field name made lowercase.
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#     id = models.CharField(db_column='ID', max_length=20)  # Field name made lowercase.
#     password = models.CharField(db_column='PASSWORD', max_length=20)  # Field name made lowercase.
#     pub_date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.
#     user = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
#     hit = models.PositiveIntegerField(db_column='HIT')  # Field name made lowercase.
    
#     def __str__(self):
#       return self.title
  
# class Photo(models.Model):
#   post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#   image = models.ImageField(upload_to='images/', blank=True, null=True)
  
    
# class Comment(models.Model):
#     number = models.AutoField(db_column='NUMBER', primary_key=True)  # Field name made lowercase.
#     board_number = models.PositiveIntegerField(db_column='BOARD_NUMBER')  # Field name made lowercase.
#     id = models.CharField(db_column='ID', max_length=20)  # Field name made lowercase.
#     content = models.TextField(db_column='CONTENT')  # Field name made lowercase.
#     date = models.DateTimeField(db_column='DATE')  # Field name made lowercase
#     parent_number = models.ForeignKey(Post, db_column='PARENT_NUMBER', on_delete=models.CASCADE, null=False)  # Field name made lowercase.
#     # parent_number = models.PositiveIntegerField(db_column='PARENT_NUMBER')  # Field name made lowercase.
    


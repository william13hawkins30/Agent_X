from django.db import models

# Create your models here.
#  name of parent class = models.ForeignKey(parent class, on_delete=models.CASCADE)
#replace parent class with the name of the model it inheirits from ß

class Users(models.Model):
    Users_name = models.CharField(max_length=200,null=False)
    Users_email = models.CharField(max_length=200,null=False)
    Users_password = models.CharField(max_length=200,null=False)
    Users_id = models.IntegerField(null=False)
    Users_about = models.CharField(max_length=200,null=False)
    Users_location = models.CharField(max_length=200,null=False)
    Users_years_of_experience = models.IntegerField(null=False)

class Form(models.Model):
    Form_id = models.IntegerField(null=False)
    Form_class = models.CharField(max_length=200,null=False)

class Talent(models.Model):
    Talent_id = models.IntegerField(null=False)

class Employer(models.Model):
    Employer_id = models.CharField(max_length=200,null=False)
    Employer_about = models.CharField(max_length=200,null=False)
    Employer_location = models.CharField(max_length=200,null=False)
    Employer_looking_for = models.CharField(max_length=200,null=False)

class Available_projects(models.Model):
    Available_projects_id = models.IntegerField(null=False)

#example of inhertance------------------------------------
class Available_projects_has_Employers(models.Model):
    Available_projects_has_Employers = models.IntegerField(null=False)
    Available_projects_has_Employers = models.ForeignKey(Employers, on_delete=models.CASCADE)

class user_has_form(models.Model):
    User_id = models.IntegerField(null=False)
    Form_id = models.IntegerField(null=False)

class user_has_Welcome(models.Model):
    user_id = models.IntegerField(null=False)
    welcome_id = models.IntegerField(null=False)
    user_has_Welcome = models.ForeignKey(Welcome, on_delete=models.CASCADE)

class Employers_has_user(models.Model):
    Employers_idEmployers = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    Employers_has_user = models.ForeignKey(user, on_delete=models.CASCADE)

class Talent_has_user(models.Model):
    Talent_idTalent = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    Talent_has_user = models.ForeignKey(user, on_delete=models.CASCADE)

class sign_up(models.Model):
    idsign up

 


from django.db import models

class Departments(models.Model):
    Department= models.CharField(max_length=200)
    def __str__(self):
        return self.Department

class Course(models.Model):
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    def __str__(self):
        return self.course

class Entity(models.Model):
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    entity = models.CharField(max_length=200,default="Student")
    entityname = models.CharField(max_length=200)
    rollno=models.IntegerField(default=0)
    def __str__(self):
        return self.entityname

class Login(models.Model):
    name= models.ForeignKey(Entity, on_delete=models.CASCADE)
    username= models.CharField(max_length=200,default="")
    password= models.CharField(max_length=200)
    entity= models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Subjects(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    def __str__(self):
        return self.subject

class attendance(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    rollno = models.IntegerField(default=0)
    attended=models.IntegerField(default=0)
    totalclasses=models.IntegerField(default=0)

class exam(models.Model):
    Department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    ExamName = models.CharField(max_length=200)
    question = models.CharField(max_length=1000)

class Marks(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    exam=models.ForeignKey(exam, on_delete=models.CASCADE)
    rollno = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)




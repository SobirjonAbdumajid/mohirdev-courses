from django.db import models


class Teacher(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    Universities = (
        ('university pdp', 'PDP university'),
        ('university oxford', 'Oxford university')
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=15, choices=GENDER)
    graded_university = models.CharField(max_length=150, choices=Universities)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        db_table = 'Teacher'


class Experience(models.Model):
    company = models.CharField(max_length=150)
    year = models.PositiveIntegerField()



    def __str__(self):
        return f"{self.year} experience in {self.company}"

    class Meta:
        db_table = 'Experience'


class TeacherInfo(models.Model):
    TeacherEXP = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='Teacher_info')
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='Teacher_info')
    # TeachingEXP = models.DateField()

    def __str__(self):
        return f"{self.TeacherEXP} for {self.Teacher}"

    class Meta:
        db_table = 'TeacherInfo'
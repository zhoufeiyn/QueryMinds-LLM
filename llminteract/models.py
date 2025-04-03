from django.db import models

# Create your models here.
class ExerciseLlm(models.Model):
    id_exercise_llm = models.AutoField(primary_key=True)
    f_weight = models.DecimalField(max_digits=5, decimal_places=2)
    d_deadline = models.DateField()
    id_difficultylevel = models.IntegerField(blank=True, null=True)
    n_max_attempts = models.IntegerField(blank=True, null=True)
    topic = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EXERCISE_LLM'


class StudentEvaluationLlm(models.Model):
    id_student = models.IntegerField(primary_key=True)
    id_exercise_llm = models.ForeignKey(ExerciseLlm, models.DO_NOTHING, db_column='id_exercise_llm')
    f_score = models.DecimalField(max_digits=5, decimal_places=2)
    d_begins = models.DateField(blank=True, null=True)
    d_finish = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STUDENT_EVALUATION_LLM'
        unique_together = (('id_student', 'id_exercise_llm'),)

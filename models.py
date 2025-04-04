# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answer(models.Model):
    id_answer = models.AutoField(primary_key=True)  # The composite primary key (id_answer, id_student, id_exercise) found, that is not supported. The first column is selected.
    id_student = models.ForeignKey('Student', models.DO_NOTHING, db_column='id_student')
    id_exercise = models.ForeignKey('Exercise', models.DO_NOTHING, db_column='id_exercise')
    v_answer = models.TextField()
    n_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    b_iscorrect = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ANSWER'
        unique_together = (('id_answer', 'id_student', 'id_exercise'),)


class AnswerMultipleOption(models.Model):
    id_option = models.OneToOneField('MultipleOption', models.DO_NOTHING, db_column='id_option', primary_key=True)  # The composite primary key (id_option, id_answer) found, that is not supported. The first column is selected.
    id_answer = models.ForeignKey(Answer, models.DO_NOTHING, db_column='id_answer')

    class Meta:
        managed = False
        db_table = 'ANSWER_MULTIPLE_OPTION'
        unique_together = (('id_option', 'id_answer'),)


class Attempt(models.Model):
    id_answer = models.OneToOneField(Answer, models.DO_NOTHING, db_column='id_answer', primary_key=True)  # The composite primary key (id_answer, id_option) found, that is not supported. The first column is selected.
    id_option = models.ForeignKey('MultipleOption', models.DO_NOTHING, db_column='id_option')
    d_began = models.DateTimeField()
    d_finished = models.DateTimeField()
    n_attempt_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ATTEMPT'
        unique_together = (('id_answer', 'id_option'),)


class ChapterEvaluation(models.Model):
    id_learningchapter = models.OneToOneField('LearningChapter', models.DO_NOTHING, db_column='id_learningchapter', primary_key=True)  # The composite primary key (id_learningchapter, id_evaluation) found, that is not supported. The first column is selected.
    id_evaluation = models.ForeignKey('Evaluation', models.DO_NOTHING, db_column='id_evaluation')

    class Meta:
        managed = False
        db_table = 'CHAPTER_EVALUATION'
        unique_together = (('id_learningchapter', 'id_evaluation'),)


class ChapterExercise(models.Model):
    id_learningchapter = models.OneToOneField('LearningChapter', models.DO_NOTHING, db_column='id_learningchapter', primary_key=True)  # The composite primary key (id_learningchapter, id_exercise) found, that is not supported. The first column is selected.
    id_exercise = models.ForeignKey('Exercise', models.DO_NOTHING, db_column='id_exercise')

    class Meta:
        managed = False
        db_table = 'CHAPTER_EXERCISE'
        unique_together = (('id_learningchapter', 'id_exercise'),)


class ChapterStudent(models.Model):
    id_student = models.OneToOneField('Student', models.DO_NOTHING, db_column='id_student', primary_key=True)  # The composite primary key (id_student, id_learningchapter) found, that is not supported. The first column is selected.
    id_learningchapter = models.ForeignKey('LearningChapter', models.DO_NOTHING, db_column='id_learningchapter')
    n_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    n_ranking = models.IntegerField()
    d_begin = models.DateField()
    d_finish = models.DateField(blank=True, null=True)
    n_normalized_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CHAPTER_STUDENT'
        unique_together = (('id_student', 'id_learningchapter'),)


class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    id_instructor = models.ForeignKey('Instructor', models.DO_NOTHING, db_column='id_instructor')
    v_subject = models.CharField(max_length=255)
    d_created = models.DateField()
    d_starting_at = models.DateField()
    d_finishing_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'COURSE'


class CourseLearnchapter(models.Model):
    id_course = models.OneToOneField(Course, models.DO_NOTHING, db_column='id_course', primary_key=True)  # The composite primary key (id_course, id_learningchapter) found, that is not supported. The first column is selected.
    id_learningchapter = models.ForeignKey('LearningChapter', models.DO_NOTHING, db_column='id_learningchapter')

    class Meta:
        managed = False
        db_table = 'COURSE_LEARNCHAPTER'
        unique_together = (('id_course', 'id_learningchapter'),)


class DifficultyLevel(models.Model):
    id_difficultylevel = models.AutoField(primary_key=True)
    v_title = models.CharField(max_length=20)
    v_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'DIFFICULTY_LEVEL'


class Evaluation(models.Model):
    id_evaluation = models.AutoField(primary_key=True)
    f_weight = models.DecimalField(max_digits=5, decimal_places=2)
    d_deadline = models.DateField()

    class Meta:
        managed = False
        db_table = 'EVALUATION'


class EvaluationExercise(models.Model):
    id_evaluation = models.OneToOneField(Evaluation, models.DO_NOTHING, db_column='id_evaluation', primary_key=True)  # The composite primary key (id_evaluation, id_exercise) found, that is not supported. The first column is selected.
    id_exercise = models.ForeignKey('Exercise', models.DO_NOTHING, db_column='id_exercise')

    class Meta:
        managed = False
        db_table = 'EVALUATION_EXERCISE'
        unique_together = (('id_evaluation', 'id_exercise'),)


class Exercise(models.Model):
    id_exercise = models.AutoField(primary_key=True)
    f_weight = models.DecimalField(max_digits=5, decimal_places=2)
    d_deadline = models.DateField()
    id_difficultylevel = models.ForeignKey(DifficultyLevel, models.DO_NOTHING, db_column='id_difficultylevel')
    n_max_attempts = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'EXERCISE'


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


class Instructor(models.Model):
    id_instructor = models.AutoField(primary_key=True)
    id_user = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    n_phone = models.CharField(max_length=20, blank=True, null=True)
    v_specialty = models.CharField(max_length=255)
    v_bio = models.TextField()

    class Meta:
        managed = False
        db_table = 'INSTRUCTOR'


class LearningChapter(models.Model):
    id_learningchapter = models.AutoField(primary_key=True)
    id_instructor = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='id_instructor')
    d_created_at = models.DateField()
    v_content = models.TextField(blank=True, null=True)
    d_deadline = models.DateField(blank=True, null=True)
    f_weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'LEARNING_CHAPTER'


class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_sender = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='id_sender')
    id_receiver = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='id_receiver', related_name='message_id_receiver_set')
    v_text = models.TextField(blank=True, null=True)
    d_sent_at = models.DateTimeField()
    n_read_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MESSAGE'


class MultipleOption(models.Model):
    id_option = models.AutoField(primary_key=True)
    id_exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='id_exercise', blank=True, null=True)
    b_iscorrect = models.IntegerField(blank=True, null=True)
    v_option = models.TextField()

    class Meta:
        managed = False
        db_table = 'MULTIPLE_OPTION'


class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    id_user = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    n_gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    d_starting_date = models.DateField()
    d_join_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'STUDENT'


class StudentCourse(models.Model):
    id_student = models.OneToOneField(Student, models.DO_NOTHING, db_column='id_student', primary_key=True)  # The composite primary key (id_student, id_course) found, that is not supported. The first column is selected.
    id_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='id_course')

    class Meta:
        managed = False
        db_table = 'STUDENT_COURSE'
        unique_together = (('id_student', 'id_course'),)


class StudentEvaluation(models.Model):
    id_student = models.OneToOneField(Student, models.DO_NOTHING, db_column='id_student', primary_key=True)  # The composite primary key (id_student, id_evaluation) found, that is not supported. The first column is selected.
    id_evaluation = models.ForeignKey(Evaluation, models.DO_NOTHING, db_column='id_evaluation')
    f_score = models.DecimalField(max_digits=5, decimal_places=2)
    d_begins = models.DateField(blank=True, null=True)
    d_finish = models.DateField(blank=True, null=True)
    n_score_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STUDENT_EVALUATION'
        unique_together = (('id_student', 'id_evaluation'),)


class StudentEvaluationLlm(models.Model):
    id_student = models.IntegerField(primary_key=True)  # The composite primary key (id_student, id_exercise_llm) found, that is not supported. The first column is selected.
    id_exercise_llm = models.ForeignKey(ExerciseLlm, models.DO_NOTHING, db_column='id_exercise_llm')
    f_score = models.DecimalField(max_digits=5, decimal_places=2)
    d_begins = models.DateField(blank=True, null=True)
    d_finish = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STUDENT_EVALUATION_LLM'
        unique_together = (('id_student', 'id_exercise_llm'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MyappAnswer(models.Model):
    v_answer = models.TextField()
    n_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    b_iscorrect = models.IntegerField(blank=True, null=True)
    submitted_at = models.DateTimeField()
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING)
    student = models.ForeignKey(Student, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'myapp_answer'


class MyappAnswermultipleoption(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_answer = models.ForeignKey(MyappAnswer, models.DO_NOTHING, db_column='id_answer')
    id_option = models.ForeignKey(MultipleOption, models.DO_NOTHING, db_column='id_option')

    class Meta:
        managed = False
        db_table = 'myapp_answermultipleoption'
        unique_together = (('id_option', 'id_answer'),)


class MyappChapterstudent(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    n_ranking = models.IntegerField()
    d_begin = models.DateField()
    d_finish = models.DateField(blank=True, null=True)
    id_learningchapter = models.ForeignKey(LearningChapter, models.DO_NOTHING, db_column='id_learningchapter')
    id_student = models.ForeignKey(Student, models.DO_NOTHING, db_column='id_student')

    class Meta:
        managed = False
        db_table = 'myapp_chapterstudent'
        unique_together = (('id_student', 'id_learningchapter'),)


class MyappCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    created = models.DateField()
    starting_at = models.DateField()
    finishing_at = models.DateField()
    instructor = models.ForeignKey(Instructor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'myapp_course'


class MyappCourselearnchapter(models.Model):
    id = models.BigAutoField(primary_key=True)
    chapter = models.ForeignKey(LearningChapter, models.DO_NOTHING)
    course = models.ForeignKey(MyappCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'myapp_courselearnchapter'
        unique_together = (('course', 'chapter'),)


class MyappStudentcourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.ForeignKey(MyappCourse, models.DO_NOTHING)
    student = models.ForeignKey(Student, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'myapp_studentcourse'
        unique_together = (('student', 'course'),)


class MyappUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_type = models.CharField(max_length=20)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'myapp_userprofile'

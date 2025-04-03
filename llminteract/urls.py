from django.urls import path
from . import views
from . import LLMStudent
from . import LLMInstructor

urlpatterns = [
    path('', views.llm_interact_stu, name='llm_interact_stu'),
    path('llmins/', views.llm_interact_ins, name='llm_interact_ins'),
    path('llmexe/',LLMStudent.llm_interact,name='llm_interact_student'),
    path('llmexe/view/',LLMStudent.view_tasks,name="view_tasks_student"),
    path('llmexe/clear/', LLMStudent.clear_tasks, name='clear_tasks_student'),
    path('llmexe/generate_from_keyword/', LLMStudent.generate_tests_from_keyword, name='generate_from_keyword'),
    path('llmexe/submit_answer/', LLMStudent.submit_answer, name='submit_answer'),
    path("llmexe/submit_final_score/",LLMStudent.submit_final_score,name="submit_final_score"),
    path("llmexe/record/",LLMStudent.llm_view_record,name="llm_view_record"),
    path('llmins/onestu/', LLMInstructor.llm_view_record, name='llm_view_record_ins'),
    path('llmins/aiassist/', LLMInstructor.llm_view_AIassist, name='llm_AIassist'),

]

from django.urls import path
from django.urls.conf import include
from core.views import StudentMarksView, StudentTotalMarks, SubjectAvgView

urlpatterns = [
    path("marks", StudentMarksView.as_view()),
    path("marks/<int:id>", StudentMarksView.as_view()),
    path("student/marks", StudentTotalMarks.as_view()),
    path("subject/average", SubjectAvgView.as_view()),
]
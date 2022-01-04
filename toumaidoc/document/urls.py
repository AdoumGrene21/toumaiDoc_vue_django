from django.urls import path, include

from document import views 

urlpatterns =[
    path('last_documents/', views.LastDocumentsList.as_view()),
    path('documents/<slug:type_slug>/<slug:document_slug>/', views.DocumentDetail.as_view()),
]
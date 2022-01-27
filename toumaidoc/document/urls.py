from django.urls import path, include

from document import views 

urlpatterns =[
    path('last_documents/', views.LastDocumentsList),
    path('documents/<slug:type_slug>/<slug:document_slug>/', views.DocumentDetail),
    path('<slug:type_slug>/', views.TypeDetail),

    path('create_type/', views.modelCreate)
]
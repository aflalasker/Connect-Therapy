from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views

from connect_therapy.views import *

app_name = 'connect_therapy'
urlpatterns = [
    path('patient/signup',
         PatientSignUpView.as_view(),
         name="patient-signup"
         ),
    path('patient/signup/success',
         TemplateView.as_view(
             template_name='connect_therapy/patient/signup-success.html'
         ),
         name="patient-signup-success"
         ),
    path('patient/login',
         PatientLoginView.as_view(),
         name='patient-login'
         ),
    path('patient/login/success',
         TemplateView.as_view(
             template_name='connect_therapy/patient/login-success.html'
         ),
         name='patient-login-success'
         ),
    path('patient/logout',
         auth_views.logout,
         {
             'next_page':
                 reverse_lazy('connect_therapy:patient-logout-success'),
         },
         name='patient-logout'
         ),
    path('patient/logout/success',
         TemplateView.as_view(
             template_name='connect_therapy/patient/logout-success.html'
         ),
         name='patient-logout-success'
         ),
    path('chat/<int:pk>',
         ChatView.as_view(),
         name="chat"
         ),
    path('patient/my-appointments',
         PatientMyAppointmentsView.as_view(),
         name='patient-my-appointments'
         ),
    path('patient/notes-before-appointment/<int:appointment_id>',
         PatientNotesBeforeView.as_view(),
         name='patient-notes-before'
         ),
    path('practitioner/signup',
         PractitionerSignUpView.as_view(),
         name='practitioner-signup'
         ),
    path('practitioner/signup/success',
         TemplateView.as_view(
             template_name='connect_therapy/practitioner/signup-success.html'
         ),
         name='practitioner-signup-success'
         ),
    path('practitioner/login',
         PractitionerLoginView.as_view(),
         name='practitioner-login'
         ),
    path('practitioner/login/success',
         TemplateView.as_view(
             template_name='connect_therapy/practitioner/login-success.html'
         ),
         name='practitioner-login-success'
         ),
    path('practitioner/logout',
         auth_views.logout,
         {
             'next_page':
                 reverse_lazy('connect_therapy:practitioner-logout-success'),
         },
         name='practitioner-logout'
         ),
    path('practitioner/logout/success',
         TemplateView.as_view(
             template_name='connect_therapy/practitioner/logout-success.html'
         ),
         name='practitioner-logout-success'
         ),
    path('about',
         TemplateView.as_view(
             template_name='connect_therapy/about.html'
         ),
         name='about'),
    path('practitioner',
         TemplateView.as_view(
            template_name='connect_therapy/practitioner/homepage.html'
         ),
         name='practitioner-homepage'
         ),
    path('',
         TemplateView.as_view(
             template_name='connect_therapy/index.html'
         ),
         name='index'
         ),
    path('patient',
         TemplateView.as_view(
             template_name='connect_therapy/patient/homepage.html'
         ),
         name='patient-homepage'
         ),
    path('practitioner/notes/<int:appointment_id>',
         PractitionerNotesView.as_view(),
         name='practitioner-notes'
         ),
    path('practitioner/my-appointments',
         PractitionerMyAppointmentsView.as_view(),
         name='practitioner-my-appointments'
         ),
    path('patient/cancel-appointment/<int:pk>',
         PatientCancelAppointmentView.as_view(),
         name='patient-cancel-appointment'
         ),
    path('practitioner/view-previous-notes/<int:pk>',
         PractitionerPreviousNotesView.as_view(),
         name='practitioner-appointment-notes'
         ),
    path('practitioner/view-current-notes/<int:pk>',
         PatientPreviousNotesView.as_view(),
         name='practitioner-before-meeting-notes'
         ),
    path('patient/view-previous-notes/<int:pk>',
         PatientPreviousNotesView.as_view(),
         name='patient-appointment-notes',
         ),
]

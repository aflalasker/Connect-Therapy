from django.urls import path
from django.views.generic import TemplateView

from connect_therapy.views.practitioner import *

urlpatterns = [
    path('signup',
         PractitionerSignUpView.as_view(),
         name='practitioner-signup'
         ),
    path('signup/success',
         TemplateView.as_view(
             template_name='connect_therapy/practitioner/signup-success.html'
         ),
         name='practitioner-signup-success'
         ),
    path('login',
         PractitionerLoginView.as_view(),
         name='practitioner-login'
         ),
    path('login/success',
         TemplateView.as_view(
             template_name='connect_therapy/practitioner/login-success.html'
         ),
         name='practitioner-login-success'
         ),
    path('logout',
         auth_views.logout,
         {
             'next_page':
                 reverse_lazy('connect_therapy:practitioner-logout-success'),
         },
         name='practitioner-logout'
         ),
    path('logout/success',
         TemplateView.as_view(
             template_name='connect_therapy/practitioner/logout-success.html'
         ),
         name='practitioner-logout-success'
         ),
    path('',
         TemplateView.as_view(
            template_name='connect_therapy/practitioner/homepage.html'
         ),
         name='practitioner-homepage'
         ),
    path('notes/<int:appointment_id>',
         PractitionerNotesView.as_view(),
         name='practitioner-notes'
         ),
    path('my-appointments',
         PractitionerMyAppointmentsView.as_view(),
         name='practitioner-my-appointments'
         ),
    path('view-previous-notes/<int:pk>',
         PractitionerPreviousNotesView.as_view(),
         name='practitioner-appointment-notes'
         ),
    path('view-current-notes/<int:pk>',
         PractitionerPreviousNotesView.as_view(),
         name='practitioner-before-meeting-notes'
         ),
    path('view-patients',
         PractitionerAllPatientsView.as_view(),
         name='practitioner-view-patients'
         ),
]

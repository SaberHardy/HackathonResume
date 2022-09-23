from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

from resumeApp.forms import ContactForm
from resumeApp.models import WhoAmI, OnlineCourses, ProfessionalExperience


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['full_name']
            name = form.cleaned_data['email']
            content = form.cleaned_data['content']
            print(f"The form is valid {email}-{name}-{content}")

            # html = render_to_string(
            #     'blabla.html',
            #     {'name': name,
            #      'email': email,
            #      'content': content})
            send_mail(
                name,  # subject
                content,  # message
                email,  # from
                ['justdjangotest@gmail.com'],  # to whom
                fail_silently=False,
            )

            return redirect('home')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)


def get_infos(request):
    about_me = WhoAmI.objects.all()
    context = {
        'about_me': about_me,
    }
    return context


def get_online_courses(request):
    online_courses = OnlineCourses.objects.all()
    context = {
        'online_courses': online_courses,
    }
    return context


def get_professional_experience(request):
    experiences = ProfessionalExperience.objects.all()
    context = {
        'experiences': experiences,
    }
    return context

"""
 # TODO: 
Who am I.(description)
Education:
    - Bachelor and Master
Online Courses
    - Coursera
Interests:
Work Experience:

Skills and Frameworks(centred)(This should be with bars and percents)
Hobbies
Languages
Projects

Contact me.

Footer

Powered by me

Button to navigate to top


"""

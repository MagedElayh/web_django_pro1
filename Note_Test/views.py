#views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import TeacherForm,SubjectForm

def home(request):
    form = TeacherForm
    form_subject=SubjectForm
    if request.method == "POST":
        form_subject = SubjectForm(data=request.POST)
        form = TeacherForm(data=request.POST)
        if form_subject.is_valid() and form.is_valid:
            task = form.save()
            tcode=task.id
            print('----------------------------------------------------')
            print(tcode)
            # form_subject.save(commit=False)
            # form_subject.T_Code=tcode
            task_sub=form_subject.save()
            task_sub.T_Code = task
            task_sub.save()
            form         = TeacherForm()
            form_subject = SubjectForm()
        else:
            pass
            # form = TeacherForm()
            # form_subject=SubjectForm()
    context={
        'form'         : form,
        'form_subject' : form_subject
    }
    return render(request,'note.html',context)



















# def index(request):
#     members = Member.objects.all()
#     context = {'members': members}
#     return render(request, 'base.html',context)
 
 
# def create(request):
#     member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
#     member.save()
#     return redirect('/')
 
# def read(request):
#     members = Member.objects.all()
#     context = {'members': members}
#     return render(request, 'result.html', context)
 
# def edit(request, id):
#     members = Member.objects.get(id=id)
#     context = {'member': members}
#     return render(request, 'edit.html', context)
 
 
# def update(request, id):
#     member = Member.objects.get(id=id)
#     member.firstname = request.POST['firstname']
#     member.lastname = request.POST['lastname']
#     member.save()
#     return redirect('/myapp')
#     # return HttpResponseRedirect('/myapp/')
 
 
# def delete(request, id):
#     member = Member.objects.get(id=id)
#     member.delete()
#     return redirect('/')


# # //////////////////////////////////////////////////////////

# def save_member_form(request, form, template_name):
#     data = dict()
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             members = Member.objects.all()
#             data['html_member_list'] = render_to_string('myapp/partial_member_list.html', {
#                 'members': members
#             })
#         else:
#             data['form_is_valid'] = False
#     context = {'form': form}
#     data['html_form'] = render_to_string(template_name, context, request=request)
#     return JsonResponse(data)

# def member_create(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#     else:
#         form = MemberForm()
#     return save_member_form(request, form, 'myapp/partial_myapp_create.html')


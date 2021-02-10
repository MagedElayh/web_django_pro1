from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView
from .models import Doctor, Period, Month
from .forms import DoctorForm, PeriodForm
# from mainpage.tables import DoctorTable print("vjhgvn")

def mainpage(request):
    # doctors=DoctorTable(Doctor.objects.all())
    return render(request,'index1.html',{})

import django_tables2 as tables


class SimpleTable(tables.Table):
    class Meta:
        model = Doctor

class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = Doctor.objects.all()
    template_name = "table.html"

def doctor(request):
    form = DoctorForm
    # doctors=DoctorTable(Doctor.objects.all())
    perForDoc={}
    doctors=Doctor.objects.all()
    for doctor in doctors:
        s=str(doctor.frist_name)
        perForDoc[doctor]=doctor.period_set.all()
        print(doctor,perForDoc[doctor])
    # perForDoc=doctors.period_set.all()
    period=Period.objects.prefetch_related('doctor')

    # for periods in period:
    #     print(periods.doctor.values('frist_name','last_name'),periods.time_from)

    # to get how doctor 1 have period
    d=Doctor.objects.get(frist_name="majedd") #or  (id=1)
    d.period_set.all()   #write model_set lowercase ffrist letter no upper
    print(d.period_set.all())

    context={
        "perForDoc":perForDoc,
        "period":period,
        "form":form,
        "doctor":doctors,
    }
    
    return render(request,'doctor.html',context)

class DoctorView(FormView):
    template_name='doctorper.html'
    form_class = DoctorForm
    success_url ='/add_doctor/'
    def form_valid(self,form):
        print(form)
        form.save()
        return super().form_valid(form)

            # if request.method == "POST"
            #     form = DoctorForm
            #     if form.is_valid():
            #         name = form.cleaned_data['frist_name']
            #         form.save()
            #         # return JsonResponse({"name": name}, status=200)
            #     else:
            #         pass:
            #         # errors = form.errors.as_json()
            #         # return JsonResponse({"errors": errors}, status=400)

            # return render(request,"doctor.html", {"form": form})

class PeriodView(FormView):
    template_name='period.html'
    form_class = PeriodForm
    success_url ='/period/'
    def form_valid(self,form):
        print(form)
        form.save()
        return super().form_valid(form)

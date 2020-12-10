from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TaxModel, ResultModel
from .form import TaxForm
from .calculator import deduction, income_life_insurance, resident_life_insurance, model_save

# Create your views here.


class TaxModelUpdateView(UpdateView):
    model = TaxModel
    template_name = "calculator.html"
    fields = ('annual_income', 'insurance_fee', 'life_fee',
              'care_fee', 'pension_fee', 'blue_yes', 'basic_yes')
    success_url = reverse_lazy('result')


def resultfunc(request):
    object_list = TaxModel.objects.get(pk=1)
    deduction_sum = deduction(
        object_list.blue_yes, object_list.basic_yes)

    life_list = [object_list.life_fee,
                 object_list.care_fee, object_list.pension_fee]

    income_life = income_life_insurance(life_list)
    resident_life = resident_life_insurance(life_list)

    input_list = {
        'annual_income': object_list.annual_income,
        'insurance_fee': object_list.insurance_fee,
        'deduction_sum': deduction_sum,
        'income_life': income_life,
        'resident_life': resident_life
    }

    model_save(input_list)
    object = ResultModel.objects.get(pk=1)

    return render(request, 'result.html', {'object': object})

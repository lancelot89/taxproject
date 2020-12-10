import math
from .models import ResultModel


def deduction(blue_yes, basic_yes):
    blue_deduction = None
    income_basic_deduction = None
    resident_basic_deduction = None
    if blue_yes:
        blue_deduction = 650000
    else:
        blue_deduction = 100000

    if basic_yes:
        income_basic_deduction = 380000
        resident_basic_deduction = 330000
    else:
        income_basic_deduction = 280000
        resident_basic_deduction = 230000

    income_deduction_sum = blue_deduction + income_basic_deduction
    resident_basic_deduction = blue_deduction + resident_basic_deduction
    deduction_sum = {
        'income_deduction_sum': income_deduction_sum,
        'resident_basic_deduction': resident_basic_deduction
    }

    return deduction_sum


def income_life_insurance(life_list):
    income_life_insurance_fee = 0
    for life_individual in life_list:
        if life_individual <= 20000:
            income_life_insurance_fee += life_individual
            continue

        elif life_individual <= 40000:
            income_life_insurance_fee += (life_individual / 2) + 10000
            continue

        elif life_individual <= 80000:
            income_life_insurance_fee += (life_individual / 4) + 20000
            continue

        else:
            income_life_insurance_fee += 40000
            continue
    if income_life_insurance_fee >= 120000:
        income_life_insurance_fee = 120000

    return income_life_insurance_fee


def resident_life_insurance(life_list):
    resident_life_insurance_fee = 0
    for life_individual in life_list:
        if life_individual <= 12000:
            resident_life_insurance_fee += life_individual
            continue

        elif life_individual <= 32000:
            resident_life_insurance_fee += (life_individual / 2) + 6000
            continue

        elif life_individual <= 56000:
            resident_life_insurance_fee += (
                life_individual / 4) + 14000
            continue

        else:
            resident_life_insurance_fee += 28000
            continue
    if resident_life_insurance_fee >= 70000:
        resident_life_insurance_fee = 70000

    return resident_life_insurance_fee


def income_tax_calculate(taxable_income):

    income_tax_rate = {
        'A': [0.05, 0],
        'B': [0.1, 97500],
        'C': [0.2, 427500],
        'D': [0.23, 636000],
        'E': [0.33, 1536000],
        'F': [0.4, 2796000],
        'G': [0.45, 4796000]
    }

    if taxable_income <= 1950000:
        income_tax = (taxable_income *
                      income_tax_rate['A'][0]) - (income_tax_rate['A'][1])
        return math.floor(income_tax)

    elif taxable_income <= 3300000:
        income_tax = (taxable_income *
                      income_tax_rate['B'][0]) - (income_tax_rate['B'][1])
        return math.floor(income_tax)

    elif taxable_income <= 6950000:
        income_tax = (taxable_income *
                      income_tax_rate['C'][0]) - (income_tax_rate['C'][1])
        return math.floor(income_tax)

    elif taxable_income <= 9000000:
        income_tax = (taxable_income *
                      income_tax_rate['D'][0]) - (income_tax_rate['D'][1])
        return math.floor(income_tax)

    elif taxable_income <= 18000000:
        income_tax = (taxable_income *
                      income_tax_rate['E'][0]) - (income_tax_rate['E'][1])
        return math.floor(income_tax)

    elif taxable_income <= 40000000:
        income_tax = (taxable_income *
                      income_tax_rate['F'][0]) - (income_tax_rate['F'][1])
        return math.floor(income_tax)

    else:
        income_tax = (taxable_income *
                      income_tax_rate['G'][0]) - (income_tax_rate['G'][1])
        return math.floor(income_tax)


def model_save(input_list):
    taxable_income = input_list['annual_income'] - \
        (input_list['insurance_fee'] +
            input_list['income_life'] +
            input_list['deduction_sum']['income_deduction_sum'])

    resident_taxable_income = input_list['annual_income'] - \
        (input_list['insurance_fee'] +
            input_list['resident_life'] +
            input_list['deduction_sum']['resident_basic_deduction'])

    income_tax = income_tax_calculate(taxable_income)
    resident_tax = math.floor(resident_taxable_income * 0.1)
    health_insurance_tax = math.floor(
        ((resident_taxable_income*0.0714)+39900) +
        ((resident_taxable_income*0.0229)+12300))
    max_housetown_tax = math.floor((resident_tax*0.28744)+2000)
    if ResultModel.objects.filter(pk=1).exists():
        object = ResultModel.objects.get(pk=1)
        object.income_tax = income_tax
        object.resident_tax = resident_tax
        object.health_insurance_tax = health_insurance_tax
        object.max_housetown_tax = max_housetown_tax
        object.save()
        print('更新')
    else:
        object = ResultModel(id=1, income_tax=income_tax, resident_tax=resident_tax,
                             health_insurance_tax=health_insurance_tax, max_housetown_tax=max_housetown_tax)
        object.save()
        print('追加')

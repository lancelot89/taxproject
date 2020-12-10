from django import forms


class TaxForm(forms.Form):
    CHOICE = {
        (False, 'いいえ'),
        (True, 'はい'),
    }
    annual_income = forms.IntegerField(
        label='年収'
    )
    insurance_fee = forms.IntegerField(
        label='社会保険料'
    )
    life_fee = forms.IntegerField(
        label='一般保険'
    )
    care_fee = forms.IntegerField(
        label='介護保険料'
    )
    pension_fee = forms.IntegerField(
        label='個人年金'
    )
    blue_yes = forms.ChoiceField(
        label='青色申告の有無',
        choices=CHOICE,
        widget=forms.RadioSelect,

    )
    basic_yes = forms.ChoiceField(
        label='e-taxの有無',
        choices=CHOICE,
        widget=forms.RadioSelect,

    )

from django import forms
from django.core.exceptions import ValidationError


def check_density(value):
    if float(value) is not True:
        raise ValidationError('Incorrect value!')
    else:
        if value > 15.0 or value < 0.6:
            raise ValidationError('Incorrect value!')
        else:
            return True


def check_volume(value):
    if int(value) is not True:
        raise ValidationError('Incorrect Value')
    else:
        if value % 10:
            return True
        else:
            raise ValidationError('Incorrect value!')


def check_net_weight(value):
    if float(value) is not True:
        raise ValidationError('Incorrect value')
    else:
        if value > 9999 or value <= 0:
            raise ValidationError('Incorrect value')
        else:
            return True


def check_molar_weight(value):
    if float(value) is not True:
        raise ValidationError('Incorrect value')
    else:
        if value > 9999 or value < 2:
            raise ValidationError('Incorrect value')
        else:
            return True


class SolventForm(forms.Form):
    solvent_name = forms.CharField(max_length=64, label='Solvent name', required=True)
    vessel_volume = forms.IntegerField(label='volume [mL]', validators=[check_volume], required=True)
    # producer = nie mam chwilowo pomysłu jak to wypełnić
    density = forms.DecimalField(label='density [g/mL]', validators=[check_density], max_digits=3, decimal_places=1,
                                 required=True)
    comment = forms.CharField(max_length=256, widget=forms.Textarea(), label='Type your comment here...')


class ReagentForm(forms.Form):
    reagent_name = forms.CharField(max_length=256, label='Reagent name', required=True)
    color = forms.CharField(max_length=64, label='Color', required=True)
    # producer = nie mam chwilowo pomysłu jak to wypełnić
    common_name = forms.CharField(label='Common name', max_length=64)
    physical_state = forms.ChoiceField(label='Choose the physical state from the list',
                                       choices=['PDR', 'LQD', 'OIL', 'SLN'], required=True)
    # kiedy próbowałem podać listę krotek z parami klucz-wartość w modelach wyrzucało mi błąd - spodziewaną wartością
    # był string
    net_weight_in_grams = forms.DecimalField(max_digits=6, decimal_places=2, required=True,
                                             validators=[check_net_weight])
    molar_weight = forms.DecimalField(max_digits=7, decimal_places=3, required=True, label='Molar weight [g/mol]',
                                      validators=[check_molar_weight])
    comment = forms.CharField(max_length=256, widget=forms.Textarea())


class ReactionForm(forms.Form):
    description = forms.CharField(max_length=1024, required=True, label='Describe the reaction here ...',
                                  widget=forms.Textarea())
    comment = forms.CharField(max_length=256, label='Leave your comment here...', widget=forms.Textarea())


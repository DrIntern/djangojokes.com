from django import forms
from datetime import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )

class JobApplicationForm(forms.Form):

    employment = (
        (None, '---------'),
        ('full Time','Full Time'),
        ('part time','Part Time'),
    )

    week = (
        ( 1, 'Monday'),
        ( 2, 'Tuesday'),
        ( 3, 'Wednesday'),
        ( 4, 'Thursday'),
        ( 5, 'Friday'),
    )

    years = range(datetime.now().year, datetime.now().year+2)

    first_name = forms.CharField(
        widget = forms.TextInput(attrs= {'autofocus': True})
    )
    last_name = forms.CharField()

    email = forms.EmailField()

    website = forms.CharField(
        required= False,
        validators=[URLValidator(schemes=['http', 'https'])],
        widget= forms.TextInput(attrs= {
            'placeholder' : 'https://fakewebsite.com'
        })
    )
    
    employment_type = forms.ChoiceField(choices=employment)

    start_date = forms.DateField(help_text='The earliest date you can start working.', 
        widget = forms.SelectDateWidget(
            years= years,
            attrs= {'style': 'width: 31%; display: inline-block; margin: 0 1%'}
        ),
        validators=[validate_future_date],
        error_messages = {'past_date': 'Please enter a future date.'}
    )
    availability = forms.TypedMultipleChoiceField(
        choices=week,
        coerce=int,
        help_text='Check all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked':True}
        )
    )
    desired_hourly_rate = forms.DecimalField(
        widget= forms.NumberInput(
            attrs= {
                'min' : '10.00',
                'max' : '100.00',
                'step' : '.25',
            }
        )
    )
    cover_letter = forms.CharField(required= False,
        widget= forms.Textarea(
            attrs= {
                'cols' : '75',
                'rows' : '5',
            }
        ) 
    )
    confirmation = forms.BooleanField(label='I certify that the information I have provided is true.')
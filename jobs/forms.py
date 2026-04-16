from django import forms
from datetime import datetime

class JobApplicationForm(forms.Form):

    employment = (
        (None, '---------'),
        ('full Time','Full Time'),
        ('part time','Part Time'),
    )

    week = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
    )

    years = range(datetime.now().year, datetime.now().year+2)

    first_name = forms.CharField(
        widget = forms.TextInput(attrs= {'autofocus': True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required = False,
        widget = forms.URLInput(
            attrs= {
                'placeholder' : 'htttps:/fakewebsite.com',
                'size' : '50',
            }
        ) 
    )
    employment_type = forms.ChoiceField(choices=employment)
    start_date = forms.DateField(help_text='The earliest date you can start working.', 
        widget = forms.SelectDateWidget(
            years= years
        )                
    )
    availability = forms.MultipleChoiceField(choices = week,
        widget = forms.CheckboxSelectMultiple(
            attrs= {
                'checked' : 'True'
            }
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
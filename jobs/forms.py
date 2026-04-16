from django import forms

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

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required = False)
    employment_type = forms.ChoiceField(choices=employment)
    start_date = forms.DateField(help_text='The earliest date you can start working.')
    availability = forms.MultipleChoiceField(choices = week)
    desired_hourly_rate = forms.DecimalField()
    cover_letter = forms.CharField(required= False)
    confirmation = forms.BooleanField(label='I certify that the information I have provided is true.')
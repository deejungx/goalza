from django.db import models

DAY_OF_THE_WEEK = {
    '0' : 'Monday',
    '1' : 'Tuesday',
    '2' : 'Wednesday',
    '3' : 'Thursday',
    '4' : 'Friday',
    '5' : 'Saturday',
    '6' : 'Sunday',
}


class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1
        super(DayOfTheWeekField,self).__init__(*args, **kwargs)

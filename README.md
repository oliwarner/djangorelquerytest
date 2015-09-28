## http://stackoverflow.com/q/32783582/

A test to see why Django's realted queries aren't working. Step by step:

    git clone https://github.com/oliwarner/djangorelquerytest.git
    cd djangorelquerytest
    python3 -m venv venv
    . ./venv/bin/activate
    pip install ipython Django==1.9a1

    ./manage.py migrate
    ./manage.py shell

In the shell, fire in:

    from django.db.models import F
    from querytest.models import Category, Agent, Booking
    Booking.objects.exclude(agent__categories=F('category'))

And that'll make it explode with:

    OperationalError: no such column: U2.id

## But why?

I'm trying to pick out Booking instances where the category isn't within the m2m relationship between its Agent and Category. There's a [more flowery explanation its Stack Overflow question](http://stackoverflow.com/q/32783582/).

The database is preloaded with 3 Bookings:

 - One where its agent__category matches category. 
 - Two where it doesn't.

I want a query that returns the two incorrect ones. Good hunting.

----

This test was written for Django 1.9+ (so I could play with the new `python -m django startproject`) but the same issue exists in stable versions.
## http://stackoverflow.com/q/32783582/

A test to see why Django's realted queries aren't working.

To run this test, set up a new virtualenv, install Django-dev and 
some other stuff, and try to do a relative lookup.

Here's a step be step:

    git clone https://github.com/oliwarner/djangorelquerytest.git
    cd djangorelquerytest

    python3 -m venv venv
    . ./venv/bin/activate
    pip install -U pip
    pip install git+git://github.com/django/django.git
    pip install ipython

    ./manage.py migrate
    ./manage.py shell

And in the shell, fire in:

    from django.db.models import F
    from querytest.models import Category, Agent, Booking
    Booking.objects.exclude(agent__categories=F('category'))

It will explode after that. 

    OperationalError: no such column: U2.id

## But why?

I'm trying to pick out Booking instances where the category isn't within
the m2m relationship between its Agent and Category. There's a [more flowery explanation its Stack Overflow question](http://stackoverflow.com/q/32783582/).

The database is preloaded with 3 Bookings:

 - One where its agent__category matches. 
 - Two where it doesn't.

I want a query that returns the two incorrect. Good hunting.

----

This test was written for Django-dev (so I could play with the new
`python -m django startproject` but the same bug exists in stable 
versions.
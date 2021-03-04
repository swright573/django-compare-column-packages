==============================
django-compare-column-packages
==============================

This compares the packages django-vertical-multi-columns and django-columns. Both do roughly the same thing but in a much different way. To see the comparison in action, do the following:

*Windows commands are shown here. Use the equivalent if you run on Mac or Linux.*

1. Clone the django-compare-colums-packages repo. Unpack it if neccessary.

|
2. In the clone's directory, create a virtual environent (optional).

|
3. Install Django and the packages `django-vertical-multi-columns`_ and `django-columns`_.

.. code-block:: bash

	pip install django
	pip install django-columns
	pip install django-vertical-multi-columns


4. Update settings.py found in ./compare_columns with your secret key (*or use an environment variable*)

.. code-block:: bash

	SECRET_KEY = <*insert your Django secret key here*>

5. Activate the site.

.. code-block:: bash

	cd ..
	python manage.py runserver

8. Point your browser to localhost:8000. More information about the comparison is provided there.

.. _`django-vertical-multi-columns`: https://github.com/swright573/django-vertical-multi-columns
.. _`django-columns`: https://github.com/audreyfeldroy/django-columns

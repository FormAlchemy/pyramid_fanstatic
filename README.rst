pyramid_fanstatic
=================

This package provide a `Pyramid tween
<http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/hooks.html#registering-tweens>`_
for  `fanstatic <http://readthedocs.org/docs/fanstatic>`_ and a pyramid scaffold.

Scaffold
--------

Just run::

    $ pcreate -s starter -s pyramid_fanstatic myproject

Or::

    $ pcreate -s pyramid_fanstatic myexistingproject

if you want to add ``pyramid_fanstatic`` to an existing project.

Then read ``README_FANSTATIC.txt``

Fanstatic library definition is added to ``resources.py``. Resources are
located in the ``resources/`` directory.

Tween usage
-----------

You can use all `fanstatic options
<http://readthedocs.org/docs/fanstatic/en/latest/configuration.html>`_ in your
``.ini``. You just need to prefix options with ``fanstatic.``::

    [app:main]
    ...
    fanstatic.publisher_signature = fanstatic

You should add at least those two options::

    fanstatic.bottom = true
    fanstatic.debug = true # in development.ini

Then include ``pyramid_fanstatic`` in your ``__init__.py``::

    config.include('pyramid_fanstatic')

Base URLs for resources
^^^^^^^^^^^^^^^^^^^^^^^

By default, resource URLs from Fanstatic come served at in the script root and
Fanstatic provides its ``base_url`` option to set a URL prefix for all 
resource URLs. You can utilise this option statically using the following::

    [app:main]
    ...
    fanstatic.base_url = https://example.com/myapp

Take note that the URL should not have a trailing slash - Fanstatic has 
resources URLs that feature a ``/`` prefix already.

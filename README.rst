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

Static
""""""

By default, resource URLs from Fanstatic come served at in the script root and
Fanstatic provides its ``base_url`` option to set a URL prefix for all 
resource URLs. You can utilise this option statically using the following::

    [app:main]
    ...
    fanstatic.base_url = https://example.com/myapp

Take note that the URL should not have a trailing slash - Fanstatic has
resources URLs that feature a ``/`` prefix already.

Dynamic
"""""""

The above process works, but your application may need to serve from multiple
URLs, multiple paths, and so forth. ``pyramid_fanstatic`` has a special option
to allow the ``base_url`` prefix to be configured on a per-request basis. Your
application URI is generated using ``wsgiref.util.application_uri`` and is
based upon the request environment (according to `PEP 333
<http://www.python.org/dev/peps/pep-0333/#url-reconstruction>`_).

This option is ``fanstatic.use_application_uri`` and is specific to
``pyramid_fanstatic`` and is not passed to Fanstatic.  Specify this option as
follows::

    [app:main]
    ...
    fanstatic.use_application_uri = true

Any static ``base_url`` that is set will take precedence over this option.

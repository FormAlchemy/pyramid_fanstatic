pyramid_fanstatic
=================

This package provide a `Pyramid tween
<http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/hooks.html#registering-tweens>`_
for  `fanstatic <http://readthedocs.org/docs/fanstatic>`_.

Usage
-----

You can use all `fanstatic options
<http://readthedocs.org/docs/fanstatic/en/latest/configuration.html>`_ in your
``.ini``. You just need to prefix options with ``fanstatic.``::

    [app:main]
    ...
    fanstatic.publisher_signature = fanstatic

Then include ``pyramid_fanstatic`` in your ``__init__.py``::

    config.include('pyramid_fanstatic')



Changelog
=========

0.6 (2020-06-16)
----------------

Features
^^^^^^^^

- Add support for Python 3.7 and 3.8. [sallner, gotcha]

Other
^^^^^

- Remove zc.buildout and nosetest infratructure in favour of tox and pytest.


0.5 (2013-11-08)
----------------

- Support fanstatic > 1.0 with backward compat


0.4 (2012-09-21)
----------------

- Add new option ``fanstatic.use_application_uri`` to have Fanstatic
  base URLs generated using the current request. A ``base_url`` that is set
  will override this option.
  [davidjb]
- Document details about Fanstatic base URLs and the ``fanstatic.base_url``
  option.
  [davidjb]

0.3 (2011-12-27)
----------------

- Improve the Pyramid scaffold that's available with ``pcreate``.
  [gawel]


0.2 (2011-12-26)
----------------

- Forward requests to Pyramid handler if a resource can't be found.
  [gawel]
- Documentation and coverage improvements
  [gawel]


0.1 (2011-12-26)
----------------

- Initial release.
  [gawel]

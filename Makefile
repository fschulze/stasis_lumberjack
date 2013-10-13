virtualenv = virtualenv

all: bin/stasis

bin/python:
	$(virtualenv) --system-site-packages --clear .
	-clear-setuptools-dependency-links

bin/stasis: bin/python
	bin/pip install pyramid_jinja2
	bin/pip install PyYAML
	bin/pip install stasis

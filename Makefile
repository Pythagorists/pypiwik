init:
	pip install -r requirements.txt

release:
	python setup.py sdist --formats=gztar,zip upload --sign --identity=lyndsy@lyndsysimon.com

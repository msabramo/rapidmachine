test:
	nosetests
doc:
	pycco example/index.py
	cd docs && git add . && git commit -m "Update docs" && git push origin gh-pages
bootstrap:
	git clone git@github.com:myfreeweb/rapidmachine.git docs
	cd docs && git checkout gh-pages && cd ..
	virtualenv ./venv
	$(SHELL) -c "source ./venv/bin/activate && pip install -r ./requirements.txt"
	echo "Your virtualenv is ready, type 'source ./venv/bin/activate' to use it"
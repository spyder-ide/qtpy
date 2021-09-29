To release a new version of qtpy on PyPI:

* Close Github milestone

* git fetch upstream && git merge upstream/master

* git clean -xfdi

* Update CHANGELOG.md using `loghub` to generate the list of issues and PRs merged to add at the top of the file

    loghub -m vX.X.X spyder-ide/qtpy

* Update `_version.py` (set release version, remove 'dev0')

* git add . && git commit -m 'Release X.X.X'

* python setup.py sdist

* python setup.py bdist_wheel

* twine check dist/*

* twine upload dist/*

* git tag -a vX.X.X -m 'Release X.X.X'

* Update `_version.py` (add 'dev0' and increment minor)

* git add . && git commit -m 'Back to work'

* git push

* git push --tags

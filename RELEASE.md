# Release Procedure

To release a new version of QtPy on PyPI:


## Prepare

* Close Github milestone and ensure all issues are resolved/moved

* `git switch master && git pull upstream master` (assuming `master` is the release branch)

* Check `MANIFEST.in` and `setup.cfg` to ensure they are up to date


## Commit

* `pip install --upgrade loghub`

* Update `CHANGELOG.md` using `loghub` to generate the list of issues and PRs merged to add at the top of the file:

  ```bash
  loghub -m vX.Y.Z spyder-ide/qtpy
  ```

* Update `__version__` in `__init__.py` (set release version, remove `.dev0`)

* `git commit -am 'Release X.Y.Z'`


## Build

**Note**: We use `pip` instead of `conda` here even on Conda installs, to ensure we always get the latest upstream versions of the build dependencies.

* `git clean -xfdi`

* `python -m pip install --upgrade-strategy eager --upgrade build pip setuptools twine wheel`

* `python -bb -X dev -W error -m build`


## Upload

* `twine check --strict dist/*`

* `twine upload dist/*`

* `git tag -a vX.Y.Z -m 'Release X.Y.Z'`


## Cleanup

* Update `__version__` in `__init__.py` (add `.dev0` and increment minor)

* `git commit -am 'Back to work'`

* `git push upstream --follow-tags`

* Create a GitHub release from the tag

## PyPI

To release a new version of qtpy on PyPI (replacing `X.Y.Z` for the corresponding version when needed):

* Close [GitHub milestone](https://github.com/spyder-ide/qtpy/milestones)

* Update local repo with

      git checkout 1.x && git fetch upstream && git merge upstream/1.x

* Clean local repo with

      git clean -xfdi

* Update `CHANGELOG.md` with

      loghub spyder-ide/qtpy -m vX.Y.Z

* Update `_version.py` (set release version, remove 'dev0')

* Create release commit with

      git add . && git commit -m "Release X.Y.Z"

* Update the most important release packages with

      pip install -U pip setuptools twine wheel

* Create source distribution with

      python setup.py sdist

* Create wheel with

      python setup.py bdist_wheel

* Check release files with

      twine check dist/*

* Upload to PyPI package files with

      twine upload dist/*

* Create release tag with

      git tag -a vX.Y.Z -m "Release X.Y.Z"

* Update `_version.py` (add 'dev0' and increment minor)

* Create `Back to work` commit with

      git add . && git commit -m "Back to work"

* Merge new release commits on master with

      git checkout master && git fetch upstream && git merge upstream/master
      git merge 1.x
      git commit -m "Merge from 1.x: Release X.Y.Z"

* Update remote repository with

      git push upstream master
      git push upstream 1.x
      git push upstream --tags

## Conda-forge

To release a new version of qtpy on Conda-forge

* After the release on PyPI an automatic PR in the [conda-forge feedstock repo for qtpy](https://github.com/conda-forge/qtpy-feedstock/pulls) should open. Merging this PR will update the respective conda-forge package.
# Cookiecutter: Hypermodern Python for ML

<!-- badges-begin -->

[![CalVer][calver badge]][calver]
[![License][license badge]][license]<br>
[![Read the documentation][readthedocs badge]][readthedocs page]
[![Tests][github actions badge]][github actions page]
[![Codecov][codecov badge]][codecov page]<br>
[![pre-commit enabled][pre-commit badge]][pre-commit project]
[![Black codestyle][black badge]][black project]
[![Contributor Covenant][contributor covenant badge]][code of conduct]

[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black project]: https://github.com/psf/black
[calver badge]: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
[calver]: http://calver.org/
[github actions badge]: https://github.com/mdsach/cookiecutter-hypermodern-python-ml/workflows/Tests/badge.svg
[github actions page]: https://github.com/mdsach/cookiecutter-hypermodern-python-ml/actions?workflow=Tests
[github page]: https://github.com/mdsach/cookiecutter-hypermodern-python-ml
[license badge]: https://img.shields.io/github/license/mdsach/cookiecutter-hypermodern-python-ml
[license]: https://opensource.org/licenses/MIT
[pre-commit badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit project]: https://pre-commit.com/
[readthedocs badge]: https://img.shields.io/readthedocs/cookiecutter-hypermodern-python-ml/latest.svg?label=Read%20the%20Docs
[readthedocs page]: https://cookiecutter-hypermodern-python-ml.readthedocs.io/

<!-- badges-end -->

# Introduction
This is an opinionated framework using an object-oriented approach to training and deploying machine learning applications.

# Creating a new project

## Requirements
Git, DVC (), Poetry (>=1.2.2), 

1. Create git repo
   1. Add LICENSE
   2. Add README.md
   3. Add .gitignore
2. `poetry init`
   1. Add pyproject.toml
   2. Add <project_name> directory
   3. Add <__init__.py> file to <project_name> directory

# Credits & Acknowledgements

This [Cookiecutter](https://github.com/audreyr/cookiecutter) template is substantially based on work from previous authors:
   - [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python) by [Claudio Jolowicz](https://github.com/cjolowicz)
   - [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) by [DrivenData](https://www.drivendata.org/)

And inspired by ideas presented by the following authors:
   - [cookiecutter-ml](https://github.com/jeannefukumaru/cookiecutter-ml) by [Jeanne Fukumaru](https://github.com/jeannefukumaru)
   - [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) by [Audrey Roy Greenfeld](https://github.com/audreyfeldroy)
   - [cookiecutter-pypackage](https://github.com/briggySmalls/cookiecutter-pypackage) by [BriggySmalls](https://github.com/briggySmalls)
# Changelogs

## Latest Changes

## 1.0.8

### :black_nib: Code Changes

- :construction: refactored: 📦 bump types-python-dateutil from 2.9.0.20240316 to 2.9.0.20240821 (_2024-09-01_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.9.0 to 1.10.0 (_2024-09-01_)

### :card_file_box: Documents

- :page_facing_up: docs: implement mkdocs-material to this project. (_2024-09-02_)
- :page_facing_up: docs: update docs on installation tipic readme. (_2024-08-23_)
- :page_facing_up: docs: update readme docs and package desc. (_2024-08-23_)

### :bug: Fix Bugs

- :gear: fixed: fixed topic value on classifiers package. (_2024-08-23_)

### :package: Build & Workflow

- :toolbox: build: add env attach to docs workflow. (_2024-09-02_)

## 1.0.7

### :sparkles: Features

- :dart: feat: imgrate prepare_value function for Datetime. (_2024-05-26_)
- :dart: feat: transfer attributes and methods from origin formatter obj. (_2024-05-25_)
- :dart: feat: update importer for __asset objs. (_2024-05-25_)
- :dart: feat: add format method on assert module. (_2024-05-25_)
- :dart: feat: remove proxy obj and implement init instead. (_2024-05-25_)
- :dart: feat: add prepare_parsing cls method for receive parsing data. (_2024-05-25_)
- :dart: feat: add unescape regex on utils func. (_2024-05-25_)

### :black_nib: Code Changes

- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.8.14 to 1.9.0 (_2024-07-01_)
- :art: style: add type hint for mypy. (_2024-05-26_)
- :test_tube: tests: add test cases for the assets formatter obj on Serial. (_2024-05-26_)
- :construction: refactored: migrate prepare method to abstract class. (_2024-05-25_)

### :card_file_box: Documents

- :page_facing_up: docs: add more format asset for datetime. (_2024-05-26_)
- :page_facing_up: docs: update readme docs and remove link of any formatter obj. (_2024-05-25_)
- :page_facing_up: docs: changelog does not valid with old setting. (_2024-05-25_)

### :bug: Fix Bugs

- :gear: fixed: fix type of operator property on assets formatter obj. (_2024-05-26_)

### :package: Build & Workflow

- :toolbox: build: remove fix version of pytest on tests workflow. (_2024-05-25_)

## 1.0.6

### :sparkles: Features

- :dart: feat: add escape formatter group function. (_2024-05-24_)

### :black_nib: Code Changes

- :test_tube: tests: add test cases for escape regex work. (_2024-05-25_)
- :art: style: add logging with __name__ on init file. (_2024-05-19_)
- :art: style: change type hint for itself class to Self. (_2024-05-18_)

### :card_file_box: Documents

- :page_facing_up: docs: update readme and doc-string. (#69) (_2024-05-15_)

### :bug: Fix Bugs

- :gear: fixed: import return type does not use on __all__. (_2024-05-25_)
- :gear: fixed: add abstractmethod for abc class. (_2024-05-15_)

### :postbox: Dependencies

- :pushpin: deps: remove perf deps and add mkdocs deps for docs generator. (_2024-05-15_)

## 1.0.5

### :sparkles: Features

- :dart: feat: add validate method for Storage formatter object. (_2024-05-02_)

### :black_nib: Code Changes

- :test_tube: tests: add testcase for formatter group that should to fixed. (_2024-05-02_)
- :test_tube: tests: add testcase for str2byte on Storage formatter obj. (_2024-05-02_)

### :bug: Fix Bugs

- :gear: fixed: change staticmethod that use itself class to classmethod for support inherit. (_2024-05-02_)

### :package: Build & Workflow

- :toolbox: build: change repo url from github workflow file to env variable. (_2024-05-02_)
- :toolbox: build: add environment for seperate deployment to PyPI. (_2024-05-02_)

## 1.0.4

### :sparkles: Features

- :dart: feat: migrate and optimization the formatter object (_2024-05-02_)

### :black_nib: Code Changes

- :construction: refactored: change format generator suffix value update. (_2024-05-02_)
- :construction: refactored: add ClassVar to any class attributes. (_2024-05-01_)
- :construction: refactored: update change from the latest of main. (_2024-05-01_)

### :bug: Fix Bugs

- :gear: fixed: raise exception class does not use from exceptions file. (_2024-05-02_)
- :gear: fixed: revert "Merge branch 'main' into migration". (_2024-04-30_)

### :package: Build & Workflow

- :toolbox: build: add use venv step for activate python interpeter. (_2024-04-30_)
- :toolbox: build: add cache on venv that reduce installation time. (_2024-04-30_)
- :toolbox: build: use uv for installing Python dependencies in tests. (_2024-04-30_)
- :toolbox: build: change installation uv by curl command. (_2024-04-30_)
- :toolbox: build: test upgrade pip installation with uv. (_2024-04-30_)

## 1.0.3

### :sparkles: Features

- :dart: feat: add clishelf git config for force fix commit prefix. (_2024-04-29_)
- :dart: feat: add parse method on migration of formatter object. (_2024-04-29_)
- :dart: feat: change input argument name from register to asset. (_2024-04-29_)
- :dart: feat: add migration code for support dynamic creation. (_2024-03-04_)

### :black_nib: Code Changes

- :construction: refactored: remove exception classes that do not use on the formatter. (_2024-04-29_)

### :card_file_box: Documents

- :page_facing_up: docs: add migration note on formatter file. (_2024-04-29_)

### :bug: Fix Bugs

- :gear: fixed: merge branch 'migration' that fix the suffix matching. (_2024-04-29_)
- :gear: fixed: fix the bug that does not add suffix with the correct cache number. (_2024-04-29_)

### :package: Build & Workflow

- :toolbox: build: add pytest on installation step that loss from clishelf. (_2024-04-14_)

### :postbox: Dependencies

- :arrow_up: deps: upgrade dependencies from main branch (#63) (_2024-04-10_)

## 1.0.2

### :sparkles: Features

- :dart: feat: override __format__ method for support fstring. (_2024-04-14_)

### :black_nib: Code Changes

- :construction: refactored: 📦 bump types-python-dateutil from 2.8.19.20240106 to 2.9.0.20240316 (_2024-04-01_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.8.12 to 1.8.14 (_2024-04-01_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.8.11 to 1.8.12 (_2024-03-01_)
- :art: style: add type TypeAlias for hint support change on 3.12. (_2024-02-19_)
- :construction: refactored: change repo type of clishelf from local to hook. (_2024-02-13_)
- :construction: refactored: ⬆ bump actions/download-artifact from 3 to 4 (_2024-02-01_)
- :construction: refactored: ⬆ bump codecov/codecov-action from 3 to 4 (_2024-02-01_)
- :construction: refactored: ⬆ bump actions/upload-artifact from 3 to 4 (_2024-02-01_)
- :construction: refactored: 📦 bump types-python-dateutil from 2.8.19.14 to 2.8.19.20240106 (_2024-02-01_)
- :construction: refactored: ⬆ bump actions/cache from 3 to 4 (_2024-02-01_)

### :card_file_box: Documents

- :page_facing_up: docs: update README file. (_2024-03-03_)
- :page_facing_up: docs: update option highlight for note on README file. (_2024-02-29_)
- :page_facing_up: docs: update README for noted supported python version. (_2024-02-12_)
- :page_facing_up: docs: update README for supported python38. (_2024-01-30_)

### :bug: Fix Bugs

- :gear: fixed: change param name of download-artifact to pattern. (_2024-03-03_)
- :gear: fixed: fix pre-commit skip hook id on ci workflow. (_2024-02-13_)
- :gear: fixed: fix bug for download and upload artifact v4. (_2024-02-12_)

### :package: Build & Workflow

- :toolbox: build: add issue template for problem on GitHub repo. (_2024-02-18_)
- :toolbox: build: add multiple name for download and upload artifact supported on v4. (_2024-02-12_)

### :postbox: Dependencies

- :pushpin: deps: add typing-extensions for support import TypeAlias. (_2024-02-19_)

## 1.0.1

### Code Changes

- :construction: refactored: 🚧 [pre-commit.ci] auto fixes from pre-commit.com hooks (_2024-01-29_)
- :construction: refactored: 🚧 [pre-commit.ci] auto fixes from pre-commit.com hooks (_2024-01-15_)
- :construction: refactored: upgrade pyupgrade config for support py39. (_2024-01-11_)
- :test_tube: test: reformat test case that use assertIn instead assertTrue. (_2024-01-11_)

### Build & Workflow

- :toolbox: build: remove fix version of clishelf package. (_2024-01-30_)

## 1.0.0

### Features

- :dart: feat: migrate code from py3.8 to py3.9 (#42) (_2024-01-04_)

## 0.4.4

### Features

- :dart: feat: add float2decimal util function for convert value in Storage formatter obj. (_2023-10-16_)

### Code Changes

- :construction: refactored: ⬆ bump actions/setup-python from 4 to 5 (_2024-01-01_)
- :construction: refactored: ⬆ bump actions/download-artifact from 3 to 4 (_2024-01-01_)
- :construction: refactored: ⬆ bump actions/upload-artifact from 3 to 4 (_2024-01-01_)
- :construction: refactored: 📦 bump clishelf from 0.1.0 to 0.1.1 (_2024-01-01_)
- :construction: refactored: ⬆ bump pypa/gh-action-pypi-publish from 1.8.10 to 1.8.11 (_2023-12-01_)
- :construction: refactored: 📦 bump clishelf from 0.0.4 to 0.1.0 (_2023-11-01_)

### Fix Bugs

- :gear: fixed: change name of config data for clishelf on pyproject file. (_2024-01-04_)

### Build & Workflow

- :toolbox: build: change timezone from UTC to Etc/UTC. (_2023-11-22_)
- :toolbox: build: change frequency of dependabot from weekly to monthly. (_2023-11-22_)

## 0.4.3

### Features

- :dart: feat: create extract_wildcard class-method for BaseVersion object. (_2023-10-16_)

### Code Changes

- :construction: refactored: change object name of _VersionPackage to VerPackage for reusable. (_2023-10-16_)
- :construction: refactored: change type of standard value of Storage formatter obj. (_2023-10-16_)

## 0.4.2

### Features

- :dart: feat: add to_const use-case for the formatter group. (_2023-10-15_)
- :dart: feat: add string value that able to pass to any formatter objs. (_2023-10-15_)
- :dart: feat: add from_formats and from_value class-method for formatter group. (_2023-10-14_)

### Documents

- :page_facing_up: docs: update doc-string for Cosntant, FormatterGroup objs. (_2023-10-14_)
- :page_facing_up: docs: update doc-string on Naming, Storage formatter objs. (_2023-10-13_)

## 0.4.1

### Features

- :dart: feat: add train format for Naming formatter object. (_2023-10-12_)

### Code Changes

- :construction: refactor: 🚧 [pre-commit.ci] auto fixes from pre-commit.com hooks (_2023-10-09_)
- :construction: refactor: 🚧 [pre-commit.ci] pre-commit autoupdate (_2023-10-09_)
- :construction: refactored: add type hint on formatter obj. (_2023-10-06_)
- :construction: refactored: add next_version method to VersionPackage and test-cases. (_2023-10-05_)

### Documents

- :page_facing_up: docs: update doc-string on Datetime, Serial formatter objs. (_2023-10-13_)
- :page_facing_up: docs: update doc-string for formatter object. (_2023-10-13_)
- :page_facing_up: docs: update logo on python version support. (_2023-10-06_)

### Build & Workflow

- :toolbox: build: add deps version on pyproject file. (_2023-10-12_)

## 0.4.0

### Features

- :dart: feat: add __add__ operation for version formatter obj. (_2023-10-05_)
- :dart: feat: add VersionPackage that will instead packaging.version. (_2023-10-04_)
- :dart: feat: initial version object for Version formatter obj. (_2023-10-03_)
- :dart: feat: add %c and %u format for Serial formatter object. (_2023-10-02_)

### Code Changes

- :construction: refactor: 🚧 [pre-commit.ci] pre-commit autoupdate (_2023-10-03_)
- :test_tube: test: add test-case that compare between the value and datetime with same format string. (_2023-10-02_)
- :test_tube: test: add storage examples test-case. (_2023-10-02_)

### Documents

- :page_facing_up: docs: update 'train' naming format in doc-string. (_2023-10-03_)
- :page_facing_up: docs: update length of license comment. (_2023-10-02_)

### Build & Workflow

- :toolbox: build: add /tests/ on exclude list for build to sdist. (_2023-10-02_)

## 0.3.0

### Features

- :dart: feat: add checker method on SlotLevel object and validate of Naming. (_2023-10-02_)
- :dart: feat: add validate naming value for Naming formatter obj. (_2023-10-01_)
- :dart: feat: add validate datetime property on Datetime formatter obj. (_2023-10-01_)
- :dart: feat: add strct mode for check duplicat format value before initialize. (_2023-10-01_)
- :dart: feat: update formatter string for EnvConst object. (_2023-09-19_)

### Code Changes

- :construction: refactored: change name of method passer to from_value that relate with FormatterGroup. (_2023-10-02_)
- :construction: refactored: remove ddeutil deps and merge util funtions to local package. (_2023-10-02_)
- :construction: refactor: 🚧 [pre-commit.ci] pre-commit autoupdate (_2023-09-26_)
- :construction: refactor: 🚧 [pre-commit.ci] pre-commit autoupdate (_2023-09-19_)

### Documents

- :page_facing_up: docs: update use-case on README. (_2023-10-02_)
- :page_facing_up: docs: edit example code style on README. (_2023-09-29_)
- :page_facing_up: docs: update info in README and rename env const obj. (_2023-09-18_)
- :page_facing_up: docs: update doc-string for formatter module. (_2023-09-18_)

### Fix Bugs

- :gear: fixed: add condition that raise if format string does not exists in regexes. (_2023-10-02_)
- :gear: fixed: change condition of extract word for coverage. (_2023-10-02_)

## 0.2.3

### Code Changes

- :test_tube: test: add test data path to gitignore file. (_2023-09-17_)
- :construction: refactor: [pre-commit.ci] pre-commit autoupdate (_2023-09-12_)

### Documents

- :page_facing_up: docs: add more detail in doc-string in formatter module. (_2023-09-12_)

### Fix Bugs

- :gear: fixed: change logic of ordering property of formatter constant and group. (_2023-09-17_)

### Build & Workflow

- :toolbox: build: add skip local repo on pre-commit ci config. (_2023-09-12_)

## 0.2.2

### Code Changes

- :art: style: make newline on testing code and update usecase on README. (_2023-09-11_)
- :construction: refactored: add type hint and comment for mypy. (_2023-09-10_)

### Documents

- :page_facing_up: docs: update README on usecase topic. (_2023-09-11_)

### Build & Workflow

- :toolbox: build: add dependabot for pip package. (_2023-09-10_)
- :toolbox: build: add condition for receive cache in the ci workflow. (_2023-09-08_)

## 0.2.1

### Code Changes

- :construction: refactored: change deps package for dev and remove test from pyproject. (_2023-09-08_)
- :construction: refactored: remove un-use deps package from pyproject. (_2023-09-08_)

## 0.2.0

### Code Changes

- :construction: refactored: rename package from dup-fmt to fmtutil on PyPI. (_2023-09-07_)

## 0.1.4

### Features

- :dart: feat: implement cls.adjust func to formatter group object. (_2023-09-07_)
- :dart: feat: custom operation property for Naming formatter obj. (_2023-09-07_)
- :dart: feat: custom operation property for Datetime formatter obj. (_2023-09-07_)
- :dart: feat: implement operation property to formatter object. (_2023-09-07_)
- :dart: feat: add prepare_value staticmethod on parent formatter class. (_2023-09-07_)

### Code Changes

- :test_tube: test: upgrade pre-commit hooks. (_2023-09-07_)
- :test_tube: test: add test case for serial operation scenarios. (_2023-09-07_)

## 0.1.3

### Code Changes

- :test_tube: test: add test case for passing value to formatter static method. (_2023-09-06_)
- :test_tube: test: add examples test case for formatter group object. (_2023-09-06_)

## 0.1.2

### Features

- :dart: feat: add condition for validate value of formatter. (_2023-09-06_)
- :dart: feat: add .to_const() method on formatter object. (_2023-09-06_)
- :dart: feat: add base_fmt parameter on make_const func for ignore default. (_2023-09-06_)
- :dart: feat: add more type argument for formatter group class. (_2023-09-06_)

### Code Changes

- :test_tube: test: update test case for make formatter group from Constant. (_2023-09-05_)

## 0.1.1

### Documents

- :page_facing_up: docs: update README for Storage formatter object. (_2023-09-05_)

### Fix Bugs

- :gear: fixed: constant factory function can receive None value. (#18) (_2023-09-05_)

## 0.1.0

### Features

- :dart: feat: add Storage formatter and order property on formatter group instance. (_2023-09-05_)
- :dart: feat: create make_const instead Constant function. (_2023-09-05_)
- :dart: feat: add dynamic class name on constant func constructor. (_2023-09-05_)
- :dart: feat: add fmt2const constructor func for create Constant object. (_2023-09-05_)
- :dart: feat: implement order property on the formatter group class. (_2023-09-04_)
- :dart: feat: revision formatter group object logic. (_2023-09-04_)

### Code Changes

- :test_tube: test: add more test cases for Storage formatter object. (_2023-09-05_)
- :test_tube: test: add test case for coverage running. (_2023-09-05_)
- :construction: refactored: remove extract_regex_with_value function from formatter package. (_2023-09-04_)
- :construction: refactored: move base_level to class attribute. (_2023-09-04_)
- :construction: refactored: remove base_attr_prefix from formatter class. (_2023-09-04_)
- :construction: refactored: remove ordered formatter clas. (_2023-09-04_)
- :test_tube: test: change and fix test case for formatter group. (_2023-09-04_)
- :construction: refactored: improve pref on regex classmethod. (_2023-09-03_)

### Fix Bugs

- :gear: fixed: fix mypy for typing hint. (_2023-09-05_)

## 0.0.6

### Features

- :dart: feat: add new constructor of Constant object that receive fmt and value. (_2023-09-01_)

### Code Changes

- :test_tube: test: add test-case for parsing when formatter does not set group name. (_2023-09-03_)
- :construction: refactored: add suffix index on regex group name when parsing format. (_2023-09-03_)
- :construction: refactored: edit code statement that support mypy. (_2023-09-01_)

### Fix Bugs

- :gear: fixed: add condition of camel convert function if case empty string value. (_2023-09-01_)
- :gear: fixed: remove print debug stage from main code. (_2023-09-01_)

## 0.0.5.post1

### Features

- :dart: feat: create_const function can receive Formatter instance. (_2023-09-01_)

### Fix Bugs

- :gear: fixed: fix parser method of formatter object that riase if duplicate format str. (_2023-09-01_)

## 0.0.5.post0

### Code Changes

- :construction: refactored: change import layer of dup-uitls deps package. (_2023-08-28_)

### Fix Bugs

- :gear: fixed: generate Constant instance does not separate class attr. (_2023-08-31_)

## 0.0.5

### Code Changes

- :construction: refactored: change import layer of dup-uitls deps package. (_2023-08-28_)

### Fix Bugs

- :gear: fixed: generate Constant instance does not separate class attr. (_2023-08-31_)

## 0.0.5

### Features

- :dart: feat: add make_order_fmt func that make new order formatter obj. (_2023-08-27_)
- :dart: feat: add auto_serial in formatter ordered object. (_2023-08-27_)
- :dart: feat: add FMTS class attr for dynamic foramtter mapping when ordered. (_2023-08-26_)

### Code Changes

- :construction: refactored: add type of formatter group argument. (_2023-08-27_)
- :construction: refactored: split object of relative to objects file. (_2023-08-27_)
- :test_tube: test: add test cases for relativeserial object. (_2023-08-26_)
- :art: style: reformat code and comment message. (_2023-08-26_)
- :art: style: change code style that make wrong newline issue. (_2023-08-26_)
- :construction: refactored: add pre-commit message and change deps of test and dev optional deps. (_2023-08-25_)

### Fix Bugs

- :gear: fixed: change the version of dup-utils that fix import issue. (_2023-08-27_)
- :gear: fixed: duplicate replaces to the previous value on format method. (_2023-08-26_)
- :gear: fixed: add omit cli files for coverage process (_2023-08-25_)

## 0.0.4

### Features

- :dart: feat: add cli commands of formatter object parsing method (_2023-08-24_)
- :dart: feat: add utils package from dup-uitls project (_2023-07-11_)
- :dart: feat: add cli for formatter package (_2023-07-10_)
- :dart: feat: add performance load test for memory usage when init (_2023-06-19_)
- :dart: feat: Create dependabot.yml (_2023-06-19_)
- :dart: feat: add script for commit-msg and generate release note (_2023-06-19_)
- :dart: feat: edit pre-commit-msg hook (_2023-06-19_)
- :dart: feat: New (_2023-06-19_)

### Code Changes

- :test_tube: test: add type annotation with required by mypy package (_2023-08-24_)
- :construction: refactor: remove commit-message script (_2023-07-03_)
- :construction: refactor: ⬆ bump actions/setup-python from 3 to 4 (_2023-06-19_)
- :construction: refactor: ⬆ bump pypa/gh-action-pypi-publish from 1.8.5 to 1.8.6 (_2023-06-19_)
- script: add precommit (_2023-06-19_)
- :test_tube: test: add type construct of formatter object scenario (_2023-06-19_)

### Documents

- :page_facing_up: docs: prepare and remove unsuable code in pyproject.toml (_2023-06-23_)

### Fix Bugs

- :gear: fix: delete extension file from git command (_2023-06-20_)
- :gear: fix: merge change from main that add dependabot config (_2023-06-19_)
- :gear: fix: commit-msg (_2023-06-19_)
- :gear: fix:  (_2023-06-19_)
- :gear: fix: has_warning (_2023-06-19_)

### Build & Workflow

- :toolbox: build: add bump2version dependency and update version dup-utils (_2023-08-24_)

## 0.0.3.post1

**Fix**:

- :gear: fix: add type annotation for 100% coverage that missing (#7)
- :gear: fix: debug pytest for another python versions

**Features**:

- :dart: feat: add abstract class for Formatter object (#7)

**Documents**:

- :page_facing_up: docs: add more README.md

## 0.0.3

**Fix**:

- :gear: fix: add ignore htmlcov

**Workflows**:

- :toolbox: build: add black config on pyproject.toml

**Features**:

- :dart: feat: add type annotation and fix typing issue for mypy 100% coverage (#6)
- :dart: test: add test examples
- :dart: feat: add bump2version
- :dart: feat: add local hook for pytest
- :dart: feat: add test pipeline for python version 3.10, 3.11

**Documents**

- :page_facing_up: docs: add more CONTRIBUTING.md

## 0.0.2

**Fix**:

- :gear: fix: pypi release does not publish

## 0.0.1

**Fix**:

- :gear: fix: clear debug command on workflow
- :gear: fix: ci pipeline does not add htmlcov/ (#4)
- :gear: fix: add debug for ci pipeline
- :gear: fix: htmlcov/ on coverage comment action (#3)
- :gear: fix: add htmlcov/ for action comment bot
- :gear: fix: feature and workflows from v0.0.1 (#2)
- :gear: fix: coverage in ci pipeline
- :gear: fix: ls command in ci pipeline

**Workflows**:

- :toolbox: workflow: remove ci for any version branch
- :toolbox: build: move version to about (#1)
- :toolbox: workflow: edit ci pipeline
- :toolbox: build: move version to about
- :toolbox: action: add github actions

**Features**:

- :dart: feat: add foramtter package for version 0.0.1

**Documents**:

- :page_facing_up: docs: edit README file
- :page_facing_up: docs: add README and pyproject.toml files

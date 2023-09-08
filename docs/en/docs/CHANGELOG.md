# Changelogs

## Latest Changes

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

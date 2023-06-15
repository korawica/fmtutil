# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/korawica/dup-fmt/blob/coverage/htmlcov/index.html)

| Name                                    |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|---------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| dup\_fmt/\_\_about\_\_.py               |        0 |        0 |        0 |        0 |    100% |           |
| dup\_fmt/\_\_init\_\_.py                |        1 |        0 |        0 |        0 |    100% |           |
| dup\_fmt/errors.py                      |       15 |        0 |        4 |        0 |    100% |           |
| dup\_fmt/formatter.py                   |      511 |        0 |      199 |        0 |    100% |           |
| tests/\_\_init\_\_.py                   |        0 |        0 |        0 |        0 |    100% |           |
| tests/perfs/\_\_init\_\_.py             |        0 |        0 |        0 |        0 |    100% |           |
| tests/perfs/perf\_fomatter\_datetime.py |        0 |        0 |        0 |        0 |    100% |           |
| tests/test\_errors.py                   |       14 |        0 |        0 |        0 |    100% |           |
| tests/test\_examples.py                 |       12 |        0 |        0 |        0 |    100% |           |
| tests/test\_formatter.py                |       81 |        0 |       14 |        7 |     93% |29->31, 110->112, 121->123, 128->130, 139->141, 147->149, 166->168 |
| tests/test\_formatter\_datetime.py      |       36 |        0 |        0 |        0 |    100% |           |
| tests/test\_formatter\_group.py         |       34 |        0 |        4 |        2 |     95% |123->130, 162->164 |
| tests/test\_formatter\_naming.py        |       33 |        0 |        0 |        0 |    100% |           |
| tests/test\_formatter\_order.py         |       65 |        0 |        8 |        4 |     95% |37->39, 87->89, 109->111, 125->127 |
| tests/test\_formatter\_serial.py        |       45 |        0 |        2 |        1 |     98% |    55->57 |
| tests/test\_formatter\_version.py       |       43 |        0 |        2 |        1 |     98% |    52->61 |
| tests/test\_ralativeserial.py           |       18 |        0 |        0 |        0 |    100% |           |
|                               **TOTAL** |  **908** |    **0** |  **233** |   **15** | **99%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/korawica/dup-fmt/coverage/badge.svg)](https://htmlpreview.github.io/?https://github.com/korawica/dup-fmt/blob/coverage/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/korawica/dup-fmt/coverage/endpoint.json)](https://htmlpreview.github.io/?https://github.com/korawica/dup-fmt/blob/coverage/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fkorawica%2Fdup-fmt%2Fcoverage%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/korawica/dup-fmt/blob/coverage/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.
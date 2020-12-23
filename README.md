# data-structures-and-algorithms

Python implementations of data structures &amp; algorithms + solutions to problems

## Setup

This repo uses a virtual environment to ensure there's no conflict with globally
installed dependencies. To setup the repo:

```sh
$ python3 -m venv env
$ source venv/bin/activate
(venv) $ pip install -U pip setuptools wheel
(venv) $ pip install -r requirements.txt
```

## Tests

To run the linter(PEP8) with automatic corrections:

```sh
(venv) $ make lint
```

To run all tests:

```sh
(venv) $ make tests
```

To run tests in a specific directory:

```sh
(venv) $ pytest -rf -v <directory>
```

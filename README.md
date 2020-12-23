# data-structures-and-algorithms

Python implementations of data structures &amp; algorithms + solutions to problems

## Setup

This repo uses a virtual environment to ensure there's no conflict with globally
installed dependencies. To setup the repo:

```sh
$ python3 -m venv env
$ source venv/bin/activate
(venv) $ pip install -r requirements
```

## Tests

To run all tests:

```sh
(venv) $ pytest -rA
```

To run tests in a specific directory:

```sh
(venv) $ pytest -rA <directory>
```
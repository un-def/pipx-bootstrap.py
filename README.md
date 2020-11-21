# pipx-bootstrap.py

A Python script for installing pipx with pipx

## Other Versions

  * [POSIX Shell](https://github.com/un-def/pipx-bootstrap.sh)
  * [PowerShell](https://github.com/un-def/pipx-bootstrap.ps1)

## Motivation

[pipx][pipx-homepage] is an excellent tool for managing end-user applications written in Python. It installs each application (an *application* is, in fact, a regular Python package with some sort of binary, e.g., a console script) in isolated [virtual environment][venv-docs], thus avoiding pollution of system/user site directories. However, you still need to install `pipx` in a system or user site.

It seems like the ‘chicken and egg’ problem, doesn't it?

`pipx-bootstrap.py` solves the problem by installing `pipx` with `pipx` itself, that is, this script installs `pipx` as a regular `pipx` “application”.

## How it works

`pipx-bootstrap.py` works as follows:

  * creates a temporary directory
  * downloads `pipx` and its dependencies into this directory as wheels (`*.whl`) using existing `pip` installation
  * populates `sys.path` with the path of each wheel
  * runs `pipx` module with `install pipx` command
  * removes the temporary directory

## Usage

Download `pipx-bootstrap.py` and run it:

```shell
python3 pipx-bootstrap.py
```

or use ‘curl pipe python’ technique:

```shell
curl https://raw.githubusercontent.com/un-def/pipx-bootstrap.py/master/pipx-bootstrap.py | python3 -
```

Script arguments are passed to `pipx install pipx` command, e.g.,

```shell
python3 pipx-bootstrap.py --verbose --force
```

and

```shell
curl https://... | python3 - --verbose --force
```

are equivalent to

```shell
pipx install pipx --verbose --force
```

## Alternatives

* [pipx-in-pipx][pipx-in-pipx-github]

  It uses a way more complicated approach to do the same thing.

* pipx-bootstrap

  This is essentially a stripped down version of `pipx`. It is not available anymore. [Here][pipx-bootstrap-comment] is an announcement. [This][pipx-bootstrap-github-copy] could be a copy of the original repository.

* `pip install [--user] pipx`

  After all, you can drop the idea of isolation and install `pipx` using only `pip`. It is the officially recommended way<sup>†</sup>. [Here][pipx-bootstrapping-rejection] is an explanation.

---

<sup>†</sup> I am personally against the idea of installing any package with dependencies (as of May 2020, `pipx` has more than five dependencies counting transitive ones) in system/user site directories. It could break other packages due to version conflicts.


[pipx-homepage]: https://pipxproject.github.io/pipx/
[venv-docs]: https://docs.python.org/3/library/venv.html
[pipx-in-pipx-github]: https://github.com/mattsb42/pipx-in-pipx
[pipx-bootstrap-comment]: https://github.com/pipxproject/pipx/issues/44#issuecomment-458007960
[pipx-bootstrap-github-copy]: https://github.com/pmav99/pipx-bootstrap
[pipx-bootstrapping-rejection]: https://github.com/pipxproject/pipx/pull/160#issuecomment-490183821

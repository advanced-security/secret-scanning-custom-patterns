# Test Custom Secret Scanning patterns

This test Python script uses Intel's `hyperscan` to test custom GitHub Advanced Security Secret Scanning patterns.

## Usage

First run `make requirements` to install required dependencies.

``` bash
./test.py
```

By default it searches the directory above the `testing` directory for `pattern.yml` files, and tests those patterns on the same directory that file was found in.

or

``` bash
./test.py --tests <directory>
```

For full usage use `./test.py --help`

## Requirements

This only works on Intel-compatible platforms, since `hyperscan` is an Intel application and written to use Intel-specific instructions.

* Python 3.9
* `hyperscan` module, which provides Python bindings to Intel's Hyperscan
* `python-pcre` module, which provides Python bindings to libPCRE

## Development notes

Please run `make lint` after any changes


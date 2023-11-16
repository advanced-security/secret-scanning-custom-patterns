# Secret Scanning Tools

> ℹ️ This is an _unofficial_ tool created by Field Security Services, and is not officially supported by GitHub.

This is a testing suite for GitHub Secret Scanning Custom Patterns.

It can be used in combination with GitHub Actions to test custom patterns before they are deployed.

An example repository that uses this Action is [advanced-security/secret-scanning-custom-patterns](https://github.com/advanced-security/secret-scanning-custom-patterns).

A sample custom patterns config file compatible with this tool suite is provided in [`examples/config/patterns.yml`](examples/config/patterns.yml).

## Usage in Actions

```yaml
- name: Secret Scanning Test Suite
  uses: advanced-security/secret-scanning-tools@main
```

### Advanced Configuration

```yaml
- name: Secret Scanning Test Suite
  uses: advanced-security/secret-scanning-tools@main
  with:
    # Modes to run
    # > 'validate' (default), 'all', 'snapshot', 'markdown'
    mode: 'validate'
```

### Using GitHub App Token

```yaml
- name: Get Token
  id: get_workflow_token
  uses: peter-murray/workflow-application-token-action@v1
  with:
    application_id: ${{ secrets.ADVANCED_SECURITY_APP_ID }}
    application_private_key: ${{ secrets.ADVANCED_SECURITY_APP_KEY }}

- name: Secret Scanning Test Suite
  uses: advanced-security/secret-scanning-tools@main
  with:
    token: ${{ steps.get_workflow_token.outputs.token }}
```

## Offline testing of Secret Scanning custom patterns

We have a test Python script, `secretscanning/test.py` that uses Intel's `hyperscan` to test custom GitHub Advanced Security Secret Scanning patterns.

This is useful for thorough testing of patterns before they are deployed, whereas the rest of the test suite is primarily designed to be run in GitHub Actions for testing in CI.

### Local test script usage

Change directory to `secretscanning`.

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

### Local test script requirements

This only works on Intel-compatible platforms, since `hyperscan` is an Intel application and written to use Intel-specific instructions.

* Python 3.9+
* `hyperscan` module, which provides Python bindings to Intel's Hyperscan
* `python-pcre` module, which provides Python bindings to libPCRE

### Development notes

Please run `make lint` after any changes

## License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](LICENSE) for the full terms.

## Maintainers

See [CODEOWNERS](CODEOWNERS) for the list of maintainers.

## Support

> ℹ️ This is an _unofficial_ tool created by Field Security Services, and is not officially supported by GitHub.

See the [SUPPORT](SUPPORT.md) file.

## Background

See the [CHANGELOG](CHANGELOG.md), [CONTRIBUTING](CONTRIBUTING.md), [SECURITY](SECURITY.md), [SUPPORT](SUPPORT.md), [CODE OF CONDUCT](CODE_OF_CONDUCT.md) and [PRIVACY](PRIVACY.md) files for more information.

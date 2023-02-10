# custom-pattern-secrets

Custom Secret Scanning Patterns repository created and maintained by the GitHub Field Services.

This repository extends the [list of supported Vendors out of the box](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/secret-scanning-patterns) with GitHub's Advanced Security Secret Scanning.

> :warning: This repository does not guarantee the quality or precision of the patterns which might result in False Positives

{% for path, config in configs.items() %}
### [{{ config.name }}]({{ config.path.replace("/patterns.yml", "") }})
{% for pattern in config.patterns %}
{%- if pattern.experimental == False %}
- {{ pattern.name }}
{%- endif %}
{%- endfor %}

{% endfor %}

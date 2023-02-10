<!-- WARNING: This README is generated automatically
-->
# {{ config.name }}
{%- for pattern in config.patterns %}

## {{ pattern.name }}

{% if pattern.experimental -%}
**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
{%- endif %}
{% if pattern.description -%}
{{ pattern.description }}
{%- endif %}
*version: {{ pattern.regex.version }}*

{% if pattern.comments -%}
**Comments / Notes:**
{% for comment in pattern.comments %}
- {{ comment }}
{%- endfor %}
{% endif %}

<details>
<summary>Pattern Format</summary>
<p>

```regex
{{ pattern.regex.pattern }}
```

</p>
</details>

{% if pattern.regex.start -%}
<details>
<summary>Start Pattern</summary>
<p>

```regex
{{ pattern.regex.start }}
```

</p>
</details>
{%- endif %}

{%- if pattern.regex.end -%}
<details>
<summary>End Pattern</summary>
<p>

```regex
{{ pattern.regex.end }}
```

</p>
</details>
{%- endif %}

{%- if pattern.regex.additional_match or pattern.regex.additional_not_match %}
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).

{% for match in pattern.regex.additional_match %}
- Match: `{{ match }}`
{%- endfor %}
{%- for match in pattern.regex.additional_not_match %}
- Not Match: `{{ match }}`
{%- endfor %}

</p>
</details>
{%- endif %}
{%- endfor %}

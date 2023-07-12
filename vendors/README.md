<!-- WARNING: This README is generated automatically
-->
# Vendors

## Azure SQL Connection String


<details>
<summary>Pattern Format</summary>
<p>

```regex
(?i)[a-z][a-z0-9-]+\.database(?:\.secure)?\.(?:(?:windows|usgovcloudapi)\.net|chinacloudapi\.cn|cloudapi\.de)
```

**Comments / Notes:**

- Current Version: v0.1
- Removed from Secret Scanning for private repositories: https://github.blog/changelog/2021-10-18-secret-scanning-no-longer-supports-azure-sql-connection-strings-in-private-repos/
</p>
</details>



## Grafana API token


<details>
<summary>Pattern Format</summary>
<p>

```regex
eyJrIjoi[A-Za-z0-9_=-]{42}
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>



## SendGrid (deprecated)


<details>
<summary>Pattern Format</summary>
<p>

```regex
SG\.[a-zA-Z0-9-]{5,}\.[a-zA-Z0-9-]{5,}
```

**Comments / Notes:**

- Current Version: v0.1
- Deprecated (supported by Secret Scanning)
</p>
</details>


<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^a-zA-Z0-9-]
```

</p>
</details>

## Sentry Auth Token



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-fA-F0-9]{64}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
(?:\A|[\r\n])(?:\[auth\][^[]*\ntoken=|(?:export )?SENTRY_AUTH_TOKEN=|sentry-cli [^\r\n]*--auth-token |auth\.token=)
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|\s
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Match: `\d\D|\D\d`

</p>
</details>

## Sentry API Key



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-fA-F0-9]{32}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
(?:\A|[\r\n])(?:\[auth\][^[]*\napi_key=|(?:export )?SENTRY_API_KEY=|sentry-cli [^\r\n]*--api-key |auth\.api_key=)
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|\s
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Match: `\d\D|\D\d`

</p>
</details>

## Sentry DSN secret



*version: v0.1*

**Comments / Notes:**

- The secret part of the DSN is optional and effectively deprecated, and should be removed from the DSN: https://docs.sentry.io/product/sentry-basics/dsn-explainer


<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-fA-F0-9]{32}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
https://[a-fA-F0-9]{32}:
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
@([a-z0-9-.]+\.)?sentry\.io(?:/[^?#]*)?/\d+
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Match: `\d\D|\D\d`

</p>
</details>

## Sentry webpack plugin token



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{64})
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
new SentryPlugin\(\s*\{[^}]*[,\n \t]apiKey:\s*['"]
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
['"]
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Match: `\d\D|\D\d`

</p>
</details>

## Sentry Terraform provider token



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-fA-F0-9]{64}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
(?:\A|[\r\n])provider "sentry" {[^}]*[\n \t]token\s*=\s*['"]
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
['"]
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Match: `\d\D|\D\d`

</p>
</details>

## Okta token


<details>
<summary>Pattern Format</summary>
<p>

```regex
(0{2}[0-9A-Za-z_-]{40})
```

**Comments / Notes:**

- Current Version: v0.1
- Okta token, starting with `00` and 40 random alphanumeric with _ and -
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
(\A|[^0-9A-Za-z_+/-])
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
(\z|[^0-9A-Za-z_+/=-])
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `[0-9A-Fa-f-]{30}`
- Not Match: `[a-zA-Z_-]{30}`
- Not Match: `^\d+(\.\d+)?e[+-]?\d+$`
- Not Match: `[\d_]{30}`

</p>
</details>

## DataDog API key



*version: v0.1*

**Comments / Notes:**

- Looks for surrounding context to confirm this is a DataDog API key, not some other 32-byte hex string


<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-f0-9]{32}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
(\A|\b)(((?i)(DD|DATADOG)_API_KEY)['"]?\s*(value)?[=:,]\s*['"]?|new DataDogWinston\({[^}]*apiKey:\s*'|terraformer import datadog [^\n]*--api-key=|provider "datadog" {[^}]*api_key\s*=\s*")
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|\b
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `^0+$`
- Not Match: `^1+$`
- Not Match: `^ef8d5de700e7989468166c40fc8a0ccd$`
- Not Match: `^(a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5|1234567890abcdef1234567890abcdef)$`

</p>
</details>

## DataDog APP key



*version: v0.1*

**Comments / Notes:**

- Looks for surrounding context to confirm this is a DataDog App key, not some other 40-byte hex string


<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-f0-9]{40}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
(\A|\b)(((?i)(DD|DATADOG)_APP(LICATION)?_KEY)['"]?\s*(value)?[=:,]\s*['"]?|new DataDogWinston\({[^}]*apiKey:\s*'|terraformer import datadog [^\n]*--api-key=|provider "datadog" {[^}]*api_key\s*=\s*")
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|\b
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `^0+$`
- Not Match: `^1+$`
- Not Match: `a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9`

</p>
</details>
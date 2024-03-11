<!-- WARNING: This README is generated automatically
-->

<!-- markdownlint-disable no-inline-html -->

# Vendors

## Azure SQL Connection String



_version: v0.1_

**Comments / Notes:**


- Removed from Secret Scanning for private repositories: https://github.blog/changelog/2021-10-18-secret-scanning-no-longer-supports-azure-sql-connection-strings-in-private-repos/
  

<details>
<summary>Pattern Format</summary>

```regex
(?i)[a-z][a-z0-9-]+\.database(?:\.secure)?\.(?:(?:windows|usgovcloudapi)\.net|chinacloudapi\.cn|cloudapi\.de)
```

</details>



## Grafana API token



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
eyJrIjoi[A-Za-z0-9_=-]{42}
```

</details>



## SendGrid (deprecated)



_version: v0.1_

**Comments / Notes:**


- Deprecated (supported by Secret Scanning)
  

<details>
<summary>Pattern Format</summary>

```regex
SG\.[a-zA-Z0-9-]{5,}\.[a-zA-Z0-9-]{5,}
```

</details>

<details>
<summary>End Pattern</summary>

```regex
\z|[^a-zA-Z0-9-]
```

</details>

## Sentry Auth Token



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-fA-F0-9]{64}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\A|[\r\n])(?:\[auth\][^[]*\ntoken\s*=|(?:export )?SENTRY_AUTH_TOKEN\s*=|sentry-cli [^\r\n]*--auth-token |auth\.token\s*=)\s*['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\s|['"`]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  \d\D|\D\d
  ```

</details>

## Sentry API Key



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-fA-F0-9]{32}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\A|[\r\n])(?:\[auth\][^[]*\napi_key\s*=|(?:export )?SENTRY_API_KEY\s*=|sentry-cli [^\r\n]*--api-key |auth\.api_key\s*=)\s*['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\s|['"`]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  \d\D|\D\d
  ```

</details>

## Sentry DSN secret



_version: v0.1_

**Comments / Notes:**


- The secret part of the DSN is optional and effectively deprecated, and should be removed from the DSN: https://docs.sentry.io/product/sentry-basics/dsn-explainer
  

<details>
<summary>Pattern Format</summary>

```regex
[a-fA-F0-9]{32}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
https://[a-fA-F0-9]{32}:
```

</details><details>
<summary>End Pattern</summary>

```regex
@([a-z0-9-.]+\.)?sentry\.io(?:/[^?#]*)?/\d+
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  \d\D|\D\d
  ```

</details>

## Sentry webpack plugin token



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{64})
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
new SentryPlugin\(\s*\{[^}]*[,\n \t]apiKey:\s*['"]
```

</details><details>
<summary>End Pattern</summary>

```regex
['"]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  \d\D|\D\d
  ```

</details>

## Sentry Terraform provider token



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-fA-F0-9]{64}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\A|[\r\n])provider "sentry" {[^}]*[\n \t]token\s*=\s*['"]
```

</details><details>
<summary>End Pattern</summary>

```regex
['"]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  \d\D|\D\d
  ```

</details>

## Okta token



_version: v0.1_

**Comments / Notes:**


- Okta token, starting with `00` and 40 random alphanumeric with _ and -
  

<details>
<summary>Pattern Format</summary>

```regex
(0{2}[0-9A-Za-z_-]{40})
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|[^0-9A-Za-z_+/-])
```

</details><details>
<summary>End Pattern</summary>

```regex
(\z|[^0-9A-Za-z_+/=-])
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  [0-9A-Fa-f-]{30}
  ```
- Not Match:

  ```regex
  [a-zA-Z_-]{30}
  ```
- Not Match:

  ```regex
  ^\d+(\.\d+)?e[+-]?\d+$
  ```
- Not Match:

  ```regex
  [\d_]{30}
  ```

</details>

## DataDog API key



_version: v0.1_

**Comments / Notes:**


- Looks for surrounding context to confirm this is a DataDog API key, not some other 32-byte hex string
  

<details>
<summary>Pattern Format</summary>

```regex
[a-f0-9]{32}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(((?i)(DD|DATADOG)_API_KEY)['"]?\s*(value)?[=:,]\s*['"]?|new DataDogWinston\({[^}]*apiKey:\s*'|terraformer import datadog [^\n]*--api-key=|provider "datadog" {[^}]*api_key\s*=\s*")
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\b
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^0+$
  ```
- Not Match:

  ```regex
  ^1+$
  ```
- Not Match:

  ```regex
  ^ef8d5de700e7989468166c40fc8a0ccd$
  ```
- Not Match:

  ```regex
  ^(a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5|1234567890abcdef1234567890abcdef)$
  ```

</details>

## DataDog APP key



_version: v0.1_

**Comments / Notes:**


- Looks for surrounding context to confirm this is a DataDog App key, not some other 40-byte hex string
  

<details>
<summary>Pattern Format</summary>

```regex
[a-f0-9]{40}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(((?i)(DD|DATADOG)_APP(LICATION)?_KEY)['"]?\s*(value)?[=:,]\s*['"]?|new DataDogWinston\({[^}]*apiKey:\s*'|terraformer import datadog [^\n]*--api-key=|provider "datadog" {[^}]*api_key\s*=\s*")
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\b
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^0+$
  ```
- Not Match:

  ```regex
  ^1+$
  ```
- Not Match:

  ```regex
  a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9
  ```

</details>

## Microsoft Teams incoming webhook



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
https://[a-z-]+\.webhook\.office\.com/webhookb2/[a-fA-F0-9]{8}-([a-fA-F0-9]{4}-){3}[a-fA-F0-9]{12}@[a-fA-F0-9]{8}-([a-fA-F0-9]{4}-){3}[a-fA-F0-9]{12}/[^/]+/[a-fA-F0-9]{32}/[a-fA-F0-9]{8}-([a-fA-F0-9]{4}-){3}[a-fA-F0-9]{12}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|\b
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\b
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^https://contoso\.
  ```

</details>

## LaunchDarkly API key



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
api-[a-f0-9-]{8}-[a-f0-9-]{4}-[a-f0-9-]{4}-[a-f0-9-]{4}-[a-f0-9-]{12}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|\b
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\b
```

</details>

## PagerDuty API/Service key



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[A-Za-z0-9_-]{20}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(?i)pd_(service|api)_key['"`]?\s*([:=]|[?:]=|[=-]>|,)\s*['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\b
```

</details>

## Flickr OAuth token



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[0-9]{17}-[0-9a-f]{16}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)oauth_token=
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\b
```

</details>

## Flickr API key



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[0-9a-f]{32}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
https:\/\/api\.flickr\.com\/services\/rest\/?([^ ]+&)?api_key=
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\b
```

</details>

## BrowserStack access key



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[0-9a-zA-Z]{20}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(?i)_?(browserstack|bs|automate)_?\.?((Access|Auth)_?Key|Password)['"`]?\s*([:=]|[?:]=|[=-]>|,)\s*['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^a-zA-Z0-9/+_-]
```

</details>

## BrowserStack access key (imprecise)



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[0-9a-zA-Z]{20}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(?i)_?(Access|Auth)_?Key['"`]?\s*([:=]|[?:]=|[=-]>|,)\s*['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^a-zA-Z0-9/+_-]
```

</details>

## BrowserStack token (URL)



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[^:]+:[0-9a-zA-Z]{20}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
https?://
```

</details><details>
<summary>End Pattern</summary>

```regex
@hub-cloud\.browserstack\.com/
```

</details>

## Vercel Access Token (imprecise)



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[A-Za-z0-9]{24}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b|[_.-])(?i)vercel[_.-]?((access|api)[_.-]?)?token\s*[=:]\s*['"]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\s|['"]
```

</details>

## Vercel Access Token



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[A-Za-z0-9]{24}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(?i)vercel[_.-]?((access|api)[_.-]?)?token\s*[=:]\s*['"]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\s|['"]
```

</details>

## Vercel CLI token



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[A-Za-z0-9]{24}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)vercel [^\r\n]*--token=
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|\s
```

</details>

## Vercel OAuth client secrets



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[A-Za-z0-9]{24}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)client[._]?Id[:=]\s*['"]?oac_[A-Za-z0-9]{24}['"]?[^\n]*\n[^\n]*client[._]?Secret\s*[:=]\s*['"]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^A-Za-z.+/=_-]
```

</details>

## UUIDv4 Bearer token (maybe Heroku)



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\b|\A)(?i)Bearer
```

</details><details>
<summary>End Pattern</summary>

```regex
\b|\z
```

</details>
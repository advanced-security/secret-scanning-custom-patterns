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
(?:(?:\A|[\r\n])\[auth\][^[]*\ntoken\s*=|(?:\A|\b)SENTRY_AUTH_TOKEN\s*=|(?:\A|\b)sentry-cli [^\r\n]*--auth-token |(?:\A|\b)auth\.token\s*=)\s*['"`]?
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
(?:(?:\A|[\r\n])\[auth\][^[]*\napi_key\s*=|(?:\A|\b)SENTRY_API_KEY\s*=|(?:\A|\b)sentry-cli [^\r\n]*--api-key |(?:\A|\b)auth\.api_key\s*=)\s*['"`]?
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

## Okta API key (precise)



_version: v0.1_

**Comments / Notes:**


- Uses surrounding context to reduce false positives

- Either `SSWS ` then the token, or a variable starting `okta` followed by an assignment operator, then the token
  

<details>
<summary>Pattern Format</summary>

```regex
0{2}[0-9A-Za-z_-]{40}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\bSSWS\s{1,5}|(?i)okta[_-]?(api[_-]?)?(token|key|secret)\s{0,28}([:=]|[=-]>|to|[!=]={1,2}|<>)\s{0,28}['"`]?)
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^0-9A-Za-z_+/=-]
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


LaunchDarkly API or SDK key
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
(api|sdk)-[a-f0-9-]{8}-[a-f0-9-]{4}-[a-f0-9-]{4}-[a-f0-9-]{4}-[a-f0-9-]{12}
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

**Comments / Notes:**


- Looks for surrounding context to confirm this is a PagerDuty API key, not some other 20-byte alphanumeric string

- The `Token token=` prefix is used in an Authorization header; it's possible that a different vendor could use a similar key and this same prefix, causing results that are a different vendor's key
  

<details>
<summary>Pattern Format</summary>

```regex
[A-Za-z0-9_-]{20}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(?i)((pd|pagerduty)_(service|api)_key['"`]?\s*([:=]|[?:]=|[=-]>)\s*['"`]?|Token token=)
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



- Match:

  ```regex
  [A-Z]
  ```

- Match:

  ```regex
  [a-z]
  ```
- Not Match:

  ```regex
  ^(pagerduty|pd)_(service|api)_
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
(\b|\A)(?i)Bearer[ ]
```

</details><details>
<summary>End Pattern</summary>

```regex
\b|\z
```

</details>

## Azure client secret



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-zA-Z0-9~_.-]{34}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)(client|azure[a-z_.-]{0,10})(key|secret|password|pwd|token)[a-z_.-]{0,9}\b['"`]?(\s{0,5}[\]\)])?\s{0,3}([:,=]|[=-]>|to|[!=]={1,2}|<>)?\s{0,5}([[{])?['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|["'`]|\s
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  [A-Z][a-z]|[A-Z][a-z]
  ```

- Match:

  ```regex
  [0-9][A-Za-z]|[A-Za-z][0-9]
  ```

- Match:

  ```regex
  [.~_-][A-Za-z0-9]|[A-Za-z0-9][.~_-]
  ```

</details>

## Google private key id (or older API key)



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-fA-F0-9]{40}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)(private_key_id|google_api_key)['"`]?(\s*[\]\)])?\s*([:,=]|[=-]>|to|[!=]={1,2}|<>)?\s*([[{])?['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\b|\z
```

</details>

## OpenStack password/API key


OpenStack password or API key
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[^'",\r\n \t\x00-\x08]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)OPEN_?STACK_(PASSWORD|API_?KEY)[_A-Z]*['"`]?(\s*[\]\)])?\s*([:,=]|[=-]>|to|[!=]={1,2}|<>)?\s*([[{])?['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
['"\r\n,]|\z
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(ENV|[a-z_]+)\[$
  ```
- Not Match:

  ```regex
  ^<%=.*%>$
  ```
- Not Match:

  ```regex
  ^([a-z_]+\.api_?key|self\.[a-z_]+|os\.environ\.get\()$
  ```
- Not Match:

  ```regex
  ^(\$\{?[A-Z]+\}?|<password>|\s+)$
  ```
- Not Match:

  ```regex
  ^(@?[a-z_]+\[:.*\]|@[a-z_]+)$
  ```

</details>

## AlienVault OTX API key


AlienVault OTX API key
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-f0-9]{64}|[a-f0-9]{40}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)ALIENVAULT(_?OTX)?(_?API)?_?KEY['"`]?(\s*[\]\)])?\s*([:,=]|[=-]>|to|[!=]={1,2}|<>)?\s*([[{])?['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
['"`\r\n,]|\z
```

</details>

## Apollo.io API key


Apollo.io API key
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
service:[A-Za-z0-9-]+:[^\s'"`,\x00-\x08\x7f-\xff]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)key['"`]?(\s*[\]\)])?\s*([:,=]|[=-]>|to|[!=]={1,2}|<>)?\s*([[{])?['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
['"`,]|\z|\s
```

</details>

## ClickUp API key


ClickUp API key
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
pk_[0-9]{6,8}_[A-Z0-9]{32}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\b|\A
```

</details><details>
<summary>End Pattern</summary>

```regex
\b|\z
```

</details>

## Amazon MWS Auth Token


Amazon MWS Auth Token
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\b|\A
```

</details><details>
<summary>End Pattern</summary>

```regex
\b|\z
```

</details>

## Jenkins API token


Jenkins API token
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-f0-9]{32,64}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)jenkins_?(api[_-]?)?(token|secret|key)['"`]?(\s*[\]\)])?\s*([:,=]|[=-]>|to|[!=]={1,2}|<>)?\s*([[{])?['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
['"`\r\n,]|\z
```

</details>

## AWS S3 presigned URL


AWS S3 presigned URL
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
https://[a-z-]+\.s3\.amazonaws\.com/[^?\s'"`\r\n]+\?[^\s'"`\r\n]+&X-Amz-Signature=[^\s'"`\r\n]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\b|\A
```

</details><details>
<summary>End Pattern</summary>

```regex
['"`\r\n,]|\z
```

</details>

## Azure Access Key (legacy format)


Azure Access Key in context in a variable assignment - legacy key format without internal identifiable features
_version: v0.1_

**Comments / Notes:**


- This is a legacy format for Azure Access Keys. The key is base64 encoded and encodes a fixed length key, so we know its length and that it always end in `==`.

- The key lacks internal identifiable features, which are used in modern keys issued by these Azure services.

- The use of `+` instead of `{86}` in the regex pattern is due to limitations of secret scanning - make sure you use the "additional match" to constrain the length
  

<details>
<summary>Pattern Format</summary>

```regex
[A-Za-z0-9/+]+==
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\A|\b)(?i)(AZURE|ACCOUNT)(_?ACCESS|_?STORAGE(_?ACCOUNT)?)?_?KEY['"`]?(\s*[\]\)])?\s*([:,=]|[=-]>|to|[!=]={1,2}|<>)?\s*([[{])?['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
['"`\r\n,]|\z
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).



- Match:

  ```regex
  ^[A-Za-z0-9/+]{86}==$
  ```

</details>

## Azure Shared Access Signature (SAS) Token


Azure Shared Access Signature (SAS) Token
_version: v0.1_

**Comments / Notes:**


- This is a Shared Access Signature (SAS) token for Azure services. See [these examples](https://learn.microsoft.com/en-us/rest/api/storageservices/service-sas-examples)

- The token is a URL query string parameter, and the signature is a base64 encoded HMAC-SHA256 hash, so is a fixed length in plain text and always ends in =

- When encoded in a URL, the `+` character is replaced with `%2B`, the `/` character is replaced with `%2F`, and the `=` character is replaced with `%3D`

- Because of the variable length of the characters (beacuse of the URL encoding), we use `{43,}` to match the signature

- We ignore `https://files.oaiusercontent.com/` because they are URLs for images generated by ChatGPT
  

<details>
<summary>Pattern Format</summary>

```regex
(https://[^?]+\?)?[^\s?/]*\bsig=([A-Za-z0-9]|%2[bfBF]){43,}%3[dD][^\s?/]*
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\b|\A
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
  (^|&)sv=[0-9]{4}-[0-9]{2}-[0-9]{2}
  ```

- Match:

  ```regex
  (^|&)se=[0-9]{4}-[0-9]{2}-[0-9]{2}
  ```

- Match:

  ```regex
  (^|&)st=[0-9]{4}-[0-9]{2}-[0-9]{2}
  ```
- Not Match:

  ```regex
  ^https://files\.oaiusercontent\.com/
  ```

</details>

## CircleCI API token


CircleCI API token
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[a-f0-9]{40}
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?i)circle[_-]?(ci[_.-]?)?(api[_.-]?)?(token|key)['"`]?(\s*[\]\)])?\s*([:,=]|[=-]>|to|[!=]={1,2}|<>)?\s*([[{])?['"`]?
```

</details><details>
<summary>End Pattern</summary>

```regex
['"`\r\n,]|\z
```

</details>
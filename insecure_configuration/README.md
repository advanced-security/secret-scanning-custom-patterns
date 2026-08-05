<!-- WARNING: This README is generated automatically
-->

<!-- markdownlint-disable no-inline-html -->

# Insecure Configuration

## Cleartext LDAP URL

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Cleartext ldap:// URL. LDAP binds (including the bind DN and password) are
transmitted unencrypted (CWE-319). Use ldaps:// or STARTTLS instead.

_version: v0.1_

**Comments / Notes:**


- Only matches the insecure ldap:// scheme; ldaps:// is intentionally not matched

- Pair with a CodeQL query to confirm the URL reaches an LDAP context/bind sink
  

<details>
<summary>Pattern Format</summary>

```regex
ldap://[a-zA-Z0-9._:\-/]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|[^a-zA-Z0-9]
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|["'`\s,;]
```

</details>

## Insecure trustServerCertificate

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Setting the JDBC trustServerCertificate property to true disables TLS
certificate validation (CWE-295), so the driver accepts any server
certificate and the encrypted channel is unauthenticated (man-in-the-middle).

_version: v0.1_

**Comments / Notes:**


- Matches only the insecure '=true' value; '=false' is not matched

- Case-insensitive on the property name and value, allows spaces around '='

- Pair with a CodeQL query to confirm the URL reaches a JDBC/DB connection sink
  

<details>
<summary>Pattern Format</summary>

```regex
(?i)trustServerCertificate[ \t]*=[ \t]*true
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|[^0-9A-Za-z]
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^0-9A-Za-z]
```

</details>

## Cleartext HTTP endpoint

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
A cleartext http:// endpoint configured against a URL/endpoint key
(CWE-319). Traffic to the endpoint, including any credentials it carries,
crosses the network unencrypted. Use https:// instead.

_version: v0.1_

**Comments / Notes:**


- Anchored on a preceding URL/endpoint-style config key to cut false positives from unrelated http:// URLs (e.g. XML namespaces, schema locations)

- Loopback/localhost endpoints (localhost, 127.0.0.0/8, 0.0.0.0, ::1) are not matched

- Only matches http://; https:// is intentionally not matched

- Pair with a CodeQL query to confirm the URL reaches a network request sink
  

<details>
<summary>Pattern Format</summary>

```regex
http://[^\s"'`<>\\]+
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(?:\A|[^a-zA-Z0-9])(?i)(?:url|uri|endpoint|base[_-]?url|base[_-]?uri|href|callback|webhook|target|location)[ \t]*[:=][ \t]*['"]?
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|['"`\s<>]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^http://(?:localhost|127\.\d{1,3}\.\d{1,3}\.\d{1,3}|0\.0\.0\.0|\[::1\]|::1)(?:[:/?#]|$)
  ```

</details>
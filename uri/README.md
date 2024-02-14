<!-- WARNING: This README is generated automatically
-->

<!-- markdownlint-disable no-inline-html -->

# URI / URL Custom Patterns

## Hardcoded Internal Emails



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[^:@\r\n \t"'/\p{Cc}]+@(internal\.)?example\.com
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|[\s"'`,;=]
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^a-zA-Z._0-9-]
```

</details>

## Hardcoded Internal URLs



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[A-Za-z][A-Za-z0-9+_-]*://([^/?#\s\p{Cc}]*[.@])?(example\.com|internal\.example\.com)[/?#]?[^\s"']*
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|[^A-Za-z0-9+_-]
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[\s'"]
```

</details>

## Hardcoded URI Passwords



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
[^$/?#@\s][^/?#@\s\x00-\x08]*
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
(\b|\A)[A-Za-z][A-Za-z0-9+_-]*://[^/?#:@\s\x00-\x08]*:
```

</details><details>
<summary>End Pattern</summary>

```regex
@[\p{L}\p{N}\.-]*(?:\:[0-9]{1,5})?([/?#\s"'`]|\z)
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  (?i)^[[{(<]?(?:password|passwd|secret)[\]})>]?$
  ```
- Not Match:

  ```regex
  ^\$?\{[^}+]\}i\}$
  ```
- Not Match:

  ```regex
  ^%(?:\.\*)?s$
  ```

</details>

## Routable IPv4 Addresses



_version: v0.1_

**Comments / Notes:**


- False Positives with build versions, but won't match if prefixed with v or ends with -

- Use a custom IPv4 pattern if possible, tailored for the ranges you use

- Doesn't include test, localhost or non-routable IPs

- Does include local ranges such as 192.168.0.0/24
  

<details>
<summary>Pattern Format</summary>

```regex
(?:(?:25[0-5]|(?:2[0-4]|1[0-9]|[1-9]|)[0-9])\.){3}(?:25[0-5]|(?:2[0-4]|1[0-9]|[1-9]|)[0-9])
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|[^v.0-9]
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^.0-9-]
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^(?:0\.0\.0\.0|255\.255\.255\.255)$
  ```
- Not Match:

  ```regex
  ^(?:127|169\.254|224\.0\.0)\..*
  ```
- Not Match:

  ```regex
  ^(?:192\.0.2|198\.51\.100|203\.0\.113|233\.252\.0)\..*
  ```

</details>

## GitHub Container Registry typos



_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
(?:ghrc|gchr|hgcr|ghr|ghc)\.io
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
\A|[^0-9A-Za-z-]
```

</details><details>
<summary>End Pattern</summary>

```regex
\z|[^0-9A-Za-z.-]
```

</details>
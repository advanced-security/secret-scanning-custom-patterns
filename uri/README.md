<!-- WARNING: This README is generated automatically
-->
# URI / URL Custom Patterns

## Hardcoded Internal Emails


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^:@\r\n \t"'/\p{Cc}]+@(internal\.)?example\.com
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
\A|[\s"'`,;=]
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\Z|[^a-zA-Z._0-9-]
```

</p>
</details>

## Hardcoded Internal URLs


<details>
<summary>Pattern Format</summary>
<p>

```regex
[A-Za-z][A-Za-z0-9+_-]*://([^/?#\s\p{Cc}]*[.@])?(example\.com|internal\.example\.com)[/?#]?[^\s"']*
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
\A|[^A-Za-z0-9+_-]
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[\s'"]
```

</p>
</details>

## Hardcoded URI Passwords


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^$/?#@\s][^/?#@\s\p{Cc}]*
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
\b[A-Za-z][A-Za-z0-9+_-]*://[^/?#:@\s\p{Cc}]*:
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
@[\p{L}\p{N}\.-]*(?:\:[0-9]{1,5})?[/?#\s]
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `(?i)^[[{(<]?(?:password|passwd|secret)[\]})>]?$`
- Not Match: `^\$?\{[^}+]\}i\}$`
- Not Match: `^%(?:\.\*)?s$`

</p>
</details>

## Routable IPv4 Addresses


<details>
<summary>Pattern Format</summary>
<p>

```regex
(?:(?:25[0-5]|(?:2[0-4]|1[0-9]|[1-9]|)[0-9])\.){3}(?:25[0-5]|(?:2[0-4]|1[0-9]|[1-9]|)[0-9])
```

**Comments / Notes:**

- Current Version: v0.1
- False Positives with build versions, but won't match if prefixed with v or ends with -
- Use a custom IPv4 pattern if possible, tailored for the ranges you use
- Doesn't include test, localhost or non-routable IPs
- Does include local ranges such as 192.168.0.0/24
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
\A|[^v.0-9]
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^.0-9-]
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `^0\.0\.0\.0$`
- Not Match: `^127\..*`
- Not Match: `^192\.0.2\.`
- Not Match: `^198\.51\.100\.`
- Not Match: `^203\.0\.113\.`
- Not Match: `^233\.252\.0\.`
- Not Match: `^169\.254\.`
- Not Match: `^224\.0\.0\.`
- Not Match: `^255\.255\.255\.255$`

</p>
</details>
<!-- WARNING: This README is generated automatically
-->
# URI / URL Custom Patterns

## Hardcoded Internal Emails



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[^:@\r\n \t"'/\p{Cc}]+@(internal\.)?example\.com
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
\A|[\s"'`,;=]
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\Z|[^a-zA-Z._0-9-]
```

</p>
</details>

## Hardcoded Internal URLs



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[A-Za-z][A-Za-z0-9+_-]*://([^/?#\s\p{Cc}]*[.@])?(example\.com|internal\.example\.com)[/?#]?[^\s"']*
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
\A|[^A-Za-z0-9+_-]
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|[\s'"]
```

</p>
</details>

## Hardcoded URI Passwords



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[^$/?#@\s][^/?#@\s\p{Cc}]*
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
\b[A-Za-z][A-Za-z0-9+_-]*://[^/?#:@\s\p{Cc}]*:
```

</p>
</details><details>
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
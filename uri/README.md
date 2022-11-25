<!-- WARNING: This README is generated automatically
-->
# URI / URL Custom Patterns

## Hardcoded Internal Emails



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[^/'"`][a-z0-9!#$%&'*+/=?^_`{|}~-]+@(example.com|internal.example.com)
```

</p>
</details>



## Hardcoded Internal URLs



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[A-Za-z0-9+-_]+://[a-zA-Z0-9!@:#$%&'*+/=?^_`{|}~-]?(example.com|internal.example.com)[^/#?"']?
```

</p>
</details>



## Hardcoded URI Passwords



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[^$][a-zA-Z0-9!.,$%&*+?^_`{|}\(\)~-]+
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
(A-Za-z0-9)?://[^/?#:]*:
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|[@]|[^a-zA-Z0-9!.,$%&*+?^_`{|}\(\)~-]
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Match: `[^0-9]`

</p>
</details>

<!-- WARNING: This README is generated automatically
-->
# JWT

## JWT


JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties.
*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
e[A-Za-z0-9-_=]{14,}\.e[A-Za-z0-9-_=]{14,}\.?[A-Za-z0-9-_=]*
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z-_\\.]|\A
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
[^0-9A-Za-z-_\\.]|\z
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: `(/|=)`

</p>
</details>
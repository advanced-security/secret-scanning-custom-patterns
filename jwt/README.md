<!-- WARNING: This README is generated automatically
-->

# JWT

## JWT


JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties.
_version: v0.1_



<details>
<summary>Pattern Format</summary>
<p>

```regex
e(?:y[IJ]|yL[CD]|yA[JKgi]|w[ko][JKgi])[A-Za-z0-9_-]{10,}(?:fQ|[3HXn]0|[1BFJNRVZdhlpx]9)={0,2}\.e(?:y[IJ]|yL[CD]|yA[JKgi]|w[ko][JKgi])[A-Za-z0-9_-]{10,}(?:fQ|[3HXn]0|[1BFJNRVZdhlpx]9)={0,2}(?:\.?[A-Za-z0-9_-]+={0,2})?
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z_.-]|\A
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
[^0-9A-Za-z_.=-]|\z
```

</p>
</details>

<details>
<summary>Additional Matches</summary>
<p>
Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match: ```^eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\.eyJrZXkiOiJrZXkxIiwiZXhwIjo[A-Za-z0-9_-]+(JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9|ZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ|mWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0)```

</p>
</details>
<!-- WARNING: This README is generated automatically
-->

<!-- markdownlint-disable no-inline-html -->

# JWT

## JWT


JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties.
_version: v0.1_



<details>
<summary>Pattern Format</summary>

```regex
e(?:y[IJ]|yL[CD]|yA[JKgi]|w[ko][JKgi])[A-Za-z0-9_-]{10,}(?:fQ|[3HXn]0|[1BFJNRVZdhlpx]9)={0,2}\.e(?:y[IJ]|yL[CD]|yA[JKgi]|w[ko][JKgi])[A-Za-z0-9_-]{10,}(?:fQ|[3HXn]0|[1BFJNRVZdhlpx]9)={0,2}(?:\.?[A-Za-z0-9_-]+={0,2})?
```

</details>

<details>
<summary>Start Pattern</summary>

```regex
[^0-9A-Za-z_.-]|\A
```

</details><details>
<summary>End Pattern</summary>

```regex
[^0-9A-Za-z_.=-]|\z
```

</details>

<details>
<summary>Additional Matches</summary>

Add these additional matches to the [Secret Scanning Custom Pattern](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning#example-of-a-custom-pattern-specified-using-additional-requirements).


- Not Match:

  ```regex
  ^eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIs
  ```

</details>
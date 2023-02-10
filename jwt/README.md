<!-- WARNING: This README is generated automatically
-->
# JWT

## JWT

JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties.

<details>
<summary>Pattern Format</summary>
<p>

```regex
e(?:y[IJ]|yL[CD]|yA[JKgi]|w[ko][JKgi])[A-Za-z0-9_-]{10,}(?:fQ|[3HXn]0|[1BFJNRVZdhlpx]9)={0,2}\.e(?:y[IJ]|yL[CD]|yA[JKgi]|w[ko][JKgi])[A-Za-z0-9_-]{10,}(?:fQ|[3HXn]0|[1BFJNRVZdhlpx]9)={0,2}(?:\.?[A-Za-z0-9_-]+={0,2})?
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z_.-]|\A
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
[^0-9A-Za-z_.=-]|\z
```

</p>
</details>
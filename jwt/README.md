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
ey[A-Za-z0-9-_]{12,}[Q90]={0,2}\.ey[A-Za-z0-9-_]{12,}[Q90]={0,2}\.?[A-Za-z0-9-_=]*
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
[^0-9A-Za-z_.-]|\z
```

</p>
</details>
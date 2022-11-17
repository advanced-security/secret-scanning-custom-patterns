<!-- WARNING: This README is generated automatically
-->
# Personally identifiable information (PII)

## Credit Cards



*version: v0.1*

**Comments / Notes:**

- Only supports Visa, MasterCard, and American Express


<details>
<summary>Pattern Format</summary>
<p>

```regex
(4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|(34|37)[0-9]{13})
```

</p>
</details>



## Credit Cards - Visa



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
4[0-9]{12}(?:[0-9]{3})?
```

</p>
</details>



## Credit Cards - MasterCard



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}
```

</p>
</details>



## Credit Cards - American Express



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
(34|37)[0-9]{13}
```

</p>
</details>



## Credit Cards - Discover



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
6(?:011|5[0-9]{2})[0-9]{12}
```

</p>
</details>


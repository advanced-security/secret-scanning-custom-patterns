# Personally identifiable information (PII)

## Credit Cards

<details>
<summary>Pattern Format</summary>
<p>

```regex
(4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|(34|37)[0-9]{13})
```

**Comments / Notes:**

- Current Version: v0.1
- Only supports Visa, MasterCard, and American Express
</p>
</details>



## Credit Cards - Visa

<details>
<summary>Pattern Format</summary>
<p>

```regex
4[0-9]{12}(?:[0-9]{3})?
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>



## Credit Cards - MasterCard

<details>
<summary>Pattern Format</summary>
<p>

```regex
(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>



## Credit Cards - American Express

<details>
<summary>Pattern Format</summary>
<p>

```regex
(34|37)[0-9]{13}
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>



## Credit Cards - Discovery

<details>
<summary>Pattern Format</summary>
<p>

```regex
6(?:011|5[0-9]{2})[0-9]{12}
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>


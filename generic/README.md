<!-- WARNING: This README is generated automatically
-->
# Generic Secrets / Passwords

## Generic Passwords


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\t "'(${{)][a-zA-Z0-9\t !.,$%&*+?^_`{|}()~-]+
```

**Comments / Notes:**

- Current Version: v0.3
- `password`, `secret`, `key`, or password like prefix (fuzzy)
- Delimiters like `=` or `:` (with padding)
- String with a number of chars until a breaking char
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
(?i)((api|jwt|mysql|)?(_|-|.)?((pass|pas)(wd|wrd|word|code|phrase)|pass|pwd|secret|token))([\t ]+|)(=|:)([\t ]+|)("|'|[\t ]|)
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^a-zA-Z0-9\t !.,$%&*+?^_`{|}()~-]|'|"
```

</p>
</details>

## UUIDs


<details>
<summary>Pattern Format</summary>
<p>

```regex
[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>


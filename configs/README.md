# Configuration Secrets

## Generic Passwords

```regex
[^\s"'(${{)][a-zA-Z0-9\s!.,$%&*+?^_`{|}()~-]+
```

**Comments / Notes:**

- Current Version: v0.3
- `password`, `secret`, `key`, or password like prefix (fuzzy)
- Delimiters like `=` or `:` (with padding)
- String with a number of chars until a breaking char

<details>
<summary>Start Pattern</summary>
<p>

```regex
(?i)((api|jwt|mysql|)?(_|-|.)?((pass|pas)(wd|wrd|word|code|phrase)|pass|pwd|secret|token))(\s+|)(=|:)(\s+|)("|'|\s|)
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^a-zA-Z0-9\s!.,$%&*+?^_`{|}()~-]|'|"
```

</p>
</details>

## Hardcoded Spring SQL passwords

```regex
[a-zA-Z0-9!$%&*+?^_`{|}~-]+
```

**Comments / Notes:**

- Current Version: v0.1

<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z](spring.datasource.password|jdbc.password)(\s+|)=(\s+|)
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^0-9A-Za-z]|'
```

</p>
</details>

## Django Secret Key

```regex
[^\s"'(${{)][a-zA-Z0-9!.,$%&*+?^_`{|}()~-]*
```

**Comments / Notes:**

- Current Version: v0.1
- _If the secret is at the start of the file, its not picked up_

<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z](SECRET_KEY)(\s+|)=(\s+|)("|')
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^a-zA-Z0-9\s!.,$%&*+?^_`{|}()~-]|'|"
```

</p>
</details>

## YAML Static Password Fields
**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
This secret pattern has a relative high false positive rate and should be tested on a number of repositories before running on an entire organisation.

```regex
[a-zA-Z0-9%!#$%&*+=?^_-{|}~\.,]{12,32}
```

**Comments / Notes:**

- Current Version: v0.1
- The hardcoded password is between 12 and 32 chars long
- Some false positives in Code might appear
- The pattern only checks for cerain key words to begin the pattern (`secret:`, `password:`, etc.)

<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z](\s+|)(secret|service_pass(wd|word|code|phrase)|pass(wd|word|code|phrase)|key)(\s+|):(\s+|)
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
[^0-9A-Za-z'"\(\)]|\z
```

</p>
</details>
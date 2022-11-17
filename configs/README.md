<!-- WARNING: This README is generated automatically
-->
# Configuration Secrets

## Hardcoded Database Passwords


<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-zA-Z0-9!$%&*+?^_`{|}~-]{1,}
```

**Comments / Notes:**

- Current Version: v0.1
- Checks if the password is null / length of 0
- Supports quoted passwords
- Not case sensative
</p>
</details>


<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z](?i)(postgres|mysql|mysql_root)_password(\s+|)(=|:)(\s+|)('|"|)
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^a-zA-Z0-9!$%&*+?^_`{}|~-]|'|"
```

</p>
</details>

## Hardcoded Spring SQL passwords


Hardcoded JDBC / Spring datasource passwords which typically are in property files or passed in at runtime

*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-zA-Z0-9!$%&*+?^_`{|}~-]+
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z](spring.datasource.password|jdbc.password)(\s+|)=(\s+|)
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^0-9A-Za-z]|'
```

</p>
</details>

## Django Secret Key



*version: v0.1*

**Comments / Notes:**

- _If the secret is at the start of the file, its not picked up_


<details>
<summary>Pattern Format</summary>
<p>

```regex
[^\s"'(${{)][a-zA-Z0-9!.,$%&*+?^_`{|}()~-]*
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z](SECRET_KEY)(\s+|)=(\s+|)("|')
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
\z|[^a-zA-Z0-9\s!.,$%&*+?^_`{|}()~-]|'|"
```

</p>
</details>

## YAML Static Password Fields

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**
Pattern to find Static passwords in YAML configuration files

*version: v0.1*

**Comments / Notes:**

- The hardcoded password is between 12 and 32 chars long
- Some false positives in Code might appear
- The pattern only checks for cerain key words to begin the pattern (`secret:`, `password:`, etc.)


<details>
<summary>Pattern Format</summary>
<p>

```regex
[a-zA-Z0-9%!#$%&*+=?^_-{|}~\.,]{12,32}
```

</p>
</details>

<details>
<summary>Start Pattern</summary>
<p>

```regex
[^0-9A-Za-z](\s+|)(secret|service_pass(wd|word|code|phrase)|pass(wd|word|code|phrase)|key)(\s+|):(\s+|)
```

</p>
</details><details>
<summary>End Pattern</summary>
<p>

```regex
[^0-9A-Za-z'"\(\)]|\z
```

</p>
</details>
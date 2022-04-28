# URI / URL Custom Patterns

## Hardcoded Internal Emails

```regex
[^/'"`][a-z0-9!#$%&'*+/=?^_`{|}~-]+@(example.com|internal.example.com)
```

**Comments / Notes:**

- Current Version: v0.1


## Hardcoded Internal URLs

```regex
[A-Za-z0-9+-_]+://[a-zA-Z0-9!@:#$%&'*+/=?^_`{|}~-]?(example.com|internal.example.com)[^/#?"']?
```

**Comments / Notes:**

- Current Version: v0.1


## Hardcoded URI Passwords

```regex
[^$][a-zA-Z0-9!.,$%&*+?^_`{|}\(\)~-]+
```

**Comments / Notes:**

- Current Version: v0.1

<details>
<summary>Start Pattern</summary>
<p>

```regex
(A-Za-z0-9)?://[^/?#:]*:
```

</p>
</details>
<details>
<summary>End Pattern</summary>
<p>

```regex
\z|[@]|[^a-zA-Z0-9!.,$%&*+?^_`{|}\(\)~-]
```

</p>
</details>
<details>
<summary>Additional Matches</summary>
<p>

</p>
</details>
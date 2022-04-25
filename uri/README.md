# URI / URL Custom Patterns

## Hardcoded Internal Emails

Replacing `example.com|internal.example.com` with a list on organisation domains (separated by pipes `|`) will allow users to find hardcoded org emails.

### Pattern

```
[^/'"`][a-z0-9!#$%&'*+/=?^_`{|}~-]+@(example.com|internal.example.com)
```

## Hardcoded Internal URLs

Replacing `example.com|internal.example.com` with a list on organisation domains (separated by pipes `|`) will allow users to find hardcoded org urls.

### Pattern

```
[A-Za-z0-9+-_]+://[a-zA-Z0-9!@:#$%&'*+/=?^_`{|}~-]?(example.com|internal.example.com)[^/#?"']?
```

**Notes:**

- URIs/URLs need to have a schema / protocol
  - `[A-Za-z0-9+-_]+://`
- This Regex stops once a path / query / fragment is researched
  - `[^/#?"']?`

## Hardcoded URI Passwords

Find passwords in URI/URL strings.

### Pattern

```
[^$][a-zA-Z0-9!.,$%&*+?^_`{|}\(\)~-]+
```

**Notes:**

- `[^$]`: Reduce false positives that are env vars


#### Before Secret

```
(A-Za-z0-9)?://[^/?#:]*:
```

#### After Secret

```
\z|[@]|[^a-zA-Z0-9!.,$%&*+?^_`{|}\(\)~-]
```

#### Additional Match

```
[^0-9]
```

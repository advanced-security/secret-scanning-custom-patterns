# Personally identifiable information (PII)

## Credit Cards

```regex
(4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|(34|37)[0-9]{13})
```

**Comments / Notes:**

- Current Version: v0.1
- Only supports Visa, MasterCard, and American Express


## Credit Cards - Visa

```regex
4[0-9]{12}(?:[0-9]{3})?
```

**Comments / Notes:**

- Current Version: v0.1


## Credit Cards - MasterCard

```regex
(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}
```

**Comments / Notes:**

- Current Version: v0.1


## Credit Cards - American Express

```regex
(34|37)[0-9]{13}
```

**Comments / Notes:**

- Current Version: v0.1


## Credit Cards - Discovery

```regex
6(?:011|5[0-9]{2})[0-9]{12}
```

**Comments / Notes:**

- Current Version: v0.1

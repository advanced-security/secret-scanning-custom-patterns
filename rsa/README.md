<!-- WARNING: This README is generated automatically
-->
# RSA Keys

## Generic RSA keys


<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN (?:[A-Z]+ )?PRIVATE KEY--+(\\r|\\n|)+[a-zA-Z0-9+/=\s]+(\\r|\\n|)+--+END (?:[A-Z]+ )?PRIVATE KEY--
```

**Comments / Notes:**

- Current Version: v1.1
- Basic support for hardcoded strings in code with RSA private key
</p>
</details>



## SSH Private Keys


<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN OPENSSH PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END OPENSSH PRIVATE KEY--
```

**Comments / Notes:**

- Current Version: v0.1
- *SSH Password:* `MyPassword`
</p>
</details>



## GPG Private Key


<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN PGP PRIVATE KEY BLOCK--+(?:[\r\n]+((Version|Comment|MessageID|Hash|Charset): [^\r\n]+[\r\n]+)+[\r\n]+)?[a-zA-Z0-9+/=\s]+--+END PGP PRIVATE KEY BLOCK--
```

**Comments / Notes:**

- Current Version: v0.1
</p>
</details>



## SSH Public Key


**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**

<details>
<summary>Pattern Format</summary>
<p>

```regex
ssh-rsa(\s)+[a-zA-Z0-9\/\+=]{20,}
```

**Comments / Notes:**

- Current Version: v0.2
- SSH Public Key (not a secret)
- Ignores the name of the public key
</p>
</details>


<details>
<summary>End Pattern</summary>
<p>

```regex
\z|(\s)+[a-zA-Z0-9@-]+
```

</p>
</details>
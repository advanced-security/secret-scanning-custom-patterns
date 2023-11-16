<!-- WARNING: This README is generated automatically
-->

# RSA Keys

## Generic RSA keys



_version: v1.2_

**Comments / Notes:**


- Basic support for hardcoded strings in code with RSA private key

- Includes keys hardcoded in strings with escaped line breaks
  

<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN (?:[A-Z]+ )?PRIVATE KEY--+(\\[nr]|[\r\n])+([a-zA-Z0-9+/=\s]|\\[rn])+(\\[rn]|[\r\n])+--+END (?:[A-Z]+ )?PRIVATE KEY--
```

</p>
</details>



## SSH Private Keys



_version: v0.1_

**Comments / Notes:**


- *SSH Password:* `MyPassword`
  

<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN OPENSSH PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END OPENSSH PRIVATE KEY--
```

</p>
</details>



## GPG Private Key



_version: v0.1_



<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN PGP PRIVATE KEY BLOCK--+(?:[\r\n]+((Version|Comment|MessageID|Hash|Charset): [^\r\n]+[\r\n]+)+[\r\n]+)?[a-zA-Z0-9+/=\s]+--+END PGP PRIVATE KEY BLOCK--
```

</p>
</details>



## SSH Public Key

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**

_version: v0.2_

**Comments / Notes:**


- SSH Public Key (not a secret)

- Ignores the name of the public key
  

<details>
<summary>Pattern Format</summary>
<p>

```regex
ssh-rsa(\s)+[a-zA-Z0-9\/\+=]{20,}
```

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
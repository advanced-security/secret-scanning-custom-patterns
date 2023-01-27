<!-- WARNING: This README is generated automatically
-->
# RSA Keys

## Generic RSA keys



*version: v1.1*

**Comments / Notes:**

- Basic support for hardcoded strings in code with RSA private key


<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN (?:[A-Z]+ )?PRIVATE KEY--+(\\r|\\n|)+[a-zA-Z0-9+/=\s]+(\\r|\\n|)+--+END (?:[A-Z]+ )?PRIVATE KEY--
```

</p>
</details>



## SSH Private Keys



*version: v0.1*

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



*version: v0.1*



<details>
<summary>Pattern Format</summary>
<p>

```regex
--BEGIN PGP PRIVATE KEY BLOCK--+[a-zA-Z0-9+/=\s]+--+END PGP PRIVATE KEY BLOCK--
```

</p>
</details>



## SSH Public Key

**⚠️ WARNING: THIS RULE IS EXPERIMENTAL AND MIGHT CAUSE A HIGH FALSE POSITIVE RATE (test before commiting to org level) ⚠️**

*version: v0.2*

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
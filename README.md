# custom-pattern-secrets

Custom Secret Scanning Repo - Created by [@GeekMasher](https://github.com/geekmasher)


## Samples

### RSA (private keys)

Generic RSA keys

```
--BEGIN (?:[A-Z]+ )?PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END (?:[A-Z]+ )?PRIVATE KEY--
```

### SSH (private keys)

```
--BEGIN OPENSSH PRIVATE KEY--+[a-zA-Z0-9+/=\s]+--+END OPENSSH PRIVATE KEY--
```

### GPG (private key)

```
--BEGIN PGP PRIVATE KEY BLOCK--+[a-zA-Z0-9+/=\s]+--+END PGP PRIVATE KEY BLOCK--
```

### [URI Strings](./uri)


### SendGrid

```
SG\.[a-zA-Z0-9-]*\.[a-zA-Z0-9-]*
```

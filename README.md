# custom-pattern-secrets

Custom Secret Scanning Patterns repository created and maintained by the GitHub Field Services.

This repository extends the [list of supported Vendors out of the box](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/secret-scanning-patterns) with GitHub's Advanced Security Secret Scanning.

> :warning: This repository does not guarantee the quality or precision of the patterns which might result in False Positives


### [Configuration Secrets](./configs)

- Hardcoded Database Passwords
- Hardcoded Spring SQL passwords
- Django Secret Key
- GitHub Actions SHA Checker


### [Generic Secrets / Passwords](./generic)

- Generic Passwords
- UUIDs


### [JWT](./jwt)

- JWT


### [Password Stores](./password_store)

- Arc


### [Personally identifiable information (PII)](./pii)

- IBAN
- Credit Cards
- Credit Cards - Visa
- Credit Cards - MasterCard
- Credit Cards - American Express
- Credit Cards - Discover


### [RSA Keys](./rsa)

- Generic RSA keys
- SSH Private Keys
- GPG Private Key


### [URI / URL Custom Patterns](./uri)

- Hardcoded Internal Emails
- Hardcoded Internal URLs
- Hardcoded URI Passwords
- Any IPv4 Addresses


### [Vendors](./vendors)

- Azure SQL Connection String
- Grafana API token
- Okta token
- SendGrid (deprecated)

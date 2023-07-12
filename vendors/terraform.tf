terraform {
  required_providers {
    sentry = {
      source = "jianyuan/sentry"
    }
  }
}

provider "sentry" {
  token = "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
}

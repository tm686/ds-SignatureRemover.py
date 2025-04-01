# ds-SignatureRemover.py

This script removes all <ds:Signature> elements from an XML file, typically used in scenarios such as testing SAML Signature Exclusion vulnerabilities in Single Sign-On (SSO) implementations.

Usage:
```
python3 remove_signature.py saml-response.xml
```
The new file will be created as cleaned_(input_file)


When It Might Not Work:
If the file has namespaced variations (like sig:Signature instead of ds:Signature)

If the XML is malformed (missing closing tags)

If you need to remove only some signatures and preserve others

In those cases, you'd need to tweak the script slightly

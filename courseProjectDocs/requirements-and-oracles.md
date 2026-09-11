# Requirements and Test Oracles

## Functional Requirements
1. **FR-1:** The system shall provide a high-level symmetric encryption recipe (Fernet) that allows users to encrypt and decrypt data with a secret key.
2. **FR-2:** The system shall allow users to generate cryptographically secure keys for use with Fernet.
3. **FR-3:** The system shall provide the ability to parse, inspect, and generate X.509 certificates.
4. **FR-4:** The system shall implement standard cryptographic hash functions (e.g., SHA-256) and return deterministic digests for arbitrary inputs.
5. **FR-5:** The system shall expose low-level cryptographic primitives (such as AES, block cipher modes, and padding) through a "hazardous materials" (hazmat) module.
6. **FR-6:** The system shall allow users to generate asymmetric key pairs (e.g., RSA or Elliptic Curve) for signing and verifying data.

## Non-Functional Requirements
1. **NFR-1:** The system shall ensure performance efficiency for computationally heavy tasks by utilizing Rust extensions and C-bindings (e.g., OpenSSL).
2. **NFR-2:** The system shall provide memory safety in critical paths by leveraging Rust for lower-level implementations.
3. **NFR-3:** The system shall promote safe defaults by restricting inherently dangerous, deprecated, or low-level algorithms to the "hazardous materials" (hazmat) namespace.

## Test Oracles

| Requirement ID | Requirement Description | Test Oracle (Expected Behavior) |
|----------------|-------------------------|---------------------------------|
| FR-1, FR-2 | The system shall provide Fernet encryption and key generation. | **Oracle 1:** If a user generates a Fernet key, uses it to encrypt "secret data", and decrypts the ciphertext with the same key, the output should exactly match "secret data". |
| FR-4 | The system shall implement standard hash functions. | **Oracle 2:** When a user hashes an empty string using SHA-256, the resulting digest must exactly match the standard test vector `e3b0c442...b855`. |
| FR-6 | The system shall allow asymmetric key generation, signing, and verification. | **Oracle 3:** When a user signs a message with a generated RSA private key, they should be able to successfully verify the signature using the corresponding public key. |
| FR-3 | The system shall support X.509 certificate parsing. | **Oracle 4:** When the system loads a valid X.509 PEM certificate, it should successfully parse and expose the correct subject name, issuer, and expiration date. |
| NFR-3 | The system shall sequester dangerous algorithms to `hazmat`. | **Oracle 5:** When a user attempts to use a weak or deprecated algorithm (like MD5) outside of the explicitly named `hazmat` module, the library should prevent it (e.g., it is unavailable in high-level recipes). |
| NFR-1 | The system shall perform cryptographic operations efficiently via Rust/C bindings. | **Oracle 6:** When performing AES encryption on a large payload (e.g., 100MB), execution should be delegated to the underlying bindings and complete within expected performance benchmarks (rather than executing pure Python). |

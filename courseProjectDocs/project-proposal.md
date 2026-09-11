## Overview

`cryptography` is the de facto Python library for all common cryptography applications. It provides encryption through both primitives and recipes (most notably Fernet, a symmetric-key encryption specification, and Cobblestone, a version adapted for streaming), allowing encryption to be integrated in python programs easily and simply with secure default configurations, but also exposing lower-level features for developers with more specific needs. It is developed under the supervision of the Python Cryptographic Authority, which also manages projects like `bcrypt` and `pyopenssl`.

Emphasizing safety, the project is structured so as to encourage the use of Fernet and Cobblestone (as well as X.509) as easy and safe options. Primitives, old/deprecated algorithms, and other low-level utilities are referred to as "hazardous materials" in both the documentation and directory structure.
Software quality has been a focus of the project since its v0.1 release in 2014, which included a robust unit test suite using pytest with parameterization.

---

## Quality Metrics

We plan to collect the following standard maintainability metrics:
- LOC per file
- Comment density
- Cyclomatic complexity  
    source directory 5941
- Number of unit tests
- Unit test coverage
    100%

Within the context of cryptography, there are a plethora of other relevant quality metrics that are difficult to measure in the same ways as the above metrics. These include, for example, ease of use, or robustness of algorithms.

# Metrics how to

This document explains how to run the metrics code to reproduce the results in [The Project Proposal](../../courseProjectDocs/project-proposal.md)

## Lines of Code

The `LOC.py` script calculates the total Lines of Code (LOC) for the repository, grouped by directory and sorted alphabetically. It counts LOC across the following file types: `.py`, `.rs`, `.c`, `.h`, `.cpp`, `.md`, `.rst`, `.toml`, `.json`, `.yaml`, and `.yml`.

To run the script, open your terminal at the root of the repository and execute:

```bash
python courseProjectCode/Metrics/LOC.py
```

The output will list each directory alongside its respective LOC, followed by the total LOC across the entire repository.

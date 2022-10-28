# Learning With Errors (LWE) - Prototypes

Diving into "Learning With Errors" (LWE) via the [Tutorial Series](https://mark-schultz.github.io/nist-standard-out/) by Mark Schultz.

## Setup

1. `git clone <url>`
2. `nix-shell`
3. `python <file>`

_Optional_: Update the `python.formatting.blackPath` property in the `.vscode/settings.json` file. Run `which black` within a Nix shell to get the project-specific `black` path.

## Useful Commands

```sh
nix-shell

python <file>
```

## Useful Resources

- [NIST-PQC Choices Out](https://mark-schultz.github.io/nist-standard-out/)
  - [Textbook RSA and LWE](https://mark-schultz.github.io/lattices-for-programmers-pt1/)
  - [Private Key Lattice-based Encryption](https://mark-schultz.github.io/lattices-for-programmers-pt2/)
  - [Public Key Lattice-based Encryption](https://mark-schultz.github.io/lattices-for-programmers-pt3/)
- [A Guide to Post-Quantum Cryptography](https://mark-schultz.github.io/lattices-for-programmers-pt1/)
- [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf)
- [The Learning with Errors Problem](https://cims.nyu.edu/~regev/papers/lwesurvey.pdf)

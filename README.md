# HTTPS Link Enforcer

A compliance scanner that finds insecure `http://` links in your source code and documentation. It ignores localhost and common XML namespaces.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Smart Detection**: Flags external HTTP links while allowing `localhost` and `w3.org` (often used in DOCTYPEs).
*   **Recursive Scanning**: Checks HTML, Markdown, JS, Python, and JSON files.
*   **Zero Dependencies**: Pure Python.

## Usage

```bash
python run_enforcer.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_enforcer.py src/
```

**2. Check URL list**
```bash
python run_enforcer.py links.txt
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.

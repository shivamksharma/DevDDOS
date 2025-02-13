# DevDDOS

> A powerful load testing and performance analysis tool for web applications

[![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen.svg)](https://github.com/shivamksharma/DevDDOS/releases/tag/v1.0.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![Go](https://img.shields.io/badge/Go-1.16%2B-00ADD8.svg)](https://golang.org/)

DevDDOS is a professional-grade load testing tool designed to evaluate web application performance under high concurrency. It provides detailed insights into how your application behaves under stress, helping you identify bottlenecks and optimize performance.

## 🚀 Key Features

- **Multi-Protocol Support**
  - HTTP/HTTPS protocols
  - WebSocket connections
  - Custom protocol implementations

- **Advanced Load Testing**
  - Configurable concurrent users
  - Adjustable request rates
  - Custom test scenarios
  - Real-time performance metrics

- **Comprehensive Request Customization**
  - Multiple HTTP methods (GET, POST, PUT, DELETE, HEAD)
  - Custom headers and cookies
  - JSON and XML payload support
  - Request body templating

- **Proxy Support**
  - SOCKS5 proxy integration
  - HTTP/HTTPS proxy support
  - Multiple proxy rotation

- **Real-time Analytics**
  - Response time tracking
  - Error rate monitoring
  - Throughput statistics
  - Performance graphs

## 📋 Prerequisites

- Python 3.6 or higher
- Go 1.16 or higher (for Go implementation)
- pip (Python package manager)
- Git

## 🔧 Installation

### Using pip (Recommended)

```bash
pip install devddos
```

### From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/shivamksharma/DevDDOS.git
   cd DevDDOS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the package:
   ```bash
   pip install .
   ```

## 💻 Usage

### Basic Usage

```bash
devddos -u <URL> -c <CONCURRENT_USERS> -r <REQUESTS_PER_SECOND>
```

### Examples

1. Basic load test:
   ```bash
   devddos -u https://example.com -c 1000 -r 100
   ```

2. POST request with JSON payload:
   ```bash
   devddos -u https://api.example.com/data \
           -c 100 \
           -r 10 \
           -m POST \
           -d '{"key":"value"}' \
           -f json
   ```

3. Test with custom headers:
   ```bash
   devddos -u https://example.com \
           -c 500 \
           -r 50 \
           -H "Authorization: Bearer token" \
           -H "Custom-Header: value"
   ```

### Advanced Configuration

```bash
devddos [options]
  -u, --url string          Target URL
  -c, --concurrent int      Number of concurrent users
  -r, --rate int           Requests per second
  -t, --timeout int        Request timeout in seconds
  -m, --method string      HTTP method (GET, POST, PUT, DELETE, HEAD)
  -d, --data string        Request body data
  -f, --format string      Data format (json, xml)
  -H, --header strings     Custom headers
  -C, --cookie strings     Custom cookies
  -p, --proxy string       Proxy URL (SOCKS5/HTTP)
  --duration int           Test duration in seconds
  --output string          Output file for results
```

## 📊 Output and Analysis

DevDDOS provides detailed performance metrics including:

- Response time statistics (min, max, average, percentiles)
- Request throughput
- Error rates and types
- Connection statistics
- Resource utilization

Results can be exported in various formats:
- JSON
- CSV
- HTML reports
- Graph visualizations

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure you update tests and documentation as appropriate.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape DevDDOS
- Inspired by various load testing tools in the open-source community

## ⚠️ Disclaimer

DevDDOS is designed for legitimate performance testing purposes only. Users are responsible for ensuring they have permission to perform load tests on target systems.


# **DevDDOS** - A tool for testing the performance of web applications under high load

[![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen.svg)](https://github.com/shivamksharma/DevDDOS/releases/tag/v1.0.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

DevDDOS is another project in Information Security which is a simple, versatile and easy-to-use tool for testing the performance of web applications under high load. It allows you to simulate a large number of concurrent users accessing your application, and measure how well it handles the load.



## Features

- Simple and easy-to-use command-line interface
- Supports HTTP and HTTPS protocols
- Configurable number of concurrent users and requests per second
- Real-time statistics and graphs
- Customizable headers and cookies
- Support for GET, POST, PUT, DELETE, and HEAD requests
- Support for JSON and XML data formats
- Support for SOCKS5 and HTTP proxies

## Installation

To install DevDDOS, simply clone the repository and run the following command:

```
pip install .
```

## Usage

To use DevDDOS, simply run the following command:

```
devddos -u <URL> -c <CONCURRENT_USERS> -r <REQUESTS_PER_SECOND>
```

For example, to simulate 1000 concurrent users sending 100 requests per second to <https://example.com>, you would run:

```
devddos -u https://example.com -c 1000 -r 100
```

You can also specify custom headers and cookies, as well as the type of request and data format, using the following options:

```
-H <HEADER>
-C <COOKIE>
-m <METHOD>
-d <DATA>
-f <FORMAT>
```

For example, to send a POST request with JSON data to <https://example.com/api>, you would run:

```
devddos -u https://example.com/api -c 100 -r 10 -m POST -d '{"key":"value"}' -f json
```

## Contributing
If you would like to contribute to DevDDOS then you know the drill, please fork the repository and submit a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.


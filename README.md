# Block Traffic with mitmproxy

Need to block all traffic except to a specific list of hosts?

# Use cases

1. A hacking lab with VWs in host only mode but still needing limited access to the internet.
1. Determining which hosts are required for a website to function.
1. Filtering out noise for browser developer tools.

# Usage

```
git clone git@github.com:fx2301/mitmproxy-block-traffic.git
mitmdump -s ./mitmproxy-block-traffic/block_traffic --set allowed_hosts=first.domain.com --set allowed_hosts=second.domain.com --set allowed_hosts=*.anysubdomain.com
```

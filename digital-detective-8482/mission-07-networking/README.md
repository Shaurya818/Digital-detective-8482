# Mission 07 — How computers communicate

## 1. Task / objective

Explain basic network concepts, use Terminal tools to check connectivity and DNS, and describe the steps involved when a browser opens a website.

## 2. Work completed

### Task 7.1 — Network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN (Local Area Network) | Connects devices in a small area. | Computers connected in a home, lab or office. |
| MAN (Metropolitan Area Network) | Connects networks across a town or city-sized area. | A network linking buildings across a city campus. |
| WAN (Wide Area Network) | Covers a large geographical area and can connect smaller networks. | The Internet. |
| DNS (Domain Name System) | Finds the IP address associated with a domain name. | Looking up `example.com` before a browser connects. |
| Router | Connects different networks and forwards data towards its destination. | A home Wi-Fi router connecting devices to an Internet provider. |
| Protocol | A set of agreed rules for communicating. | HTTPS for secure web communication. |
| Packet switching | Splits data into packets that can travel through a network and be reassembled. | Data sent between a browser and a website server. |
| Client-server | A client requests a service or resource and a server responds. | A browser requesting a web page from a web server. |

### Task 7.2 — Network observations

On macOS, use a public example domain for the test:

```bash
ping -c 4 example.com
nslookup example.com
```

`ping` sends test packets and reports whether responses arrive and how long they take. It is a basic connectivity check, although a failed ping does not always mean a website is unavailable because some networks block ping traffic.

`nslookup` asks DNS for information about a domain. Its result can include one or more IP addresses associated with that name. DNS lets a person enter a readable website name instead of having to remember a numeric IP address.

**My observation:** [Run both commands and write whether replies were received and whether DNS returned an address. Results can change depending on the network. Do not paste your own public or local IP address, Wi-Fi name or private network details.]

### Task 7.3 — What happens when I open a website?

1. I enter a website address in the browser. The browser acts as the client.
2. The browser checks whether it already has the required information available; otherwise it needs to find the server's network address.
3. DNS translates the domain name into an IP address that can be used to locate the server.
4. The device sends network packets through its local network and router towards the destination network.
5. The browser and server communicate using protocols such as TCP/IP and HTTPS. The client sends a request for a page or other resource.
6. The server processes the request and sends a response, such as HTML, stylesheets, scripts and images.
7. The browser receives the response, processes the page resources and displays the website on the screen.

## 3. Commands / tools used

- `ping -c 4 example.com` — sends four connectivity test packets.
- `nslookup example.com` — checks DNS information for the example domain.
- Web browser — used to enter a website address and view the response.

## 4. My understanding

A network allows devices to exchange data. DNS helps convert a domain name into an address, and routers forward packets between networks. In the client-server model, the browser requests a resource and the server returns a response. Protocols provide common rules so the devices can communicate.

## 5. Difficulties faced

[Record the actual results. A ping may fail even when normal browsing works, so describe what you observed rather than assuming the Internet is down.]

## 6. How I resolved them

[Record any steps you actually took, such as repeating the test later or checking DNS separately.]

## 7. Evidence / files

- This README
- Optional redacted output from `ping` and `nslookup` in `evidence/`

## 8. Commit details

Suggested commit message: `Explain networking concepts and website communication`

**GitHub status:** [Add the actual commit ID or link after pushing this mission.]

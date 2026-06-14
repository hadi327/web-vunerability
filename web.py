import requests
from urllib.parse import urlparse

t=urlparse
def scan_website(url):
    print(f"\nScanning: {url}\n")

    try:
        response = requests.get(url, timeout=10)

        headers = response.headers

        vulnerabilities = []

        # Check HTTPS
        if not url.startswith("https://"):
            vulnerabilities.append(
                "Website is not using HTTPS."
            )

        # Security Headers
        security_headers = {
            "Content-Security-Policy":
                "Prevents XSS attacks",

            "X-Frame-Options":
                "Prevents clickjacking",

            "X-Content-Type-Options":
                "Prevents MIME sniffing",

            "Strict-Transport-Security":
                "Forces HTTPS"
        }

        for header, reason in security_headers.items():
            if header not in headers:
                vulnerabilities.append(
                    f"Missing {header} ({reason})"
                )

        # Server Disclosure
        if "Server" in headers:
            vulnerabilities.append(
                f"Server Disclosure: {headers['Server']}"
            )

        print("Scan Complete\n")

        if vulnerabilities:
            print("Potential Issues Found:\n")

            for v in vulnerabilities:
                print("-", v)

        else:
            print("No common issues detected.")

        # Save Report
        with open("report.txt", "w") as report:
            report.write(f"Website Scan Report\n")
            report.write(f"Target: {url}\n\n")

            for v in vulnerabilities:
                report.write(v + "\n")

        print("\nReport saved as report.txt")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    target = input("Enter website URL: ")
    scan_website(target)
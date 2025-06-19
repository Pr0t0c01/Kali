import re
import sys
import requests

# List of potentially dangerous JavaScript functions and properties
DOM_SINKS = [
    "innerHTML", "outerHTML", "document.write", "document.writeln", "eval",
    "setTimeout", "setInterval", "Function", "execCommand", "insertAdjacentHTML",
    "document.domain","onevent", "window.location", "document.cookie", "WebSocket", "element.src", "postMessage",
    "setRequestHeader", "FileReader.readAsText", "ExecuteSql", "sessionStorage.setItem", "document.evaluate",
    "JSON.parse", "element.setAttribute", "RegExp"
]

# Regex patterns to identify JavaScript DOM sinks
DOM_SINK_PATTERNS = [re.compile(rf'\b{sink}\b', re.IGNORECASE) for sink in DOM_SINKS]

def analyze_js_code(js_code):
    """
    Analyzes the JavaScript code for potential DOM-based vulnerabilities.

    :param js_code: JavaScript code as a string.
    """
    vulnerabilities = []

    for sink, pattern in zip(DOM_SINKS, DOM_SINK_PATTERNS):
        matches = pattern.findall(js_code)
        if matches:
            vulnerabilities.append(f"Potential use of DOM sink '{sink}' found {len(matches)} time(s).")

    if vulnerabilities:
        print("DOM-Based Vulnerability Analysis Report:")
        for vulnerability in vulnerabilities:
            print(f" - {vulnerability}")
    else:
        print("No potential DOM-based vulnerabilities found.")

def fetch_js_from_url(url):
    """
    Fetches the JavaScript code from the given URL.

    :param url: URL of the JavaScript file.
    :return: JavaScript code as a string.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching JavaScript from URL: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_dom_vulnerabilities.py <url_of_javascript_file>")
    else:
        url = sys.argv[1]
        js_code = fetch_js_from_url(url)
        if js_code:
            analyze_js_code(js_code)

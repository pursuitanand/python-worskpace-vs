#!/usr/bin/env python3

import os
import re
import csv
from pathlib import Path
from urllib.parse import urlparse

WORKSPACE = r"/path/to/workspace"

EXTENSIONS = {
    ".jsp",
    ".jspx",
    ".html",
    ".htm",
    ".js",
    ".tag",
    ".tagx"
}

PATTERNS = {
    # "external_script_tag":
    #     re.compile(r'<script[^>]*src\s*=\s*["\']([^"\']+)["\']',
    #                re.IGNORECASE),
    "external_script_tag_with_http":
        re.compile(
            r'<script[^>]*src\s*=\s*["\'](https?://[^"\']+)["\']',
            re.IGNORECASE
        ),
    "internal_script_tag_self_src":
        re.compile(
            r'<script[^>]*src\s*=\s*["\']((?!https?://)[^"\']+)["\']',
            re.IGNORECASE
        ),
    "http_https_url":
    re.compile(
        r'https?://[^\s"\'>)]+',
        re.IGNORECASE
    ),

    "inline_script":
        re.compile(r'<script(?![^>]*src=)[^>]*>',
                   re.IGNORECASE),

    "inline_event_handler":
        re.compile(
            r'\b(onclick|onchange|onload|onkeyup|onkeydown|'
            r'onblur|onfocus|onsubmit|onmouseover|onmouseout)\s*=',
            re.IGNORECASE
        ),

    "dynamic_script_creation":
        re.compile(
            r'createElement\s*\(\s*[\'"]script[\'"]\s*\)',
            re.IGNORECASE
        ),

    "jquery_getscript":
        re.compile(
            r'(\$|jQuery)\.getScript\s*\(',
            re.IGNORECASE
        ),

    "script_src_assignment":
        re.compile(
            r'\.src\s*=',
            re.IGNORECASE
        ),

    "eval_usage":
        re.compile(
            r'\beval\s*\(',
            re.IGNORECASE
        ),

    "document_write":
        re.compile(
            r'document\.write\s*\(',
            re.IGNORECASE
        )
}


def scan_file(file_path):
    findings = []

    try:
        COMMENT_PATTERNS = [
            r'<!--.*?-->',      # HTML comments
            r'<%--.*?--%>',     # JSP comments
            r'/\*.*?\*/'        # JS block comments
        ]
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            # lines = f.readlines()
            content= f.read()

            for pattern in COMMENT_PATTERNS:
                content = re.sub(
                    pattern,
                    '',
                    content,
                    flags=re.DOTALL
                )
            lines = content.splitlines()

        # for lineno, line in enumerate(lines, start=1):

        #     # SKIP JSP DIRECTIVES
        #     content = re.sub(
        #         pattern,
        #         '',
        #         content,
        #         flags=re.DOTALL
        #     )

        for lineno, line in enumerate(lines, start=1):
            
            # SKIP JSP DIRECTIVES
            if line.strip().startswith("<%@"):
                continue

            # for match in PATTERNS["external_script_tag"].finditer(line):
            #     findings.append([
            #         file_path,
            #         lineno,
            #         "EXTERNAL_SCRIPT",
            #         match.group(1),
            #         line.strip()
            #     ])
            for match in PATTERNS["external_script_tag_with_http"].finditer(line):
                findings.append([
                    file_path,
                    lineno,
                    "EXTERNAL_SCRIPT_TAG_WITH_HTTP",
                    match.group(1),
                    line.strip()
                ])

            for match in PATTERNS["internal_script_tag_self_src"].finditer(line):
                findings.append([
                    file_path,
                    lineno,
                    "INTERNAL_SCRIPT_TAG_SELF_SRC",
                    match.group(1),
                    line.strip()
                ])
            
            for match in PATTERNS["http_https_url"].finditer(line):
                findings.append([
                    file_path,
                    lineno,
                    "HTTP_HTTPS_URL",
                    match.group(0),
                    line.strip()
                ])

            if PATTERNS["inline_script"].search(line):
                findings.append([
                    file_path,
                    lineno,
                    "INLINE_SCRIPT",
                    "",
                    line.strip()
                ])

            if PATTERNS["inline_event_handler"].search(line):
                findings.append([
                    file_path,
                    lineno,
                    "INLINE_EVENT_HANDLER",
                    "",
                    line.strip()
                ])

            if PATTERNS["dynamic_script_creation"].search(line):
                findings.append([
                    file_path,
                    lineno,
                    "DYNAMIC_SCRIPT_CREATION",
                    "",
                    line.strip()
                ])

            if PATTERNS["jquery_getscript"].search(line):
                findings.append([
                    file_path,
                    lineno,
                    "JQUERY_GETSCRIPT",
                    "",
                    line.strip()
                ])

            if PATTERNS["script_src_assignment"].search(line):
                findings.append([
                    file_path,
                    lineno,
                    "SCRIPT_SRC_ASSIGNMENT",
                    "",
                    line.strip()
                ])

            if PATTERNS["eval_usage"].search(line):
                findings.append([
                    file_path,
                    lineno,
                    "EVAL_USAGE",
                    "",
                    line.strip()
                ])

            if PATTERNS["document_write"].search(line):
                findings.append([
                    file_path,
                    lineno,
                    "DOCUMENT_WRITE",
                    "",
                    line.strip()
                ])

    except Exception as ex:
        print(f"Error scanning {file_path}: {ex}")

    return findings


def scan_workspace(root):
    all_findings = []

    for current_root, dirs, files in os.walk(root):

        # Skip common generated folders
        dirs[:] = [
            d for d in dirs
            if d not in {
                ".git",
                "node_modules",
                "target",
                "dist",
                "build"
            }
        ]

        for file in files:

            ext = Path(file).suffix.lower()

            if ext not in EXTENSIONS:
                continue

            full_path = os.path.join(current_root, file)

            findings = scan_file(full_path)

            all_findings.extend(findings)

    return all_findings


def write_csv(findings):

    with open(
        "csp_scan_report.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "File",
            "Line",
            "Issue Type",
            "URL",
            "Code"
        ])

        writer.writerows(findings)


def print_summary(findings):

    summary = {}

    for row in findings:
        issue = row[2]
        summary[issue] = summary.get(issue, 0) + 1

    print("\n==== SUMMARY ====\n")

    for k, v in sorted(summary.items()):
        print(f"{k:30} {v}")

    print(f"\nTotal Findings: {len(findings)}")


def print_domain_summary(findings):

    domains = {}

    for row in findings:

        if row[2] not in (
            "EXTERNAL_SCRIPT_TAG_WITH_HTTP",
            "HTTP_HTTPS_URL"
        ):
            continue

        url = row[3]

        if not url:
            continue

        try:
            domain = urlparse(url).netloc

            domains[domain] = domains.get(domain, 0) + 1

        except Exception:
            pass

    print("\n==== EXTERNAL DOMAINS ====\n")

    for domain, count in sorted(
        domains.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{domain:40} {count}")

if __name__ == "__main__":

    findings = scan_workspace(WORKSPACE)

    write_csv(findings)

    print_summary(findings)
    
    print_domain_summary(findings)

    print("\nReport written to csp_scan_report.csv")
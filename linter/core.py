# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os

class HttpsEnforcer:
    # Match http:// but ignore http://localhost or http://127.0.0.1
    HTTP_PATTERN = re.compile(r'http://[a-zA-Z0-9.-]+')

    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    matches = HttpsEnforcer.HTTP_PATTERN.findall(line)
                    for url in matches:
                        # Ignore local dev URLS
                        if 'localhost' in url or '127.0.0.1' in url or '0.0.0.0' in url:
                            continue
                        # Ignore common XML namespace (e.g. xmlns="http://www.w3.org/...")
                        if 'w3.org' in url or 'schema.org' in url:
                             continue
                             
                        issues.append({
                            'line': line_num,
                            'file': filepath,
                            'url': url,
                            'msg': 'Insecure HTTP link found'
                        })
        except Exception:
            pass
        return issues

    @staticmethod
    def scan_directory(directory, extensions=None):
        if extensions is None:
            extensions = ['.html', '.md', '.js', '.py', '.css', '.json']
            
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    path = os.path.join(root, file)
                    issues = HttpsEnforcer.scan_file(path)
                    all_issues.extend(issues)
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

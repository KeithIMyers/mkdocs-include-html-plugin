import os
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from bs4 import BeautifulSoup

class IncludeHtmlPlugin(BasePlugin):

    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
    )

    def on_post_build(self, config, **kwargs):
        if not self.config['enabled']:
            print("Plugin is disabled")
            return

        site_dir = config['site_dir']
        print(f"Site directory: {site_dir}")

        for root, _, files in os.walk(site_dir):
            print(f"Checking directory: {root}")

            include_html_path = os.path.join(root, '.include.html')
            include_js_path = os.path.join(root, '.include.js')

            include_html_content = self.read_file(include_html_path)
            include_js_content = self.read_file(include_js_path)

            for file in files:
                if file.endswith('.html'):
                    html_file_path = os.path.join(root, file)
                    print(f"Appending content to: {html_file_path}")
                    self.append_include_content(html_file_path, include_html_content, include_js_content)

    def read_file(self, file_path):
        try:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    print(f"Reading file: {file_path}")
                    return file.read()
            else:
                print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Failed to read file {file_path}: {e}")
        return None

    def append_include_content(self, html_file_path, html_content, js_content):
        try:
            with open(html_file_path, 'r+', encoding='utf-8') as html_file:
                soup = BeautifulSoup(html_file, 'html.parser')
                if html_content:
                    include_html_tag = soup.new_tag('div')
                    include_html_tag.append(BeautifulSoup(html_content, 'html.parser'))
                    soup.body.append(include_html_tag)
                if js_content:
                    include_js_tag = soup.new_tag('script')
                    include_js_tag.string = js_content
                    soup.body.append(include_js_tag)
                html_file.seek(0)
                html_file.write(str(soup))
                html_file.truncate()
        except Exception as e:
            print(f"Failed to append content to {html_file_path}: {e}")

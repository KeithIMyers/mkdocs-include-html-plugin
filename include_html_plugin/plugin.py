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
            return

        site_dir = config['site_dir']
        for root, _, files in os.walk(site_dir):
            include_html_path = os.path.join(root, '.include.html')
            include_js_path = os.path.join(root, '.include.js')
            
            include_html_content = self.read_file(include_html_path)
            include_js_content = self.read_file(include_js_path)
            
            for file in files:
                if file.endswith('.html'):
                    html_file_path = os.path.join(root, file)
                    self.append_include_content(html_file_path, include_html_content, include_js_content)

    def read_file(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        return None

    def append_include_content(self, html_file_path, html_content, js_content):
        with open(html_file_path, 'r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')

        if html_content:
            include_html_tag = soup.new_tag('div')
            include_html_tag.append(BeautifulSoup(html_content, 'html.parser'))
            soup.body.append(include_html_tag)

        if js_content:
            include_js_tag = soup.new_tag('script')
            include_js_tag.append(js_content)
            soup.body.append(include_js_tag)

        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(str(soup))

if __name__ == "__main__":
    config = {
        'site_dir': 'site',
        'docs_dir': 'docs',
    }
    plugin = IncludeHtmlPlugin()
    plugin.on_post_build(config)

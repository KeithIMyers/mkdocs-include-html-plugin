# mkdocs-include-html-plugin

**Currently a WIP - Does not yet function as expected**

## Description

This plugin will look for the presence of any of the following files in a directory and if found, they will be appended to all markdown files in that directory during the mkdocs build process.

- .include.html
- .include.js

This allows users of mkdocs to selectively include custom html or javascript in specific pages on a website built with mkdocs instead of sitewide. 

## Installation 

### Install Plugin With pip3

```bash
pip3 install beautifulsoup4
pip3 install git+https://github.com/KeithIMyers/mkdocs-include-html-plugin.git
```

### Include Plugin In Your mkdocs.yml

plugins:
  - include_html_plugin

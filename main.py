import os
import yaml

static_se = 'static-search-engine'
w3m_se = 'w3m-search-engine'

os.makedirs(static_se, exist_ok=True)
os.makedirs(w3m_se, exist_ok=True)

with open('link-page.yml', 'r', encoding="utf-8") as yml:
    linkpage = yaml.safe_load(yml)
    with open(f'{static_se}/index.md', mode='w', encoding="utf-8") as f:
        f.write(
            '# Static Search Engine\n\nJavaScriptが有効でないサイトを見たい方は w3m-search-engine をご利用ください。\n\n')
        for category in linkpage:
            title = category['title']
            url = category['url']
            f.write(f'[{title}]({url})\n')
    with open(f'{w3m_se}/index.md', mode='w', encoding="utf-8") as f:
        f.write(
            '# w3m Search Engine\n\nw3mを使うことを想定したディレクトリ型検索エンジンです。\n\n')
        for category in linkpage:
            title = category['title']
            url = category['url']
            f.write(f'[{title}]({url})\n')
    for category in linkpage:
        category_title = category['title']
        category_url = category['url']
        with open(f'{static_se}/{category_url}.md', mode='w', encoding="utf-8") as f:
            f.write(f'# {category_title}\n\n## Sites\n\n')
            for site in category['sites']:
                title = site['title']
                url = site['url']
                f.write(f'[{title}]({url})\n')
            if 'categories' in category:
                os.makedirs(f'{static_se}/{category_url}', exist_ok=True)
                f.write(f'\n## Categories\n\n')
                for site in category['categories']:
                    title = site['title']
                    url = site['url']
                    f.write(f'[{title}]({url})\n')
        with open(f'{w3m_se}/{category_url}.md', mode='w', encoding="utf-8") as f:
            f.write(f'# {category_title}\n\n## Sites\n\n')
            for site in category['sites']:
                if not site['javascript']:
                    title = site['title']
                    url = site['url']
                    f.write(f'[{title}]({url})\n')
            if 'categories' in category:
                f.write(f'\n## Categories\n\n')
                os.makedirs(f'{w3m_se}/{category_url}', exist_ok=True)
                for site in category['categories']:
                    title = site['title']
                    url = site['url']
                    f.write(f'[{title}]({url})\n')
            f.write(f'\n## JavaScript-needed\n\n')
            for site in category['sites']:
                if site['javascript']:
                    title = site['title']
                    url = site['url']
                    f.write(f'[{title}]({url})\n')

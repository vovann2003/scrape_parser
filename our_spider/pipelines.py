import json
import os

from itemadapter import ItemAdapter


class OurSpiderPipeline:

    def open_spider(self, spider):
        self.files = {}

    def close_spider(self, spider):
        for file in self.files.values():
            file.close()

    def process_item(self, item, spider):
        country = item['country']
        domain = item['domain']
        filename = f"{item['title']}.jsonl".replace(',', '')

        country_dir = os.path.join('data', country)
        domain_dir = os.path.join(country_dir, domain)

        if not os.path.exists(domain_dir):
            os.makedirs(domain_dir)

        file = os.path.join(domain_dir, filename)

        with open(file, 'a', encoding='utf-8') as f:
            line = json.dumps(ItemAdapter(item).asdict()) + "\n"
            f.write(line)
        return item

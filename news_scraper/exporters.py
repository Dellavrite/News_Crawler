from scrapy.exporters import CsvItemExporter


class CsvCustomExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs['encoding'] = 'utf-8'
        kwargs['delimiter'] = '~'
        self.include_headers_line = False
        super(CsvCustomExporter, self).__init__(*args, **kwargs)
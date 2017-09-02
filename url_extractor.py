import re


class UrlExtractor:
    '''
    convert pattern to group match re, re.sub
    match => self.named_re march
    extract => group match to dict
    '''
    def __init__(self, pattern: str):
        self._pattern = pattern
        self._meta_pattern = self._parse_pattern()

    def _parse_pattern(self):
        meta_pattern = re.sub('{([\w_]+)}', r'(?P<\1>[\w_]+)', self._pattern)
        return re.compile(meta_pattern)

    def match(self, url):
        return self._meta_pattern.fullmatch(url)

    def extract(self, url):
        matched = self._meta_pattern.match(url)
        if matched:
            return matched.groupdict()
        return {}

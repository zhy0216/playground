from url_extractor import UrlExtractor


def test_no_para_match():
    url_extractor = UrlExtractor("/api/test")
    assert url_extractor.match("/api/test")
    assert not url_extractor.match("/api/test1")


def test_para_match():
    url_extractor = UrlExtractor("/api/{test}")
    assert url_extractor.match("/api/test")
    assert url_extractor.match("/api/test1")
    assert not url_extractor.match("/api1/test1")


def test_no_para_extraction():
    url_extractor = UrlExtractor("/api/test")
    assert url_extractor.extract("/api/test") == {}


def test_para_extraction():
    url_extractor = UrlExtractor("/api/{test}")
    assert url_extractor.extract("/api/test1") == {"test": "test1"}
from dictfetcher import DictFetcherMixin


d = {
    "a": {
        "b":{
            "abc": "what",
            "aba": "the",
            "aa": "kkk",
            "a": "lala"
        },
        "a": "somevalue",
        "c": {
            "x.y": "except",
            "x": "bug",
            "y": "ssss"
        },
        "g": "deep",
    },
    "b": "to",
    "c": {
        "d": {
            "f":{
                "g": "1234"
            }
        }
    }
}

class DictFetcher(dict, DictFetcherMixin):
    pass

df = DictFetcher(d)

def test_simple_dot_expression():
    assert df["c.d.f.g"]["c.d.f.g"] == "1234"


def test_simple_star_expression():
    assert is_dict_same(df["a.b.ab*"], {"a.b.abc": "what", "a.b.aba": "the"})


def test_question_mark_expression():
    pass

def test_char_choose_expression():
    pass


def test_empty_result():
    pass

def is_dict_same(d1, d2):
    return sorted(d1) == sorted(d2)












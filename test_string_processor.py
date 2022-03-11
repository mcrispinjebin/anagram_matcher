import pytest

from string_processor import AnagramMatcher


PARAMETRIZED_PRE_POPULATE_HASH_MAP = [(['seo', 'eos'], {"eos": ["seo", "eos"]}),
                                      ([], {})]

PARAMETRIZED_FIND = [(['foo', 'seo', 'eos'], 'oes', 'seo, eos'),
                     (['foo', 'seo', 'eos'], 'oof', 'foo'),
                     (['foo', 'seo', 'eos'], 'abc', ''),
                     ([], 'abc', '')]


class TestAnagramMatcher:
    @pytest.mark.test_pre_populate_hash_map
    @pytest.mark.parametrize('input_list, exp_result', PARAMETRIZED_PRE_POPULATE_HASH_MAP)
    def test_pre_populate_hash_map(self, input_list, exp_result):
        matcher = AnagramMatcher(input_list)
        assert matcher.populated_map == exp_result

    @pytest.mark.test_find
    @pytest.mark.parametrize('input_list, match_str, exp_result', PARAMETRIZED_FIND)
    def test_find(self, input_list, match_str, exp_result):
        matcher = AnagramMatcher(input_list)
        result = matcher.find(match_str)
        assert result == exp_result

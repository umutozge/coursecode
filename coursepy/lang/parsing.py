import nltk
from nltk.tokenize import word_tokenize
from nltk import CFG
from nltk.parse import ChartParser

def _parse_sentence(parser, sentence):
    """Map sentence to the set of its parse trees.

       In:
           parser: nltk.parse.chart.ChartParser object
           sentence: str
       Out:
           trees: list of nltk Tree objects
    """
    return\
        list(
            parser.parse(
                word_tokenize(
                    sentence
                )
            )
        )

def make_parser(grammar, parser=ChartParser):
    parser = parser(grammar)
    def f(sentence):
        return _parse_sentence(parser, sentence)
    return f

def make_cfg(rules: str) -> CFG:
    """Make a CFG grammar from the given rules.

       In:
           rules: str, a string representation of the grammar rules
       Out:
           grammar: nltk.CFG object
    """
    return CFG.fromstring(rules)

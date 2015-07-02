from nose.tools import *
from ex48.parser import *

def test_normal():
	x = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
	assert_equal(x.subject, 'bear')
	assert_equal(x.verb, 'eat')
	assert_equal(x.object, 'honey')

def test_exception():
	assert_raises(ParseError, parse_sentence, [('noun', 'bear'), ('verb', 'eat'), ('verb', 'eat'), ('noun', 'honey')]) 

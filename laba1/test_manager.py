from qa.exceptions import CatIsNotFedError, MissTheBusError
from qa.manager import ExceptionManager

import pytest


@pytest.mark.parametrize(
	'errors, critical_counter_expected, regular_counter_expected',
	[
		((), 0, 0),
		((CatIsNotFedError, CatIsNotFedError, CatIsNotFedError, MissTheBusError), 3, 1),
		((MissTheBusError, CatIsNotFedError, MissTheBusError), 1, 2),
	],
)
def test_counter(errors, critical_counter_expected, regular_counter_expected):
	em = ExceptionManager()
	for error in errors:
		em.check(error())

	assert em.critical_exc_counter == critical_counter_expected
	assert em.regular_exc_counter == regular_counter_expected


@pytest.mark.parametrize(
	'error, critical',
	[(CatIsNotFedError, True), (MissTheBusError, False)],
)
def test_is_critical(error, critical):
	em = ExceptionManager()
	assert em.is_critical(error()) is critical

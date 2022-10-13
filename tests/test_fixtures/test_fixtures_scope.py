import pytest
""" default scope is function"""

""" Module in python is file level"""

""" Scope types available to share fixtures in classes, modules, packages or session"""

""" Possible values for scope are: function, class, module, package or session. """


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes


"""
function: the default scope, the fixture is destroyed at the end of the test.

class: the fixture is destroyed during teardown of the last test in the class.

module: the fixture is destroyed during teardown of the last test in the module.

package: the fixture is destroyed during teardown of the last test in the package.

session: the fixture is destroyed at the end of the test session. 

Pytest only caches one instance of a fixture at a time, which means that when using a parametrized fixture, pytest may invoke a fixture more than once in the given scope.
"""



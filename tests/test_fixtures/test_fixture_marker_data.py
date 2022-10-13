import pytest


@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    print("\n")
    print(marker)
    if marker is None:
        # Handle missing marker in some way...
        data = None
    else:
        data = marker.args[0]
    print(data)
    # Do something with the data
    return data


@pytest.mark.fixt_data(42)
def test_fixt(fixt):
    assert fixt == 42


@pytest.fixture
def fixt1(request):
    print("\n")
    print("Requested Test:", request)
    print("Requested Test:", request.module)


def test_request(fixt1):
    assert True


@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")


@pytest.fixture
def make_customer_record():

    created_records = []

    def _make_customer_record(name):
        created_records.append(name)
        return created_records

    yield _make_customer_record

    for record in created_records:
        record.destroy()


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    print(customer_1)
    customer_2 = make_customer_record("Mike")
    print(customer_2)
    customer_3 = make_customer_record("Meredith")
    print(customer_3)
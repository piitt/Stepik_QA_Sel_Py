import pytest


class TestMainPage:

    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self):
        assert 1

    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self):
        assert 1


class TestBasket:

    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self):
        assert 1

    @pytest.mark.smoke
    def test_guest_can_see_total_price(self):
        assert 1


@pytest.mark.skip
class TestBookPage:

    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self):
        assert 1

    @pytest.mark.regression
    def test_guest_can_see_book_price(self):
        assert 1


@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue():
    assert 1

# pytest -v -m "smoke and not beta_users" test_task_mark_run.py

# run test_guest_can_login and test_guest_can_see_total_price

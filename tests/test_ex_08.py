


#тест ex_08
def test_check_stickers(app):
    for count in app.sticker.count_stickers_on_products():
        assert count == 1
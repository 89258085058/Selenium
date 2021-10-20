

#тест ex_07
def test_check_left_menu(app):
    app.admin.check_left_menu()
    app.session.logout()
import pytest


@pytest.fixture
def app():
    from app import create_app
    app = create_app()
    app.testing = True
    return app.test_client()


def test_index(app):
    r = app.get('/')
    assert r.status_code == 200
    assert 'Index' in r.data.decode('utf-8')


def test_dist_no_input(app):
    r = app.get('/distance')
    assert r.status_code == 200
    assert 'Shortest Distance Calculator' in r.data.decode('utf-8')


def test_dist_input(app):
    r = app.post('/distance', data={
        'x1': '0',
        'y1': '0',
        'x2': '5',
        'y2': '5'})
    assert r.status_code == 200
    assert '7.0711' in r.data.decode('utf-8')


def test_dist_invalid(app):
    r = app.post('/distance', data={
            'x1': 'dflbvg',
            'y1': 'no',
            'x2': '5',
            'y2': '5'})
    assert r.status_code == 200
    assert 'Invalid Input' in r.data.decode('utf-8')


def test_email_invalid(app):
    r = app.post('/email', data={'email_input': 'skjfslkf'})
    assert r.status_code == 200
    assert 'Invalid Input' in r.data.decode('utf-8')


def test_email_valid(app):
    r = app.post('/email', data={'email_input': 'ajm712@msstate.edu'})
    assert r.status_code == 200
    assert 'Email is Validated' in r.data.decode('utf-8')


def test_bmi_no_input(app):
    r = app.get('/bmi')
    assert r.status_code == 200
    assert 'Body Mass Index Calculator' in r.data.decode('utf-8')


def test_bmi_input(app):
    r = app.post('/bmi', data={
        'f': '5',
        'i': '7',
        'p': '150'})
    assert r.status_code == 200
    assert '24.1' in r.data.decode('utf-8')


def test_bmi_invalid(app):
    r = app.post('/bmi', data={
        'f': '6',
        'i': 'helloworld',
        'p': '150'})
    assert r.status_code == 200
    assert 'Invalid Input' in r.data.decode('utf-8')


def test_retire_no_input(app):
    r = app.get('/retirement')
    assert r.status_code == 200
    assert 'Retirement Age Calculator' in r.data.decode('utf-8')


def test_retire_input(app):
    r = app.post('/retirement', data={
        'Current age': '23',
        'Annual salary': '60000.00',
        'Percent saved': '10',
        'Savings goal': '100000'})
    assert r.status_code == 200
    assert "You will meet your savings goal at age 35" in r.data.decode('utf-8')


def test_retire_input_unreached_goal(app):
    r = app.post('/retirement', data={
        'Current age': '23',
        'Annual salary': '60000.00',
        'Percent saved': '10',
        'Savings goal': '1000000'})
    assert r.status_code == 200
    assert "Sorry, your goal won't be met." in r.data.decode('utf-8')


def test_retire_invalid(app):
    r = app.post('/retirement', data={
        'Current age': '2d3',
        'Annual salary': '6000sdf0.00',
        'Percent saved': '10sdfs',
        'Savings goal': '100000df'})
    assert r.status_code == 200
    assert "Invalid Input" in r.data.decode('utf-8')

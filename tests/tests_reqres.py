import schemas.schemas
from api.reqres import get_list_users, post_create_users, update_user, get_user, delete_user
from pytest_voluptuous import S


def test_list_users():
    response = get_list_users(params={"page": 2})
    print(response.json())
    assert response.status_code == 200
    assert response.json()['page'] == 2
    assert len(response.json()['data']) != 0


def test_create_user_schema(name='Elena', job='QA engineer'):
    response = post_create_users(name, job)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert response.json() == S(schemas.schemas.create_user_schema)


def test_get_user_schema(id_user=6):
    response = get_user(id_user)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['data']['id'] == 6
    assert response.json()['data']['email'] == 'tracey.ramos@reqres.in'
    assert response.json()['data']['first_name'] == 'Tracey'
    assert response.json()['data']['last_name'] == 'Ramos'
    assert response.json() == S(schemas.schemas.get_user_schema)


def test_update_user_schema(id_user='4', name='test', job='engineer'):
    response = update_user(id_user, name, job)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert response.json() == S(schemas.schemas.update_user_schema)


def test_delete_user(id_user=4):
    response = delete_user(id_user)
    assert response.status_code == 204


def test_get_all_cats_with_no_records(client):
    # Act
    response = client.get("/cats")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_cat(client, two_saved_cats):
    # Act
    response = client.get("/cats/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Ocean",
        "personality": "brave",
        "color":"blue"
    }

def test_create_one_cat(client):
    # Act
    response = client.post("/cats", json={
        "name": "New Cat",
        "personality": "The Best!",
        "color": "amazing"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Cat",
        "personality": "The Best!",
        "color": "amazing"
    }
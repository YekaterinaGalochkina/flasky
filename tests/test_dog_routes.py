def test_get_all_dogs_with_no_records(client):
    # Act
    response = client.get("/dogs")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_cat(client, two_saved_dogs):
    # Act
    response = client.get("/dogs/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Ocean",
        "temperament": "brave",
        "color":"blue",
        "is_vaccinated": False
    }

def test_create_one_dog(client):
    # Act
    response = client.post("/dogs", json={
        "name": "New Dog",
        "temperament": "The Best!",
        "color": "amazing",
        "is_vaccinated": False
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Dog",
        "temperament": "The Best!",
        "color": "amazing",
        "is_vaccinated": False
    }
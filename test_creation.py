import send_req


def test_order_creation_and_retrieval():
    response = send_req.post_new_order()
    assert response.status_code == 201, "Expected 201, but got {}".format(response.status_code)
    track_number = response.json()["track"]

    response = send_req.get_order_by_track(track_number)

    assert response.status_code == 200, "Expected 200, but got {}".format(response.status_code)

# Привет, мир! by Alex Polukazakov!

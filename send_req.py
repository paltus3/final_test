import requests
import conf


def post_new_order():
    url = conf.URL + conf.CREATE_ORDER_PATH
    body = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Вашингтон",
        "metroStation": "4",
        "phone": "12345678910",
        "rentTime": 5,
        "deliveryDate": "2023-10-25",
        "comment": "Ye djn b pfxtv ns 'nj cltkfk",
        "color": "BLACK"
    }

    return requests.post(url, json=body, headers=conf.HEADERS)


def get_order_by_track(track_number):
    url = conf.URL + conf.GET_ORDER_BY_TRACK_PATH + "?t=" + str(track_number)
    return requests.get(url, headers=conf.HEADERS)
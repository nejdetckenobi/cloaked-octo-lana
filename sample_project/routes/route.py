from flask import Blueprint, request

route = Blueprint(__name__, "sample_route")


@route.route('/hello', methods=['GET', 'POST'])
def hello():
    return request.method

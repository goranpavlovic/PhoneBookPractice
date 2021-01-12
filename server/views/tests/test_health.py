import pytest
import logging
from flask import url_for


@pytest.mark.options(debug=False)
def test_app(app):
    assert not app.debug, 'Ensure the app not in debug mode'


def test_health_check(client, caplog):

    logging.debug("Debug log level!!!")
    logging.info("Info log level!!!")
    logging.warning("Warning log level!!!")
    logging.error("Error log level!!!")
    logging.critical("Critical log level!!!")

    response = client.get(url_for('server.views.infrastructure.health_check'))
    assert response.status_code == 200
    assert 'status' in response.json.keys()

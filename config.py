# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
"""Optional logging configuration, with no import-time side effects."""
import logging

class HerokuConfig:
    @classmethod
    def init_app(cls, app):
        handler = logging.StreamHandler()
        handler.setLevel(logging.WARNING)
        app.logger.addHandler(handler)

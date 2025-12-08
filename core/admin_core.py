from config.config import ADMIN_USERNAME, ADMIN_PASSWORD

class AdminCore:

    def validate(self, username, password):
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

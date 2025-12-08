# utils/validation.py

# Admin login credentials
ADMIN_CREDENTIALS = {
    "admin": "password123"  # Change as needed
}


def validate_admin(admin_id, password):
    """
    Returns True if admin login is correct
    """
    return ADMIN_CREDENTIALS.get(admin_id) == password


def validate_employee_name(name):
    """
    Simple employee name validation
    """
    if not name:
        return False
    if len(name) < 2:
        return False
    return True

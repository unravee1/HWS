from uuid import uuid4


def generate_password_reset_id() -> str:
    """ Generation new password."""
    return str(uuid4())

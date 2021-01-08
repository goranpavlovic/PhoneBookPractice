"""
Create entry
"""

from yoyo import step

__depends__ = {}


FORWARD_STEP_CREATE_ENTRY = f"""
    CREATE TABLE entry (
        id SERIAL PRIMARY KEY,
        "firstName" VARCHAR NOT NULL,
        "lastName" VARCHAR NOT NULL
    )
"""

BACKWARD_STEP_DROP_ENTRY = f"""
    DROP TABLE IF EXISTS entry
"""


steps = [
    step(FORWARD_STEP_CREATE_ENTRY, BACKWARD_STEP_DROP_ENTRY),
]

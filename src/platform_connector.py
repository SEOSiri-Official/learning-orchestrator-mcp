# src/platform_connector.py
import hmac
import hashlib
import time

SHARED_SECRET_KEY = b"seosiri_learning_platform_secret_2026"

def generate_sync_token(student_id: str, current_level: int, interval_days: int) -> str:
    """
    Generates a secure cryptographic sync token for external AI platforms,
    preventing state manipulation during cross-platform API handshakes.
    """
    payload = f"{student_id}:{current_level}:{interval_days}:{int(time.time() / 3600)}".encode('utf-8')
    return hmac.new(SHARED_SECRET_KEY, payload, hashlib.sha256).hexdigest()

def verify_platform_handshake(student_id: str, token: str, current_level: int, interval_days: int) -> bool:
    """Verifies the incoming handshake from the external AI platform is authentic."""
    expected_token = generate_sync_token(student_id, current_level, interval_days)
    return hmac.compare_digest(expected_token, token)

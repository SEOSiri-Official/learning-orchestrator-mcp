# tests/test_learning.py
import json
import os
import sys

# Force the project root directory into the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main_server import get_progressive_syllabus, calculate_spaced_repetition, sync_ai_platform_state
from src.platform_connector import verify_platform_handshake

def test_syllabus_retrieval():
    result_raw = get_progressive_syllabus("robotics", 2)
    result = json.loads(result_raw)
    assert result["status"] == "SYLLABUS_RETRIEVED"
    assert result["lesson_plan"]["title"] == "G-Code Instruction Syntax"

def test_spaced_repetition_logic():
    result_raw = calculate_spaced_repetition(grade_1_5=5, repetition_count=3, previous_ease_factor=2.5, previous_interval_days=6)
    result = json.loads(result_raw)
    assert result["status"] == "REVIEW_SCHEDULED"
    assert result["next_interval_days"] == 15
    assert result["updated_ease_factor"] == 2.6

def test_ai_platform_handshake_verification():
    # 1. Initialize active handshake
    sync_raw = sync_ai_platform_state("student_123", current_level=2, interval_days=6)
    sync_data = json.loads(sync_raw)
    assert sync_data["status"] == "CONNECTION_ESTABLISHED"
    token = sync_data["next_sync_token"]
    
    # 2. Verify handshake works cleanly
    assert verify_platform_handshake("student_123", token, current_level=2, interval_days=6) == True
    
    # 3. Verify tampered data gets blocked
    assert verify_platform_handshake("student_123", token, current_level=3, interval_days=6) == False

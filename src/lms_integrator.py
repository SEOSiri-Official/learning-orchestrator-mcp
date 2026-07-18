# src/lms_integrator.py
import json
from datetime import datetime, timezone
from src.platform_connector import generate_sync_token

def map_scorm_score_to_grade(quiz_score_pct: float) -> int:
    """Maps raw LMS SCORM quiz scores to standard 1-5 SM-2 grades."""
    if quiz_score_pct >= 90.0:
        return 5
    elif quiz_score_pct >= 80.0:
        return 4
    elif quiz_score_pct >= 70.0:
        return 3
    elif quiz_score_pct >= 50.0:
        return 2
    return 1

def sync_lms_scorm_activity(lms_student_id: str, scorm_package_id: str, quiz_score_pct: float, repetition_count: int, previous_ease_factor: float, previous_interval_days: int) -> dict:
    """
    LMS LTI/SCORM Sync Bridge: Consumes raw corporate onboarding metrics,
    translates them to SM-2 grades, schedules the next adaptive review, 
    and generates an authorized LTI Outcomes payload.
    """
    # Local import to prevent Python circular dependency errors
    from src.main_server import calculate_spaced_repetition
    
    clean_student_id = lms_student_id.strip()
    
    # 1. Map raw SCORM performance to SM-2 grade scale
    grade = map_scorm_score_to_grade(quiz_score_pct)
    
    # 2. Calculate next adaptive spacing interval
    sm2_res_raw = calculate_spaced_repetition(
        grade_1_5=grade,
        repetition_count=repetition_count,
        previous_ease_factor=previous_ease_factor,
        previous_interval_days=previous_interval_days
    )
    sm2_res = json.loads(sm2_res_raw)
    
    # 3. Generate a secure LTI sync token for Moodle/Canvas integration
    next_level = sm2_res["next_repetition_count"]
    next_interval = sm2_res["next_interval_days"]
    lti_signature = generate_sync_token(clean_student_id, next_level, next_interval)
    
    return {
        "status": "LMS_SYNC_SUCCESS",
        "lms_student_id": clean_student_id,
        "scorm_package_id": scorm_package_id,
        "mapped_grade": grade,
        "sm2_metrics": {
            "next_repetition": next_level,
            "next_interval_days": next_interval,
            "updated_ease_factor": sm2_res["updated_ease_factor"],
            "next_review_date": sm2_res["next_review_date"]
        },
        "lti_outcomes_payload": {
            "lis_result_sourcedid": f"{clean_student_id}:{scorm_package_id}",
            "lis_outcome_service_url": "https://moodle.seosiri.com/mod/lti/service.php",
            "score": round(quiz_score_pct / 100.0, 4),
            "lti_handshake_signature": lti_signature
        }
    }

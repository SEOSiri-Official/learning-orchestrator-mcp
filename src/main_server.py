# src/main_server.py
import os
import sys

# Force the project root directory into the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from datetime import datetime, timezone, timedelta
from mcp.server.fastmcp import FastMCP
from src.platform_connector import generate_sync_token, verify_platform_handshake

mcp = FastMCP("SEOSiri-Learning-Orchestrator")

# Global, deterministic database of segmented modular syllabi
SYLLABUS_DATABASE = {
    "robotics": {
        "1": {"title": "Cartesian Coordinate Systems", "objective": "Understand X, Y, Z coordinate transformations in SI units."},
        "2": {"title": "G-Code Instruction Syntax", "objective": "Formulate valid G1 linear movement commands with specific feedrates."},
        "3": {"title": "Decoupled Kinematics", "objective": "Deconstruct biological concentration vectors into physical coordinate deltas."}
    },
    "security": {
        "1": {"title": "Credential Sanitization", "objective": "Identify and redact exposed API keys and bearer tokens in transit."},
        "2": {"title": "OWASP Injection Vectors", "objective": "Detect and block SQL and shell execution command injections."},
        "3": {"title": "Cryptographic Attestation", "objective": "Implement HMAC-SHA256 signature verification to protect serial communication."}
    },
    "seo": {
        "1": {"title": "Structured Schema Metadata", "objective": "Construct valid JSON-LD schemas incorporating nested technical articles."},
        "2": {"title": "SEO & Privacy Compliance", "objective": "Implement GDPR raw IP address redactions alongside canonical URL validations."},
        "3": {"title": "Answer Engine Optimization (AEO)", "objective": "Structure conversational Q&A blocks to optimize for generative voice search."}
    }
}

@mcp.tool()
def get_progressive_syllabus(subject_segment: str, current_mastery_level: int = 1) -> str:
    """Retrieves the exact deterministic lesson plan based on the student's mastery level."""
    segment = subject_segment.lower().strip()
    level_str = str(current_mastery_level)
    
    if segment not in SYLLABUS_DATABASE:
        return json.dumps({"error": f"Invalid segment. Choose from: {list(SYLLABUS_DATABASE.keys())}"})
        
    lesson = SYLLABUS_DATABASE[segment].get(level_str, {"title": "Advanced Research", "objective": "Sovereign project implementation."})
    return json.dumps({
        "subject_segment": segment,
        "current_mastery_level": current_mastery_level,
        "lesson_plan": lesson,
        "status": "SYLLABUS_RETRIEVED"
    })

@mcp.tool()
def generate_skills_assessment(subject_segment: str, target_level: int, cognitive_dimension: str = "apply") -> str:
    """Generates targeted questions mapped strictly to Bloom's Taxonomy cognitive dimensions."""
    segment = subject_segment.lower().strip()
    dimension = cognitive_dimension.lower().strip()
    
    assessment_bank = {
        "security": {
            "apply": "Write a regex pattern in Python to detect and redact a US Social Security Number (SSN) formatted as XXX-XX-XXXX.",
            "analyze": "In a three-tier architecture, explain why baking safety-envelope validation into the MCP tool itself violates decoupled security principles."
        },
        "robotics": {
            "apply": "Calculate the physical X displacement in millimeters for a 96-well plate well target of 'C4' (using a standard 9.0mm pitch).",
            "analyze": "Explain why a G-code feedrate must be dynamically decreased as the pipetting reagent's viscosity increases."
        },
        "seo": {
            "apply": "Write a valid JSON-LD schema block representing a SoftwareApplication with an MIT License.",
            "analyze": "Explain how Google's generative AI crawlers use unstructured conversational FAQ blocks to answer voice search queries."
        }
    }
    
    if segment not in assessment_bank:
        return json.dumps({"error": f"Invalid segment. Choose from: {list(assessment_bank.keys())}"})
        
    question = assessment_bank[segment].get(dimension, "Generate a custom project proposal demonstrating practical implementation of your core code.")
    return json.dumps({
        "subject_segment": segment,
        "mastery_target_level": target_level,
        "bloom_dimension": dimension.upper(),
        "assigned_question": question
    })

@mcp.tool()
def calculate_spaced_repetition(grade_1_5: int, repetition_count: int, previous_ease_factor: float, previous_interval_days: int) -> str:
    """Calculates the exact next optimal review date using the standardized SuperMemo SM-2 algorithm."""
    grade = max(0, min(grade_1_5, 5))
    repetition = max(1, repetition_count)
    ease_factor = max(1.3, previous_ease_factor)
    interval = max(1, previous_interval_days)
    
    if grade < 3:
        return json.dumps({
            "quality_grade": grade,
            "next_repetition_count": 1,
            "next_interval_days": 1,
            "updated_ease_factor": ease_factor,
            "next_review_date": (datetime.now(timezone.utc) + timedelta(days=1)).isoformat().replace("+00:00", "Z"),
            "status": "RE_STUDY_REQUIRED"
        })
        
    if repetition == 1:
        next_interval = 1
    elif repetition == 2:
        next_interval = 6
    else:
        next_interval = int(interval * ease_factor)
        
    next_ease_factor = ease_factor + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02))
    next_interval_days = max(1, next_interval)
    
    next_review_date = (datetime.now(timezone.utc) + timedelta(days=next_interval_days)).isoformat().replace("+00:00", "Z")
    
    return json.dumps({
        "quality_grade": grade,
        "next_repetition_count": repetition + 1,
        "next_interval_days": next_interval_days,
        "updated_ease_factor": round(max(1.3, next_ease_factor), 3),
        "next_review_date": next_review_date,
        "status": "REVIEW_SCHEDULED"
    })

@mcp.tool()
def sync_ai_platform_state(student_id: str, current_level: int, interval_days: int, platform_token: str = "") -> str:
    """AI Platform Connector: Verifies and synchronizes student progress with external platforms."""
    clean_id = student_id.strip()
    
    if platform_token:
        is_valid = verify_platform_handshake(clean_id, platform_token, current_level, interval_days)
        if not is_valid:
            return json.dumps({
                "status": "CONNECTION_REJECTED",
                "reason": "INVALID_OR_TEMPERED_HANDSHAKE_TOKEN",
                "student_id": clean_id
            })
        print(f"[Connector] Verified secure handshake for student: {clean_id}")
        
    new_token = generate_sync_token(clean_id, current_level, interval_days)
    return json.dumps({
        "status": "CONNECTION_ESTABLISHED",
        "student_id": clean_id,
        "synchronized_level": current_level,
        "synchronized_interval": interval_days,
        "next_sync_token": new_token
    })

@mcp.tool()
def sync_lms_onboarding_state(lms_student_id: str, scorm_package_id: str, quiz_score_pct: float, repetition_count: int, previous_ease_factor: float, previous_interval_days: int) -> str:
    """
    LMS Sync Bridge: Integrates with Moodle/Canvas LTI services. Parses raw 
    SCORM quiz scores, executes SM-2 scheduling, and outputs a signed LTI payload.
    """
    from src.lms_integrator import sync_lms_scorm_activity
    res = sync_lms_scorm_activity(
        lms_student_id=lms_student_id,
        scorm_package_id=scorm_package_id,
        quiz_score_pct=quiz_score_pct,
        repetition_count=repetition_count,
        previous_ease_factor=previous_ease_factor,
        previous_interval_days=previous_interval_days
    )
    return json.dumps(res)

if __name__ == "__main__":
    import time
    time.sleep(0.5)
    mcp.run(transport='stdio')

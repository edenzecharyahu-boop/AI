# קובץ 2 – החוזה של הפלט
# המודל מחזיר טקסט. אנחנו בודקות שהוא JSON לפי הסכימה.
# אם נשבר – הודעת כשל ברורה, בלי לקרוס.

import json

from pydantic import BaseModel, ValidationError
from typing import Literal


class IntentResult(BaseModel):
    intent: Literal["order", "hours", "other"]
    in_scope: bool
    answer: str


def parse_output(text: str) -> tuple[dict | None, str]:
    raw = (text or "").strip()
    if raw.startswith("```"):
        raw = raw.strip("`")
        if raw.lower().startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    start, end = raw.find("{"), raw.rfind("}")
    if start >= 0 and end > start:
        raw = raw[start : end + 1]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None, "המודל לא החזיר JSON תקין."

    try:
        parsed = IntentResult.model_validate(data)
        return parsed.model_dump(), ""
    except ValidationError as exc:
        field = exc.errors()[0].get("loc", ("?",))[0]
        return None, f"ה-JSON לא עמד בסכימה (שדה {field})."

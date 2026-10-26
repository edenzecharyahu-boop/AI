# הפונקציה בעולם האמיתי.
# המודל לעולם לא נכנס לכאן. הוא רק מבקש שנריץ.

import json

CAPITALS = {
    "israel": "ירושלים",
    "ישראל": "ירושלים",
    "france": "פריז",
    "צרפת": "פריז",
    "japan": "טוקיו",
    "יפן": "טוקיו",
    "italy": "רומא",
    "איטליה": "רומא",
    "egypt": "קהיר",
    "מצרים": "קהיר",
    "spain": "מדריד",
    "ספרד": "מדריד",
}


def get_capital(country: str) -> str:
    capital = CAPITALS.get(
        country.strip().lower(),
        "לא ידוע – המדינה לא במאגר",
    )
    result = {
        "country": country,
        "capital": capital,
        "source": "המאגר שלנו",
    }
    return json.dumps(result, ensure_ascii=False)
import time
from typing import Dict, Any

class ProjectVortexEngine:
    def __init__(self):
        # Long-term Memory & State Management
        self.context_history = []
        self.current_topic_keywords = set()
        self.turn_count = 0
        
    def _extract_keywords(self, text: str) -> set:
        """Matndan asosiy kalit so'zlarni ajratib olish (sodda namuna)."""
        stop_words = {"va", "ham", "lekin", "uchun", "bu", "shunday", "haqida", "men", "sen", "deb"}
        words = set(text.lower().replace("?", "").replace("!", "").replace(".", "").split())
        return words - stop_words

    def check_topic_boundary(self, user_input: str) -> bool:
        """
        MODULE A: Context Reset & Topic Boundary Detection
        Yangi kiritilgan matn va eski mavzu o'rtasidagi bog'liqlikni tekshiradi.
        """
        new_keywords = self._extract_keywords(user_input)
        
        if not self.current_topic_keywords:
            self.current_topic_keywords = new_keywords
            return False

        # Asosiy kalit so'zlar mosligini hisoblash (Intersection)
        overlap = self.current_topic_keywords.intersection(new_keywords)
        
        # Agar yangi mavzuda eski so'zlardan deyarli bo'lmasa -> Topic Reset
        if len(overlap) == 0 and len(new_keywords) > 2:
            print("\n[VORTEX SYSTEM LOG: Topic Drift Detected! Resetting Attention Context...]")
            self.context_history.clear() # Context Reset
            self.current_topic_keywords = new_keywords
            self.turn_count = 0
            return True
        
        self.current_topic_keywords.update(new_keywords)
        return False

    def classify_intent(self, user_input: str) -> str:
        """Inputni anqiy (Scientific) yoki Falsafiy (Philosophical) toifaga ajratadi."""
        philosophical_triggers = {"fikr", "tushuncha", "maktab", "aqlli", "to'g'ri", "xato", "falsafa", "hayot", "kelajak"}
        words = self._extract_keywords(user_input)
        if words.intersection(philosophical_triggers):
            return "PHILOSOPHICAL"
        return "FACTUAL"

    def generate_response(self, user_input: str) -> Dict[str, Any]:
        """
        MODULE B & C: Dual-Mode Engine and Permission-Based Engagement Chips
        """
        self.turn_count += 1
        is_reset = self.check_topic_boundary(user_input)
        intent = self.classify_intent(user_input)
        
        response_data = {
            "context_reset_applied": is_reset,
            "mode": "",
            "main_response": "",
            "permission_chips": []
        }

        # MODULE B: Dual-Mode Logic
        if intent == "PHILOSOPHICAL":
            response_data["mode"] = "180° Contest Mode"
            response_data["main_response"] = (
                f"[180° Mirror Engine] Sening fikringga konstruktiv raqobat sifatida: "
                f"Keling, ushbu masalaga qarama-qarshi nuqtai nazardan qaraymiz..."
            )
            # MODULE C: Engagement Chips
            response_data["permission_chips"].append("Ready for a 180° intellectual debate?")
            response_data["permission_chips"].append("Want a historical counter-example?")
        else:
            response_data["mode"] = "0° Precision Mode"
            response_data["main_response"] = f"[Direct Answer] '{user_input}' bo'yicha aniq va loqayd ma'lumot."
            response_data["permission_chips"].append("Curious about a rare scientific fact related to this?")

        # Context update
        self.context_history.append({"user": user_input, "system": response_data["main_response"]})
        return response_data

# ==========================================
# AMALDA SINOV QILISH (DEMO EXECUTION)
# ==========================================
if __name__ == "__main__":
    vortex = ProjectVortexEngine()

    print("--- PROJECT VORTEX SYSTEM INITIALIZED ---\n")

    # 1-Suhbat: Falsafiy va Maktab haqida (User-Driven Error Correction)
    input1 = "Maktab haqida men tushuntirish beraman, uni o'quvchidan va iste'molchidan maslahat qilish kerak."
    print(f"User: {input1}")
    res1 = vortex.generate_response(input1)
    print(f"System ({res1['mode']}): {res1['main_response']}")
    print(f"UI Chips: {res1['permission_chips']}\n")

    # 2-Suhbat: Xuddi shu mavzuning davomi
    input2 = "Iste'molchi to'g'irlagan xatolar eng to'g'ri yechim deb bilaman."
    print(f"User: {input2}")
    res2 = vortex.generate_response(input2)
    print(f"System ({res2['mode']}): {res2['main_response']}")
    print(f"UI Chips: {res2['permission_chips']}\n")

    # 3-Suhbat: MAVZU KESKIN O'ZGARDi (Topic Boundary Detection & Context Reset Test)
    input3 = "Pifagor teoremasi bo'yicha uchburchak gipotenuzasini hisoblab ber."
    print(f"User: {input3}")
    res3 = vortex.generate_response(input3)
    print(f"System ({res3['mode']}): {res3['main_response']}")
    print(f"UI Chips: {res3['permission_chips']}\n")

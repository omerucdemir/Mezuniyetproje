from discord import ButtonStyle
from discord.ui import Button

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        """Satır içi klavye oluşturur."""
        buttons = []
        for i, option in enumerate(self.options):
            custom = f'choice_{i}'
            style = ButtonStyle.primary
            button = Button(label=option, style=style, custom_id=custom)
            buttons.append(button)
        return buttons

# Görev 4 - Listeyi sorularınızla doldurun
# Ana ve dal soru setleri:
quiz_branches = {
    "sayısal": [
        Question("Sayısal 1. soru?", 0, "A", "B"),
        Question("Sayısal 2. soru?", 0, "C", "D"),
    ],
    "sözel": [
        Question("Yazmayı ve okumayı sever misin?", 0, "Evet", "Hayır"),
        Question("Öğretmek mi Öğrenmek mi?", 0, "Öğrenmek", "Öğretmek"),
    ],
}

root_questions = [
    Question("Hangi türe yönelisin?", 0, "Sayısal", "Sözel"),
]



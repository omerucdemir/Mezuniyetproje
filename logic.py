from discord import ui, ButtonStyle

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        # Görev 3 - Satır içi klavyeyi oluşturmak için bir yöntem oluşturun
        buttons = []
        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'sayısal_{i}'))
            else:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'wrong_{i}'))
    
        return buttons

# Görev 4 - Listeyi sorularınızla doldurun
quiz_questions = [
   Question("Hangi türe yöneliklisin", 1, "Sayısal", "Sözel"),
   Question("Kediler sevgilerini nasıl ifade ederler?", 0, "Yüksek sesle mırıldanırlar", "Sevimli fotoğraflar", "Havlar"),
]



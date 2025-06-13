import discord
from discord.ext import commands
from logic import root_questions, quiz_branches
from discord.ui import View
# Görev 7 - defaultdict komutunu içe aktar
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="+", intents=intents)

# user_data[user_id] = {"branch": None, "question": 0, "answers": []}
user_data = {}


async def send_question(ctx_or_interaction, user_id):
    """Şu anki soruyu ilgili kullanıcıya yollar."""
    data = user_data[user_id]

    if data["branch"] is None:
        question = root_questions[0]
    else:
        question = quiz_branches[data["branch"]][data["question"]]

    view = View()
    for button in question.gen_buttons():
        view.add_item(button)

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(question.text, view=view)
    else:
        await ctx_or_interaction.followup.send(question.text, view=view)


@bot.command()
async def start(ctx):
    """Sınavı Başlat."""
    user_id = ctx.author.id
    user_data[user_id] = {"branch": None, "question": 0, "answers": []}
    await send_question(ctx, user_id)


@bot.event
async def on_interaction(interaction):
    """Butona tıklandığında cevapları işler."""
    user_id = interaction.user.id

    if user_id not in user_data:
        await interaction.response.send_message("Lütfen önce +start ile başlayın.")
        return

    data = user_data[user_id]
    idx = int(interaction.data['custom_id'].split('_')[1])

    if data["branch"] is None:
        # ilk cevap
        branch = root_questions[0].options[idx].lower()
        data["branch"] = branch
        data["question"] = 0
        data["answers"].append(root_questions[0].options[idx])

        await interaction.response.defer()
        await send_question(interaction, user_id)

    else:
        questions = quiz_branches[data["branch"]]
        question = questions[data["question"]]
        answer = question.options[idx]
        data["answers"].append(answer)

        data["question"] += 1

        if data["question"] >= len(questions):
            # sınav bitti
            await interaction.response.send_message(
                f"Sınav bitti! Cevaplarınızı şöyle verdiniz:\n" + 
                "\n".join([f"{i+1}. {ans}" for i, ans in enumerate(data["answers"])]),
                ephemeral=False
            )
            del user_data[user_id]
        else:
            await interaction.response.defer()
            await send_question(interaction, user_id)


@bot.event
async def on_ready():
    print(f'{bot.user} aktif!')

bot.run(TOKEN)
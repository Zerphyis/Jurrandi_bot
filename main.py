import discord 
import os
import datetime
from discord.ext import commands
from keep_alive import keep_alive



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
Dc_token = os.environ['DISCORD_TOKEN']


trello_url = "https://trello.com/b/1FD4o1Qu/tarefas"
planilha_url = "https://docs.google.com/spreadsheets/d/SEU_ID_AQUI"

    

@bot.command()
async def meet(ctx):
    await ctx.send("Aqui está o link para a reunião no Google Meet: https://meet.google.com/new")

@bot.command()
async def planilha(ctx):
    await ctx.send(f"Aqui está a planilha: {planilha_url}")

@bot.command()
async def midia(ctx, url: str):
    embed = discord.Embed()
    if url.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):  
        embed.set_image(url=url)
    else:
        embed.description = f"[Clique aqui para visualizar]({url})" 
    await ctx.send(embed=embed)

@bot.command()
async def tarefas(ctx):
    await ctx.send(f"📋 Acompanhe suas tarefas do dia aqui: {trello_url}")

@bot.command()
async def alterar_trello(ctx, nova_url: str):
    global trello_url
    trello_url = nova_url
    await ctx.send(f"✅ URL do Trello atualizada para: {nova_url}")

@bot.command()
async def alterar_planilha(ctx, nova_url: str):
    global planilha_url
    planilha_url = nova_url
    await ctx.send(f"✅ URL da planilha atualizada para: {nova_url}")


agendamentos = {}

@bot.command()
async def agendar(ctx, data: str, hora: str, *, descricao: str):
    """Agende uma reunião interna no formato /agendar DD-MM-YYYY HH:MM Descrição."""
    try:
        data_hora = datetime.datetime.strptime(f"{data} {hora}", "%d-%m-%Y %H:%M")
        agendamentos[data_hora] = descricao
        await ctx.send(f"📅 Reunião agendada para {data_hora.strftime('%d/%m/%Y %H:%M')}: {descricao}")
    except ValueError:
        await ctx.send("❌ Formato inválido! Use: `/agendar DD-MM-YYYY HH:MM Descrição`.")

@bot.command()
async def reunioes(ctx):
    """Lista todas as reuniões agendadas."""
    if not agendamentos:
        await ctx.send("📭 Nenhuma reunião agendada.")
    else:
        msg = "📌 **Reuniões Agendadas:**\n"
        for data_hora, descricao in sorted(agendamentos.items()):
            msg += f"📅 {data_hora.strftime('%d/%m/%Y %H:%M')} - {descricao}\n"
        await ctx.send(msg)


@bot.command()
async def comandos(ctx):
    """Lista todas as funcionalidades disponíveis e como usá-las."""
    comandos_info = (
        "📌 **Lista de Comandos:**\n"
        "`/meet` - Gera um link para uma reunião no Google Meet.\n"
        "`/planilha` - Mostra o link da planilha de trabalho.\n"
        "`/midia <url>` - Exibe uma imagem no chat ou um link para mídia.\n"
        "`/tarefas` - Mostra a lista de tarefas do dia no Trello.\n"
        "`/agendar <DD-MM-YYYY> <HH:MM> <descrição>` - Agenda uma reunião interna.\n"
        "`/reunioes` - Lista todas as reuniões agendadas.\n"
        "`/alterar_trello <nova_url>` - Altera a URL do Trello.\n"
        "`/alterar_planilha <nova_url>` - Altera a URL da planilha.\n"
    )
    await ctx.send(comandos_info)

keep_alive()
bot.run(Dc_token)

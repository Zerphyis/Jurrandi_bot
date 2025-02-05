# Jurrandi_bot

Este projeto é um bot para o Discord desenvolvido em Python, utilizando a biblioteca `discord.py`, com o objetivo de automatizar e simplificar a gestão de tarefas, reuniões e links importantes dentro de uma equipe. O bot oferece uma série de funcionalidades para facilitar a comunicação e organização, permitindo agendar reuniões, compartilhar links de recursos como Google Meet, Trello e planilhas de trabalho, além de exibir imagens e links de mídia diretamente no chat do Discord.

O bot possui os seguintes comandos:
- **/meet**: Gera um link para uma reunião no Google Meet.
- **/planilha**: Compartilha o link para a planilha de trabalho.
- **/midia <url>**: Exibe imagens ou links de mídia diretamente no chat.
- **/tarefas**: Exibe o link para a lista de tarefas do Trello.
- **/agendar <DD-MM-YYYY> <HH:MM> <descrição>**: Agenda uma reunião interna, permitindo que os membros da equipe saibam os compromissos futuros.
- **/reunioes**: Lista todas as reuniões agendadas.
- **/alterar_trello <nova_url>**: Altera a URL do Trello, permitindo uma atualização dinâmica do link de tarefas.
- **/alterar_planilha <nova_url>**: Altera a URL da planilha, facilitando o compartilhamento de documentos atualizados.

Além disso, o projeto inclui um servidor Flask simples, que roda em uma thread separada, permitindo que o bot permaneça ativo em servidores de hospedagem como Replit. Isso garante que o bot não se desconecte ou seja interrompido, mantendo sua funcionalidade sempre disponível.

O bot foi desenvolvido com o intuito de proporcionar uma experiência mais organizada e eficiente para as equipes que utilizam o Discord como ferramenta de comunicação, centralizando tarefas e recursos importantes em um único lugar, diretamente no ambiente de chat.

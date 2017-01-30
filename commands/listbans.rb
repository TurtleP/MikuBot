# listbans.rb
# list bans on the server

$bot.command(
	:listbans,
	min_args: 0,
	description: "List the users banned on the server.",
	usage: "listbans",
	help_available: true
) do | event |
	ban_list = event.server.bans

	if ban_list.length == 0
		event << "No users have been banned for this server."
		return
	else
		event << "List of banned users: #{ban_list}"
		return
	end
end

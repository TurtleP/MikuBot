$bot.command(
	:list_bans,
	required_permissions: [:manage_roles],
	min_args: 0,
	description: "List the users banned on the server.",
	usage: "list_bans",
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
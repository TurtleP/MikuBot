# ban.rb
# bans a user from the server

$bot.command(
	:ban,
	required_permissions: [:manage_roles],
	min_args: 2,
	description: "Bans a user on the server.",
	usage: "ban [user] [reason]",
	help_available: true
) do | event, mention, *reason |
	reason = reason.join(' ')

	user = event.message.mentions.first.on(event.server)

	user.pm("You have been banned from the server #{event.server.name}! Reason: #{reason}")
	
	event << "#{user.mention} has been banned! Reason: #{reason}"

	event.server.ban(user)

	event << nil
end


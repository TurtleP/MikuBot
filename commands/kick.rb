# kick.rb
# kicks a user from the server

$bot.command(
	:kick,
	required_permissions: [:manage_roles],
	min_args: 1,
	description: "Kicks a user on the server.",
	usage: "kick [user] (reason)",
	help_available: true
) do | event, mention, *reason |
	reason = reason.join(' ')

	user = event.message.mentions.first.on(event.server)

	user.pm("You have been kicked from the server #{event.server.name}! Reason: #{reason}")
	
	event << "#{user.mention} has been kicked! Reason: #{reason}"

	event.server.kick(user)

	event << nil
end

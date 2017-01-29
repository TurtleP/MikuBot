# slap.rb
# slaps a user on the server

$bot.command(
	:slap,
	min_args: 1,
	description: "Slaps a user on the server.",
	usage: "slap [user]",
	help_available: true
) do | event, mention |
	user = event.message.mentions.first.on(event.server)
	event << "#{user.mention} has been slapped by #{event.message.author().username}!"
end

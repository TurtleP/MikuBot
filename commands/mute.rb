# mute.rb
# mutes a user on the server

$bot.command(
	:mute,
	required_permissions: [:manage_roles],
	min_args: 1,
	description: "Mutes a user on the server.",
	usage: "mute [user]",
	help_available: true
) do | event |
	user = event.message.mentions.first.on(event.server)

	
end

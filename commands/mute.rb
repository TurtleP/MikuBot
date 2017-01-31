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

	mute_status = server.roles.find {|role| role.name == 'mute'}

	if user.role? mute_status
		event << "#{user.username} is already muted!"
	else
		user.add_role(mute_status)
	end
end

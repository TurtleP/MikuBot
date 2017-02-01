# unmute.rb
# unmutes a user on the server

$bot.command(
	:unmute,
	required_permissions: [:manage_roles],
	min_args: 1,
	description: "Unmutes a user on the server.",
	usage: "unmute [user] [reason]",
	help_available: true
) do | event |
	user = event.message.mentions.first.on(event.server)

	mute_status = server.roles.find {|role| role.name == 'mute'}

	if user.role? mute_status
		user.remove_role(mute_status)

		event << "#{user.mention} has been unmuted by #{event.message.author.username}!"
	else
		event << "#{user.username} is not muted!"
	end
end

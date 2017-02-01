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

	mute_status = event.server.roles.find do |role|
		role.name == "mute"
	end

	if !user.nil?
		if user.role? mute_status
			user.remove_role(mute_status)
			event << "#{user.mention} has been unmuted by #{event.message.author.username}!"
		else
			event << "#{user.username} is not muted!"
		end
	else
		event << "Could not find the specified user."
	end
end

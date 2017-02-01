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

	if user.role? mute_status
		channel_status = Discordrb::Permissions.new
		channel_status.can_send_messages = true

		channels = event.server.text_channels

		for i in 0 .. channels.length do
			channels[i].define_overwrite(user, channel_status, 0)
		end

		user.remove_role(mute_status)

		event << "#{user.mention} has been unmuted by #{event.message.author.username}!"
	else
		event << "#{user.username} is not muted!"
	end
end

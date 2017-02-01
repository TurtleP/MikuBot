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

	mute_status = event.server.roles.find do |role|
		role.name == "mute"
	end

	if user.role? mute_status
		event << "#{user.username} is already muted!"
	else
		channel_status = Discordrb::Permissions.new
		channel_status.can_send_messages = true

		channels = event.server.channels

		for i in 0 .. channels.length do
			channels[i].define_overwrite(user, 0, channel_status)
		end

		user.add_role(mute_status)

		event << "#{user.mention} has been muted by #{event.message.author.username}!"
	end
end

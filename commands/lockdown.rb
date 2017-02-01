# addstaff.rb
# adds a moderator to the server

$bot.command(
	:addstaff,
	required_permissions: [:manage_channels],
	min_args: 1,
	description: "Toggles locks on the current channel.",
	usage: "lockdown",
	help_available: true
) do | event |
	user = event.message.mentions.first.on(event.server)
    
end

# lockdown.rb
# locks the channel down

$bot.command(
	:lock,
	required_permissions: [:manage_channels],
	min_args: 0,
	description: "Locks the current channel.",
	usage: "lock",
	help_available: true
) do | event |
	break if event.channel.private?
	
	lockdown_status = Discordrb::Permissions.new
	lockdown_status.can_send_messages = true

	everyone_role = event.server.roles.find do |role|
	  role.name == "@everyone"
	end

	event.channel.define_overwrite(everyone_role, 0, lockdown_status)

	event << "Channel has been locked down! Only Staff may speak."
end

$bot.command(
	:unlock,
	required_permissions: [:manage_channels],
	min_args: 0,
	description: "Unlocks the current channel.",
	usage: "unlock",
	help_available: true
) do | event |
	break if event.channel.private?
	
	lockdown_status = Discordrb::Permissions.new
	lockdown_status.can_send_messages = true

	everyone_role = event.server.roles.find do |role|
	  role.name == "@everyone"
	end

	event.channel.define_overwrite(everyone_role, lockdown_status, 0)

	event << "Thanks for your co-operation!"
end

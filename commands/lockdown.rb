require 'discordrb'

# lockdown.rb
# locks the channel down

$bot.command(
	:lock,
	required_permissions: [:manage_channels],
	min_args: 0,
	description: "Sets message locks on the current channel.",
	usage: "lockdown",
	help_available: true
) do | event |
	if event.channel.private?
		break
	
	lockdown_status = Discordrb::Permissions.new
	lockdown_status.can_send_messages = false

	everyone_role = event.server.roles.find do |role|
	  role.name == "everyone"
	end

	event.channel.define_overwrite(everyone_role, 0, lockdown_status)

	event << "Channel has been locked down!"
end

$bot.command(
	:unlock,
	required_permissions: [:manage_channels],
	min_args: 0,
	description: "Sets message locks on the current channel.",
	usage: "lockdown",
	help_available: true
) do | event |
	if event.channel.private?
		break
	
	lockdown_status = Discordrb::Permissions.new
	lockdown_status.can_send_messages = true

	everyone_role = event.server.roles.find do |role|
	  role.name == "everyone"
	end

	event.channel.define_overwrite(everyone_role, 0, lockdown_status)

	event << "Thanks for your co-operation! :heart:"
end
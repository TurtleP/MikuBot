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

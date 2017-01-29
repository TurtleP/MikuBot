# sudo.rb
# sets someone to Sudo

$bot.command(
	:sudo,
	required_permissions: [:manage_channels],
	min_args: 0,
	description: "Toggles a Staff user's Sudo status.",
	usage: "sudo",
	help_available: true
) do | event |
	user = event.message.author()

	# use do keyword to split a block across lines
	sudo_status = event.server.roles.find do |role|
	  role.name == "sudo"
	end

	#check if they *are* Sudo
	if user.role? sudo_status
		user.remove_role(sudo_status)
		
		event << "mikubot#{user.mention}~$ sudo has been revoked!"
	else
		user.add_role(sudo_status)

		event << "mikubot#{user.mention}~$ sudo has been activated!"
	end
end

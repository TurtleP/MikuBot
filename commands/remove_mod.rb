# remove_mod.rb
# removes a user from Moderator status

$bot.command(
	:delstaff,
	required_permissions: [:manage_channels],
	min_args: 1,
	description: "Removes a user from Staff status.",
	usage: "delstaff [user]",
	help_available: true
) do | event |
	user = event.message.mentions.first.on(event.server)

	# use do keyword to split a block across lines
	mod_status = event.server.roles.find do |role|
		role.name == "staff"
	end

	#check if they *are* Moderator
	unless user.role? mod_status
	  event << "#{user.username} is not Staff!"
	  return
	end

	# set_role will wipe every other role the user has..
	# not sure if that's what you intended.
	user.remove_role(mod_status)

	# Prefer to use ruby string interpolation instead of concatenating (:
	# also, just user like you said would return a Discordrb::User object
	# and not their name.
	event << "Requim in spaghetti, #{user.mention}!"
end

# add_mod.rb
# adds a moderator to the server

$bot.command(
	:add_mod,
	required_permissions: [:manage_roles],
	min_args: 1,
	description: "Set a user to Staff status.",
	usage: "addstaff [user]",
	help_available: true
) do | event |
	user = event.message.mentions.first.on(event.server)

	# use do keyword to split a block across lines
	mod_status = event.server.roles.find do |role|
	  role.name == "staff"
	end

	#check if they *are* Moderator
	if user.role? mod_status
		event << "#{user.name} is already Staff!"
		return
	end

	# set_role will wipe every other role the user has..
	# not sure if that's what you intended.
	user.add_role(mod_status)

	# Prefer to use ruby string interpolation instead of concatenating (:
	# also, just user like you said would return a Discordrb::User object
	# and not their name.
	event << "Welcome to the Shadow Realm, #{user.mention}!"
end

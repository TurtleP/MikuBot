# unmute.rb
# unmutes a user on the server

$bot.command(
	:unmute,
	required_permissions: [:manage_roles],
	min_args: 1,
	description: "Mutes a user on the server.",
	usage: "unmute [user] [reason]",
	help_available: true
) do | event |
	user = event.message.mentions.first.on(event.server)

	#user.remove_role(mod_status)

	# Prefer to use ruby string interpolation instead of concatenating (:
	# also, just user like you said would return a Discordrb::User object
	# and not their name.
	#event << "Requim in spaghetti, #{user.mention}!"
end

# unban.rb
# unbans a user from the server

$bot.command(
	:unban,
	required_permissions: [:manage_roles],
	min_args: 1,
	description: "Remove the ban from a user on the server.",
	usage: "unban [user]",
	help_available: true
) do | event, *user |
	user = user.join(' ')

	banned_user = event.server.bans.find do | user_object |
		user_object.username == user
	end

	if banned_user.nil?
		event << "Could not find the specified user: #{user}!"
		return
	end

	event.server.unban(banned_user)
	
	event << "#{user} has been unbanned. Welcome back! :wave:"
end


# slap.rb
# slaps a user on the server

$bot.command(
	:slap,
	min_args: 1,
	description: "Slaps a user on the server.",
	usage: "slap [user]",
	help_available: true
) do | event |
	user = event.message.mentions.first.on(event.server)

	if user.nil?
		event << "Could not find the specified user."
	else
		if user.username == $bot.username
			event << "Nice try, #{event.message.author.username}."
		elseif user.username == event.message.author.username
			event << "You have slapped yourself. Good job, #{event.message.author.username} :ok_hand:"
		else
			event << "#{user.mention} has been slapped by #{event.message.author().username}!"
		end
	end
end

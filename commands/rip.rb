# rip.rb
# Press 'F' to pay respects

$bot.command(
	:rip,
	min_args: 0,
	description: "Pay respects",
	usage: "rip (user)",
	help_available: true
) do | event, *user |
    user = user.join(' ')

	user_obj = event.server.bans.find do | user_object |
		user_object.username == user
	end
	
	msg = "Press **_F_** to pay respects"
	
	if user_obj.nil?
		event << msg
	else
		event << msg + " to #{user.username}!"
	end
end

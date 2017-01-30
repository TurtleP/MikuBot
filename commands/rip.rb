# rip.rb
# Press 'F' to pay respects

$bot.command(
	:rip,
	min_args: 0,
	description: "Pay respects",
	usage: "rip (user)",
	help_available: true
) do | event |
	user = event.message.mentions.first.on(event.server)
	
	msg = "Press **_F_** to pay respects"
	
	if user.nil?
		event << msg
	else
		event << msg + " to #{user.username}!"
	end
end

# rip.rb
# Press 'F' to pay respects

$bot.command(
	:rip,
	min_args: 0,
	description: "Pay respects",
	usage: "rip (user)",
	help_available: true
) do | event |
	event << "Press **_F_** to pay respects"
end

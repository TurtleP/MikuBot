# soon.rb
# Produces soon:tm:

$bot.command(
	:soon,
	min_args: 0,
	description: "Generate soon:tm:",
	usage: "soon",
	help_available: true
) do | event |
	event << "soon:tm:"
end

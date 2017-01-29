# lenny.rb
# Produces a lenny face

$bot.command(
	:lenny,
	min_args: 0,
	description: "Replaces command with a lenny face",
	usage: "lenny",
	help_available: true
) do | event |
	event.message.edit("( ° ʖ °)")
end

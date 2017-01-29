# lenny.rb
# Produces a lenny face

$bot.command(
	:lenny,
	min_args: 0,
	description: "Replaces command with ( ° ʖ °)",
	usage: "lenny",
	help_available: true
) do | event |
	user = event.message.edit("( ° ʖ °)")

	event << nil
end

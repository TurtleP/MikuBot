
# kick.rb

# kicks a user from the server



$bot.command(

	:kick,

	required_permissions: [:manage_roles],

	min_args: 1,

	description: "Slaps a user on the server.",

	usage: "slap [user]",

	help_available: true

) do | event, mention |

	user = event.message.mentions.first.on(event.server)

	event << "#{user.mention} has been slapped!"

	event << nil

end

# sudo.rb

# sets someone to Sudo



$bot.command(

	:sudo,

	required_permissions: [:manage_roles],

	min_args: 1,

	description: "Set a user to Sudo status.",

	usage: "sudo [user]",

	help_available: true

) do | event |

	user = event.message.mentions.first.on(event.server)



	# use do keyword to split a block across lines

	sudo_status = event.server.roles.find do |role|

	  role.name == "sudo"

	end



	#check if they *are* Sudo

	if user.role? sudo_status
		
		user.remove_role(sudo_status)
		
		event << "#{user.mention}@mikubot~$ sudo has been revoked!"
		
		return

	end



	# set_role will wipe every other role the user has..

	# not sure if that's what you intended.

	user.add_role(sudo_status)



	# Prefer to use ruby string interpolation instead of concatenating (:

	# also, just user like you said would return a Discordrb::User object

	# and not their name.

	event << "#{user.mention}@mikubot~$ sudo has been activated!"
end

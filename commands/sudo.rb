# sudo.rb
# sets someone to Sudo

$bot.command(

	:sudo,

	required_permissions: [:manage_roles],

	min_args: 0,

	description: "Set a user to Sudo status.",

	usage: "sudo",

	help_available: true

) do | event |

	user = event.message.author(event.server)

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

	user.add_role(sudo_status)

	event << "#{user.mention}@mikubot~$ sudo has been activated!"
end

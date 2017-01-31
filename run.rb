require 'discordrb'
require 'yaml'

$bot = Discordrb::Commands::CommandBot.new token: ENV["token"], application_id: ENV["appid"].to_i, prefix: ENV["prefix"]
# $channel_perms = Discordrb::Permissions

Dir['commands/*.rb'].each do | command |
	puts "#Loaded: #{command}"
	require_relative command
end

$bot.ready do | event |
	avatar = File.open("media/avatar.jpg")
	
	$bot.profile.avatar = avatar

	$bot.game("$help")
end

$bot.run

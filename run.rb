require 'discordrb'
require 'yaml'

$bot = Discordrb::Commands::CommandBot.new token: ENV["token"], application_id: ENV["appid"].to_i, prefix: ENV["prefix"]

Dir['commands/*.rb'].each do | command |
	puts "#Loaded: #{command}"
	require_relative command
end

$bot.message(contains: 'I blame Turret') do |event|
	if rand(100) < 10
		event << 'Always~! :heart:'
	end
end

$bot.ready do | event |
	avatar = File.open("media/avatar.jpg")
	$bot.profile.avatar = avatar
end

$bot.run
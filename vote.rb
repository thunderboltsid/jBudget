require 'sinatra'
require 'yaml/store'


set :public_folder, File.dirname(__FILE__)


get '/' do
  @title = 'jBudget - Democratizing financial decision making'
  @poll = 'How much budget do you want to go to:'
  erb :index
end


post '/cast' do
  @title = 'Thanks for casting your vote!'
  @store = YAML::Store.new 'votes.yml'
  Choices.each do |id,text|
  	print id
  	print text
  	@store.transaction do
	  	@store[id] ||= {"key"=> id, "values"=> []}
	  	# @store[id]["values"] || []
		@store[id]["values"] = params[text]
	end
  end
  erb :cast
end


get '/results' do
  @title = 'Results so far:'
  @store = YAML::Store.new 'votes.yml'
  @votes = @store.transaction { @store['votes'] }
  erb :results
end

Choices = {
  'Campus Life' => '15',
  'Marketing' => '5',
  'Maintenance' => '15',
  'Dorms' => '25',
  'Faculty Staff' => '30',
  'Other Staff' => '10'
}
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
  @vote  = params['vote']
  @store = YAML::Store.new 'votes.yml'
  @store.transaction do
    @store['votes'] ||= {}
    @store['votes'][@vote] ||= 0
    @store['votes'][@vote] += 1
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
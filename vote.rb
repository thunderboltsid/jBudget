require 'sinatra'
require 'yaml/store'

class Array
  def sum
    inject(0.0) { |result, el| result + el }
  end

  def mean 
    sum / size
  end
end

set :public_folder, File.dirname(__FILE__)

get '/' do
  @title = 'jBudget - Democratizing financial decision making'
  @poll = 'How much budget do you want to go to:'
  erb :index
end


post '/cast' do
  @title = 'Thanks for casting your vote!'
  @store = YAML::Store.new 'votes.yml'
  @vote = {}
  Choices.each do |id,text|
  	@vote[id] = text
  	@store.transaction do
	  	@store[id] ||= {"key"=> id, "values"=> Array.new(), "avg" => 0}
		  @store[id]["values"] << params[id].to_i()
		  @store[id]["avg"] = @store[id]["values"].mean
	  end
  end
  erb :cast
end


get '/results' do
  @title = 'Results so far:'
  @store = YAML::Store.new 'votes.yml'
  @vote = {}
  sum = 0
  Choices.each do |id, text|
  	@store.transaction do
	  	sum += @store[id]["avg"]
	  end
  end
  Choices.each do |id, text|
    @store.transaction do
      @vote[id] = (@store[id]["avg"]/sum)*100
    end
  end
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
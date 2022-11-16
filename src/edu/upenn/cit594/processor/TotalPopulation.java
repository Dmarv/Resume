package edu.upenn.cit594.processor;

import edu.upenn.cit594.datamanagement.PopulationReader;

public class TotalPopulation {
	
	private PopulationReader population_reader;
	private int total_population = -1;
	
	public TotalPopulation( PopulationReader population_reader) {
		this.population_reader = population_reader;
		
	}
	
	public int calculateTotalPopulation() {
		if(this.total_population!=-1) {
			return this.total_population;
		}else {
			int population=0;
			for (Integer zip: population_reader.getPopulation().keySet()) {
				population += population_reader.getPopulation().get(zip);
			}
			
			this.total_population = population;
			
			return this.total_population;
			
		}
		
		
		
	}

}

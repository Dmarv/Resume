package edu.upenn.cit594.processor;

import java.util.HashMap;
import java.util.Map;

import edu.upenn.cit594.data.House;
import edu.upenn.cit594.datamanagement.PopulationReader;
import edu.upenn.cit594.datamanagement.PropertyReader;


public class TotalMarketValuePerCapita {
	
	private PopulationReader population_reader;
	protected PropertyReader property_reader;
	private Map<Integer, Integer> total_market_value_per_capita;
	
	public TotalMarketValuePerCapita ( PopulationReader population_reader ,  PropertyReader property_reader  ){
		this.population_reader = population_reader;
		this.property_reader =  property_reader;
		this.total_market_value_per_capita = new HashMap<Integer, Integer>();
	}
	
	public int CalculateTotalMarketValuePerCapita(int zip) {
		
		if(this.total_market_value_per_capita.containsKey(zip)) {
			return(this.total_market_value_per_capita.get(zip));
		}else {
			
			if( !this.population_reader.getPopulation().containsKey(zip)  || this.population_reader.getPopulation().get(zip)==0 ) {
				this.total_market_value_per_capita.put(zip, 0);
				return 0;
			}
			
			double total_value =0;
			
			for (House house: this.property_reader.getProperties() ) {
				double value=0;
				try {
					int house_zip = house.getZip_code();
					if(zip==house_zip) {
						value = Double.parseDouble( house.getMarket_value() );
					}
						
				}catch(Exception e) {}
				total_value += value;
			}
			
			int average_market_value_per_capita = 0;
			int population_count = this.population_reader.getPopulation().get(zip);
			
			
			average_market_value_per_capita = (int) Math.floor(total_value / population_count)  ;
			this.total_market_value_per_capita.put(zip , average_market_value_per_capita);
					
			return average_market_value_per_capita;
		}
		
		
		
	}
	
	

}

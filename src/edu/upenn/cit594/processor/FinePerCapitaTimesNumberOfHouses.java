package edu.upenn.cit594.processor;

import java.util.HashMap;
import java.util.Map;

import edu.upenn.cit594.data.House;
import edu.upenn.cit594.datamanagement.PropertyReader;
import edu.upenn.cit594.datamanagement.violationReader;

public class FinePerCapitaTimesNumberOfHouses {
	
	protected PropertyReader property_reader;

	protected violationReader  violation_reader;
	protected TotalFinePerCapita total_fine_per_capita;
	
	private Map<Integer, Double> total_fine_per_capita_times_house;
	
	public FinePerCapitaTimesNumberOfHouses(  PropertyReader property_reader,  TotalFinePerCapita total_fine_per_capita) {
		this.property_reader = property_reader;
		this.total_fine_per_capita = total_fine_per_capita;
		
		this.total_fine_per_capita_times_house = new HashMap<Integer, Double>();
	}
	
	public Double calculateFinePerCapitaTimesNumberOfHouses(int zip) {
		
		if(this.total_fine_per_capita_times_house.containsKey(zip)) {
			return(this.total_fine_per_capita_times_house.get(zip));
		}
		
		
		double total_fine;
		try {
			total_fine = this.total_fine_per_capita.CalculateTotalFinePerCapita().get(zip); 
		}catch(Exception e) {
			total_fine = 0.0;
		}
		
		
		
		int numberHouses=0;
		
		for (House house: this.property_reader.getProperties()  ) {
			if(house.getZip_code()==zip)
				numberHouses++;
		}
		
		double fine_times_house =   numberHouses * total_fine;
		fine_times_house = Math.floor(  fine_times_house *10000)/10000;
		this.total_fine_per_capita_times_house.put(zip, fine_times_house);
		
		return fine_times_house;
	}

}

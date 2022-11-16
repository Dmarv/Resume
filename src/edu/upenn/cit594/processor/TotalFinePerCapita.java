package edu.upenn.cit594.processor;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import edu.upenn.cit594.data.Violation;
import edu.upenn.cit594.datamanagement.PopulationReader;
import edu.upenn.cit594.datamanagement.violationReader;

public class TotalFinePerCapita {
	
	private PopulationReader population_reader;
	private violationReader  violation_reader;
	private Map<Integer, Double> total_fine_per_capita= null;
	
	public TotalFinePerCapita( PopulationReader population_reader , violationReader  violation_reader) {
		this.population_reader = population_reader;
		this.violation_reader = violation_reader;
		
		total_fine_per_capita = new TreeMap<Integer, Double>();
	}
	
	public Map<Integer, Double> CalculateTotalFinePerCapita() {
		
		if(this.total_fine_per_capita.size()>0) {
			return this.total_fine_per_capita;
		}else {
			
			List<Violation> violations = this.violation_reader.getAllViolation();
			Map<Integer, Integer> population = this.population_reader.getPopulation();
			
			Map<Integer, Integer> zipFine = new HashMap<Integer, Integer>();
			
			
			// getting the total violation for each zip code and storing it in zipFine 
			for (Violation violation:violations) {
				int zip= violation.getZip();
				int fine= violation.getFine();
				
				if(!violation.getState().toUpperCase().equals("PA")) {
					continue;
				}
				
				if(!zipFine.containsKey(zip)) {
					zipFine.put(zip, fine);
				}else {
					int value = zipFine.get(zip);
					zipFine.put(zip, fine+value );
				}
			}
			
			
			// calculating the fine per capita for each zip code
			for (Integer zip: population.keySet()) {
				
				if ( !zipFine.containsKey(zip) || !population.containsKey(zip)  || zipFine.get(zip)==0 || population.get(zip)==0 ) {
					continue;
				}
				
				double violation_per_capita = zipFine.get(zip) *1.0/population.get(zip);
				
				violation_per_capita = Math.floor(  violation_per_capita *10000)/10000;
				
				this.total_fine_per_capita.put(zip, violation_per_capita);
			}
		}

		
		return(this.total_fine_per_capita);
		
	}

}
